import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QFileDialog, QWidget
from PyQt5.QtGui import QTextCursor, QPixmap, QTextImageFormat
from PyQt5.QtCore import Qt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import getpass
import os
import re

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit(self)
        self.insertImageButton = QPushButton("Insert Image", self)
        self.sendEmailButton = QPushButton("Send Email", self)
        
        self.insertImageButton.clicked.connect(self.insertImage)
        self.sendEmailButton.clicked.connect(self.sendEmail)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.insertImageButton)
        layout.addWidget(self.sendEmailButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.setWindowTitle("Email Sender with QTextEdit")
        self.resize(600, 400)

    def insertImage(self):
        # Open file dialog to select an image
        filePath, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        print(filePath)

        if filePath:
            # Load the image using QPixmap to get its original size
            pixmap = QPixmap(filePath)

            # Get the width of the image
            image_width = pixmap.width()
            image_height = pixmap.height()
            print(f"Original Image Width: {image_width} px")
            print(f"Original Image Height: {image_height} px")

            # Create a QTextImageFormat object
            imageFormat = QTextImageFormat()
            imageFormat.setName(filePath)

            if image_height > 400 or image_width > 400:
                # Set the desired width and height for the image
                desired_width = image_width // 2  # Change this value to control the width
                desired_height = image_height // 2 # Change this value to control the height
                imageFormat.setWidth(desired_width)
                imageFormat.setHeight(desired_height)

            # Get the QTextCursor at the current position
            cursor = self.textEdit.textCursor()
            
            # Insert the image with the specified format
            cursor.insertImage(imageFormat)

    def sendEmail(self):
        HOST = "smtp-mail.outlook.com"
        PORT = 587

        FROM_EMAIL = "moadhoueslati@outlook.com"
        TO_EMAIL = "moadhoueslati2@gmail.com"
        PASSWORD = getpass.getpass("Enter password: ")

        # Get the HTML content from the QTextEdit
        html_body = self.textEdit.toHtml()

        # Extract and embed images
        image_cid_map = {}
        pattern = r'<img src="([^"]+)"'
        matches = re.findall(pattern, html_body)

        message = MIMEMultipart()
        message["From"] = FROM_EMAIL
        message["To"] = TO_EMAIL
        message["Subject"] = "😍✨ CAN I GET AA HUG ?!!? ✨😍"

        for i, image_path in enumerate(matches):
            cid = f"image{i+1}"
            image_cid_map[image_path] = cid

            with open(image_path, "rb") as img:
                img_part = MIMEBase("image", "jpeg")
                img_part.set_payload(img.read())
                encode_base64(img_part)
                img_part.add_header("Content-ID", f"<{cid}>")
                img_part.add_header("Content-Disposition", f"inline; filename={os.path.basename(image_path)}")
                message.attach(img_part)

        # Replace image paths with cid references in the HTML
        for image_path, cid in image_cid_map.items():
            html_body = html_body.replace(image_path, f"cid:{cid}")

        # Attach the HTML body
        html_part = MIMEText(html_body, "html")
        message.attach(html_part)

        # Send the email
        with smtplib.SMTP(HOST, PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL, PASSWORD)
            server.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())

        print("Email sent with content from QTextEdit!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
