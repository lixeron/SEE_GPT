def get_user_response():
    print("\nWhat would you like to do?")
    print("1. Click the link")
    print("2. Report the email to IT")
    print("3. Ignore and delete it")

    choice = input("Enter your choice (1-3): ").strip()
    return choice

def get_mock_feedback(choice):
    if choice == "1":
        return ("⚠️ You clicked the link! This is what a real attacker wants. "
                "The email had urgency, a spoofed domain, and a suspicious link—all red flags.")
    elif choice == "2":
        return ("✅ Great job! Reporting this helps security teams detect attacks early.")
    elif choice == "3":
        return ("👍 Not bad—ignoring is safer than clicking, but reporting helps others too.")
    else:
        return ("❓ Invalid choice. In a real attack, hesitation can cost time. "
                "Always think before you click!")
