import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "moadhoueslati@outlook.com"
TO_EMAIL = "moadhoueslati2@gmail.com"
PASSWORD = getpass.getpass("Enter password: ")

# Specify image details
image_path = "C:/Users/ASUS/OneDrive/Desktop/Clients/Moadh/captured_image.png"  # Replace with your image path
image_name = "loudspeaker.png"  # Desired attachment name

# Create the message container
message = MIMEMultipart()
message["From"] = FROM_EMAIL
message["To"] = TO_EMAIL
message["Subject"] = "😍✨ New From StockUp! ✨😍"

# Create the HTML body
html_body = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            color: #5a5a5a;
            text-align: center;
        }}
        .image {{
            text-align: center;
            margin: 20px 0;
        }}
        .image img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }}
        .button {{
            display: inline-block;
            padding: 12px 25px;
            font-size: 16px;
            color: #fff;
            background-color: #4CAF50;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            margin: 10px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, box-shadow 0.3s;
        }}
        .button:hover {{
            background-color: #45a049;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }}
        .footer {{
            margin-top: 20px;
            font-size: 12px;
            color: #888;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌟 Welcome to StockUp! 🌟</h1>
        <div class="image">
            <img src="cid:image001" alt="Exclusive Accessory">
        </div>
        <p>Hello there,</p>
        <p>We are thrilled to unveil our latest accessories collection just for you! Browse through our exquisite collection and find the perfect accessory to enhance your style.</p>
        <p><a href="https://yourwebsite.com" class="button">Shop Now</a></p>
        <p>Hurry, these exclusive items are in high demand!</p>
        <div class="footer">
            <p>Thank you for being a valued customer.</p>
            <p>StockUp</p>
        </div>
    </div>
</body>
</html>
"""

# Create the text body
text_part = MIMEText("Limited edition purchase now!", "plain")
message.attach(text_part)

# Attach the HTML body
html_part = MIMEText(html_body, "html")
message.attach(html_part)

# Attach the image
with open(image_path, "rb") as attachment:
    img_part = MIMEBase("image", "jpeg")
    img_part.set_payload(attachment.read())
    encode_base64(img_part)
    img_part.add_header("Content-ID", "<image001>")
    img_part.add_header("Content-Disposition", f"attachment; filename={image_name}")

    # Attach the encoded image to the message
    message.attach(img_part)

# Send the email
with smtplib.SMTP(HOST, PORT) as server:
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())

print("Email sent with image attachment!")
