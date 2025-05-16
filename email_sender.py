from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import time
import os
import re
from text_editor import textEditor
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64


class EmailSender:
    def __init__(self, mw):
        self.mw = mw
        layout = QVBoxLayout()
        self.text_editor = textEditor()
        layout.addWidget(self.text_editor)
        self.mw.textEmailWidget.setLayout(layout)
        
        self.email = None
        self.password = None
        self.all_emails = []
        self.new_emails = []

        self.mw.emailSendPushButton.clicked.connect(self.sendEmail)

        self.mw.allCheckBox.stateChanged.connect(lambda: self.check(self.all_emails))
        self.enable_all_check_box_trigger = True

        self.mw.emailListWidget.itemChanged.connect(self.on_item_changed)

        self.worker = None  

    def on_item_changed(self, item):
        if item.checkState() == Qt.Unchecked:
            self.enable_all_check_box_trigger = False
            self.mw.allCheckBox.setCheckState(Qt.Unchecked)
            self.enable_all_check_box_trigger = True


    def refresh_list(self):
        # Fetch all emails
        all_emails = self.mw.fetch_all_data_by_column_name("Clients", "email")
        all_emails = [email for email in all_emails if len(email) != 0]  # remove the empty string emails 

        # Determine new emails that have been just added
        self.new_emails = [email for email in all_emails if email not in self.all_emails]

        # Adding the new emails and adding checkbox to them
        for email in self.new_emails:
            if email not in self.all_emails:
                self.mw.emailListWidget.addItem(email)
                self.all_emails.append(email)

        for i in range(self.mw.emailListWidget.count()):
            email = self.mw.emailListWidget.item(i)
            if email.text() in self.new_emails:
                email.setFlags(email.flags() | Qt.ItemIsUserCheckable)
                email.setCheckState(Qt.Unchecked)
        
        self.new_emails = []
        self.all_emails = all_emails

    def check(self, check_list):
        if self.enable_all_check_box_trigger:
            all_checked = self.mw.allCheckBox.isChecked()
            for i in range(self.mw.emailListWidget.count()):
                item = self.mw.emailListWidget.item(i)
                if item.text() in check_list:
                    item.setCheckState(Qt.Checked if all_checked else Qt.Unchecked)

    def get_email_recipients(self):
        to_emails = []
        for i in range(self.mw.emailListWidget.count()):
            item = self.mw.emailListWidget.item(i)
            if item.checkState() == Qt.Checked:
                to_emails.append(item.text())
        return to_emails

    def sendEmail(self):
        self.mw.emailConsolePlainTextEdit.setPlainText("") # Clear all previous messages.
        self.to_emails = self.get_email_recipients()
        if self.to_emails: 
            self.mw.emailSendPushButton.setEnabled(False)
            self.mw.emailConsolePlainTextEdit.setPlainText("Sending emails...")
            self.email = self.mw.emailLineEdit.text()
            self.password = self.mw.emailPasswordLineEdit.text()
            self.sending_delay = self.mw.emailDelaySpinBox.value()
            self.subject = self.mw.emailSubjectLineEdit.text()

            html_body = self.text_editor.editor.toHtml()
            pattern = r'<img src="([^"]+)"'
            matches = re.findall(pattern, html_body)

            if self.worker and self.worker.isRunning():
                self.worker.terminate()  

            self.worker = Worker(self.email, self.password, self.sending_delay, self.subject, self.to_emails, html_body, matches)
            self.worker.sent_email_to.connect(self.on_sent_email_to)
            self.worker.finished_process.connect(self.on_finished_sending_process)
            self.worker.start()
            
        else: 
            self.mw._handle_user_error("You must select at least 1 email to send the message to.")
        
    def on_sent_email_to(self, message):
        self.mw.emailConsolePlainTextEdit.appendPlainText(message)
    
    def on_finished_sending_process(self, message):
        self.mw.emailConsolePlainTextEdit.appendPlainText(message)
        self.mw.emailSendPushButton.setEnabled(True)


class Worker(QThread):
    sent_email_to = pyqtSignal(str)
    finished_process = pyqtSignal(str)

    def __init__(self, email, password, sending_delay, subject, to_emails, html_body, matches):
        super().__init__()
        self.email = email
        self.password = password
        self.sending_delay = sending_delay
        self.subject = subject
        self.to_emails = to_emails
        self.html_body = html_body
        self.matches = matches
        self.success_count = 0
        self.fail_count = 0

        # SMTP Setup
        self.host = "smtp-mail.outlook.com"
        self.port = 587

    def run(self):
        # Initialize the SMTP connection
        with SMTP(self.host, self.port) as server:
            server.starttls()  # Start TLS encryption
            server.login(self.email, self.password)  # Log in once

            for to_email in self.to_emails:
                time.sleep(self.sending_delay)
                try:
                    self.send_email(server, to_email)
                    self.sent_email_to.emit(f"Email successfully sent to {to_email}")
                    self.success_count += 1
                except Exception as e:
                    self.sent_email_to.emit(f"Failed to send email to {to_email} Error: {e}")
                    self.fail_count += 1

            # Notify completion
            self.finished_process.emit(f"\nTotal emails sent successfully: {self.success_count}\nTotal emails failed: {self.fail_count}")

    def send_email(self, server, to_email):
        image_cid_map = {}
        message = MIMEMultipart()
        message["From"] = self.email
        message["To"] = to_email
        message["Subject"] = self.subject

        for i, image_path in enumerate(self.matches):
            cid = f"image{i+1}"
            image_cid_map[image_path] = cid

            with open(image_path, "rb") as img:
                img_part = MIMEBase("image", "jpeg")
                img_part.set_payload(img.read())
                encode_base64(img_part)
                img_part.add_header("Content-ID", f"<{cid}>")
                img_part.add_header("Content-Disposition", f"inline; filename={os.path.basename(image_path)}")
                message.attach(img_part)

        for image_path, cid in image_cid_map.items():
            self.html_body = self.html_body.replace(image_path, f"cid:{cid}")

        html_part = MIMEText(self.html_body, "html")
        message.attach(html_part)

        server.sendmail(self.email, to_email, message.as_string())
