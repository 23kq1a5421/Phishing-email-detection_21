
import re
from urllib.parse import urlparse
import ipaddress


def check_sender(sender):
    reasons = []

    sender = sender.strip()

    if sender.count("@") != 1:
        reasons.append("Invalid sender email format.")
        return reasons

    name, domain = sender.split("@")

    if not name or not domain or "." not in domain:
        reasons.append("Sender email address looks invalid.")

    if domain in ["gmail.com", "yahoo.com", "outlook.com"]:
        pass
    elif domain.endswith(".xyz") or domain.endswith(".top"):
        reasons.append("Sender uses a suspicious email domain.")

    return reasons


def check_keywords(subject, message):
    reasons = []

    suspicious_words = [
        "urgent",
        "verify your account",
        "password",
        "account suspended",
        "click here",
        "bank details",
        "free prize",
        "limited time",
        "confirm your identity"
    ]

    email_text = (subject + " " + message).lower()

    for word in suspicious_words:
        if word in email_text:
            reasons.append(
                "Suspicious keyword found: " + word
            )

    return reasons


def check_links(message):
    reasons = []

    urls = re.findall(
        r'https?://[^\s]+',
        message,
        re.IGNORECASE
    )

    suspicious_shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "is.gd"
    ]

    for url in urls:
        clean_url = url.rstrip(".,!?;:)")
        parsed_url = urlparse(clean_url)
        domain = parsed_url.hostname

        if not domain:
            continue

        if domain.lower() in suspicious_shorteners:
            reasons.append("Shortened URL detected.")

        try:
            ipaddress.ip_address(domain)
            reasons.append("Link uses an IP address instead of a domain name.")
        except ValueError:
            pass

        if parsed_url.scheme == "http":
            reasons.append("Link uses HTTP instead of HTTPS.")

    return reasons


def analyze_email(sender, subject, message):

    reasons = []

    reasons.extend(check_sender(sender))
    reasons.extend(check_keywords(subject, message))
    reasons.extend(check_links(message))

    risk_score = len(reasons)

    if risk_score >= 3:
        risk_level = "High Risk"
    elif risk_score >= 1:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "reasons": reasons
    }
