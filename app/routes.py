import csv
from flask import render_template, redirect, request, session, url_for
from app import app
from phishing_gpt import generate_phishing
from logger import log_result
from email_utils import send_email

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["user"] = request.form.get("username")
        return redirect(url_for("test"))
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        topic = request.form.get("topic")
        tone = request.form.get("tone")
        session["topic"] = topic
        session["tone"] = tone

        # Generate and store the phishing email
        session["email"] = generate_phishing(topic, tone)
        return redirect(url_for("respond"))
    return render_template("test.html")


@app.route("/respond", methods=["GET", "POST"])
def respond():
    if request.method == "POST":
        choice = request.form.get("choice")
        topic = session.get("topic")
        tone = session.get("tone")

        # Simple logic to give mock feedback (you can later GPT this)
        if choice == "click":
            outcome = "Unsafe - Clicked link"
            feedback = "⚠️ That could have compromised your system. The link and urgency were red flags."
        elif choice == "report":
            outcome = "Safe - Reported"
            feedback = "✅ Excellent! Reporting suspicious messages helps protect everyone."
        elif choice == "ignore":
            outcome = "Neutral - Ignored"
            feedback = "👍 Ignoring is better than clicking, but reporting is best."
        else:
            outcome = "Unknown"
            feedback = "❓ Something went wrong. No action recorded."

        # Save result to CSV
        log_result(topic, tone, choice, outcome)

        return render_template("result.html", email=session["email"], feedback=feedback)

    return render_template("respond.html", email=session.get("email"))


@app.route("/stats")
def stats():
    safe = unsafe = neutral = 0

    try:
        with open("logs/results.csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                outcome = row["Outcome"].lower()
                if "unsafe" in outcome:
                    unsafe += 1
                elif "safe" in outcome:
                    safe += 1
                elif "neutral" in outcome:
                    neutral += 1

    except FileNotFoundError:
        pass

    return render_template("stats.html", safe=safe, unsafe=unsafe, neutral=neutral)


@app.route("/send-email", methods=["GET", "POST"])
def send_email_route():
    if request.method == "POST":
        to_email = request.form.get("email")
        topic = request.form.get("topic")
        tone = request.form.get("tone")

        email_body = generate_phishing(topic, tone)
        send_email(to_email, f"[Phishing Simulation] Urgent {topic.title()} Message", email_body)

        return render_template("email_sent.html", email=email_body, recipient=to_email)

    return render_template("send_email.html")
