# SEE-GPT 
UNFINISHED ! ! !
Need to setup up GPT API key but no $$$

**Social Engineering Engine powered by GPT**  
A phishing simulation platform that generates realistic social engineering attacks using OpenAI GPT. Designed for cybersecurity awareness training, user behavior tracking, and educational insight into social engineering tactics.

---

## Project Overview

**SEE-GPT** is a cybersecurity education tool that simulates phishing attacks through:
- GPT-generated emails
- User response logging (click, report, ignore)
- Real-time feedback
- Chart-based performance analytics
- Optional simulated email delivery

Built using Python, Flask, and Chart.js, the project highlights the fusion of **AI and cybersecurity** to raise awareness of social engineering tactics in modern threat landscapes.

---

##  Features

- GPT-generated phishing emails based on topic and tone
- Flask web interface for simulations
- Interactive response flow: Click, Report, or Ignore
- Real-time feedback based on user action
- CSV logging of all simulations
- Visual analytics dashboard with Chart.js
- (Optional) Email delivery via Gmail SMTP 

---

##  Tech Stack

- **Python** · Flask · OpenAI API (GPT-3.5/4)
- **Chart.js** for interactive charts
- **CSV Logging** for data analysis
- **Bootstrap** for simple UI
- **SMTP** (Gmail) for email simulation

---

##  Installation & Run

```bash
# Clone the repo
git clone https://github.com/lixeron/SEE-GPT.git
cd SEE-GPT

# Install dependencies
pip install -r requirements.txt

# Add .env file
touch .env
follow instructions in requirements
