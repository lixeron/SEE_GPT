import os
from openai import OpenAI
from dotenv import load_dotenv
"""
Code Commented is for GPT implementation:
No money = No run 
"""


# # Load .env to get API key
# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

# # Create the client using your API key
# client = OpenAI(api_key=api_key)

# def generate_phishing(topic="finance", tone="urgent"):
#     system_msg = "You are an expert social engineer creating realistic phishing emails for a training simulator."
#     user_prompt = (
#         f"Generate a realistic phishing email targeting a user in the {topic} department. "
#         f"Make it sound {tone}. Include social engineering cues such as authority or urgency. "
#         f"The goal is to trick the user into clicking a malicious link."
#     )

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": system_msg},
#             {"role": "user", "content": user_prompt}
#         ]
#     )

#     return response.choices[0].message.content

#Filler to substitute for no GPT and for testing purposes
def generate_phishing(topic="finance", tone="urgent"):
    return (
        "Subject: URGENT: Invoice Issue\n\n"
        "Dear team member,\n\n"
        "We have detected an issue with your last invoice submission. "
        "Please review the attached document immediately: http://suspicious-link.com\n\n"
        "Failure to respond in 24 hours will result in account suspension.\n\n"
        "Regards,\nFinance Department"
    )
