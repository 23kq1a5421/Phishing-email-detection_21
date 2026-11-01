# Phishing Email Detection System

## Project Description
A Python and Flask-based web application that analyzes email senders, content, and links to identify potential phishing attempts and assess their risk level.

## Technologies Used
- Python
- Flask
- HTML
- CSS

## Features
- **Sender Email Analysis:** Checks sender email addresses for suspicious formats and domains.
- **Keyword Detection:** Identifies suspicious words such as urgent, verify your account, password, and account suspended.
- **Suspicious Link Detection:** Checks for shortened URLs, IP-based links, and HTTP links.
- **Risk Assessment:** Classifies emails into Low Risk, Medium Risk, or High Risk.
- **Detection Details:** Displays the reasons why an email was flagged.

## Project Structure

```text
Phishing_Email_Detection/
│
├── app.py
├── detector.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## How the Project Works

1. The user enters the sender email address, subject, and email message.
2. Flask receives the submitted information.
3. The detection module checks the sender, suspicious keywords, and links.
4. A risk score is calculated based on the detected warning signs.
5. The application displays the risk level and detection details.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Phishing_Email_Detection
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

## Risk Classification

| Risk Score | Risk Level |
|---|---|
| 0 | Low Risk |
| 1–2 | Medium Risk |
| 3 or more | High Risk |

## Learning Outcomes

- Understanding basic phishing detection techniques.
- Learning Python functions and conditional statements.
- Working with Flask to develop web applications.
- Connecting HTML and CSS with a Python backend.
- Understanding URL analysis and suspicious email indicators.

## Limitations

This project uses rule-based detection rather than a trained machine learning model. It identifies selected warning signs and cannot guarantee whether an email is genuinely safe or malicious.

## Future Enhancements

- Integrate machine learning for improved phishing detection.
- Add email attachment analysis.
- Improve URL reputation checking.
- Store previous email analysis results.
- Develop a more advanced security dashboard.

## Author

Salma Shaik

B-tech AI & Data Science Student
