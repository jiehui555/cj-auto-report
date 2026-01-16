import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional


def send_email(
    smtp_host: str,
    smtp_port: int,
    smtp_from: str,
    smtp_pass: str,
    to: str,
    subject: str,
    body: str,
    attachments: Optional[List[str]] = None,
    is_html: bool = True,
) -> None:
    """
    Send email

    Args:
        smtp_host: SMTP server host
        smtp_port: SMTP server port
        smtp_from: Sender email address
        smtp_pass: Sender email password
        to: Recipient email address
        subject: Email subject
        body: Email body content
        attachments: List of file paths to attach
        is_html: Whether body is HTML
    """
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = smtp_from
    message["To"] = to

    message.attach(MIMEText(body, "html" if is_html else "plain"))

    if attachments:
        for attachment_path in attachments:
            if os.path.exists(attachment_path):
                with open(attachment_path, "rb") as file:
                    filename = os.path.basename(attachment_path)
                    message.attach(MIMEApplication(file.read(), Name=filename))

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_from, smtp_pass)
        server.sendmail(smtp_from, [to], message.as_string())
        server.quit()
