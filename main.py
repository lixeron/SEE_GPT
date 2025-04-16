from phishing_gpt import generate_phishing
from interaction import get_user_response, get_mock_feedback
from logger import log_result
from analyze import summarize_results

def main():
    print("Welcome to SEE-GPT: Social Engineering Awareness Engine")

    topic = input("Choose a phishing topic (e.g., finance, HR, student portal): ").strip().lower()
    tone = input("Choose tone (e.g., urgent, friendly, threatening): ").strip().lower()

    print("\n[Simulated Phishing Email]")
    email = generate_phishing(topic, tone)
    print(email)

    user_choice = get_user_response()
    feedback = get_mock_feedback(user_choice)

    print("\n[Feedback]")
    print(feedback)
    
    
    if user_choice == "1":
        outcome = "Unsafe - Clicked link"
    elif (user_choice) == "2":
        outcome = "Safe - Reported"
    elif user_choice == "3":
        outcome = "Neutral - Ignored"
    else:
        outcome = "Invalid input"
        
    log_result(topic, tone, user_choice, outcome)
    print("\n Your response has been logged. Thank you for training safely!")
    summarize_results()
    
if __name__ == "__main__":
    main()
