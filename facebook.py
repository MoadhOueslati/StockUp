from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
import re

class Worker(QThread):
    starting_process = pyqtSignal()
    finished_process = pyqtSignal()
    login_message = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, email, password, msg, msg_send_delay, target, messenger_group_link=None):
        super().__init__()
        self.driver = None
        self.email = email
        self.password = password
        self.msg = msg
        self.msg_send_delay = msg_send_delay
        self.messenger_group_link = messenger_group_link
        self.target = target
        self.facebook_login_link = "https://www.facebook.com/login.php/"
        self.data_file = "requirements.txt"

    def run(self):
        self.starting_process.emit()
        try:
            self.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or specify the path explicitly

            # Open Facebook login page
            self.driver.get(self.facebook_login_link)

            # Wait for the page to load and enter email
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(self.email)

            self.driver.find_element(By.NAME, "pass").send_keys(self.password)
            self.driver.find_element(By.NAME, "pass").send_keys(Keys.RETURN)

            # Wait for login to complete
            # time.sleep(5)
            self.login_message.emit()

            # Run the group messenger script if he gave the group messenger link
            if self.messenger_group_link and self.target == "Messenger Group":
                data = self.fetch_messenger_group_data()
                # FOR FINDING ALL THE USER IDS (EVEN REPEATED ONES)
                messenger_group_id = self.messenger_group_link.split("/")[-1]
                pattern = rf'\[5,"addParticipantIdToGroupThread",\[19,"{messenger_group_id}"],\[19,"(\d+)"\]'
                users_ids = re.findall(pattern, data)

                # CLEANING REPEATED USER_IDS
                cleaned_users_ids = []
                for user_id in users_ids:
                    if user_id not in cleaned_users_ids:
                        cleaned_users_ids.append(user_id)
                
                time.sleep(5)
                print(f"There are {len(cleaned_users_ids)} user ids :")
                print("="*100)
                print(cleaned_users_ids)
                print("="*100)
                time.sleep(5)
                
                # Starting sending messages for every single user 
                for user_id in cleaned_users_ids:
                    try:
                        time.sleep(5) # navigating between users
                        self.send_message_to_user(user_id)
                    except:
                        print(f"failed sending message to {user_id}")
            
            self.finished_process.emit()


        except Exception as e:
            # when about to publish to users make it say wrong email or password or .......... but not always sometimes errors happen suddenly
            print(f"An error occurred: {e}")
            self.error.emit(str(e))

    def send_message_to_user(self, user_id):
            # Navigate to a specific conversation
            self.driver.get(f"https://www.facebook.com/messages/t/{user_id}")

            # Because sometimes a stupid continue button appears
            try:
                # Use JavaScript to click the "Continue" button
                continue_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Continue')]"))
                )
                self.driver.execute_script("arguments[0].click();", continue_button)
                print("Clicked the 'Continue'.")
            except: pass

            message_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
            )

            # Send a message
            # time.sleep(self.msg_send_delay)
            pyperclip.copy(self.msg)
            message_input.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            message_input.send_keys(Keys.RETURN)
            time.sleep(self.msg_send_delay)


    def fetch_messenger_group_data(self):
        self.driver.get(self.messenger_group_link)

        time.sleep(10)

        with open(self.data_file, 'w', encoding='utf-8') as file:
            file.write(self.driver.page_source)

        time.sleep(10)

        # FOR CLEANING THE CONTENT FROM FUCKING BACKWARD SLASH :d
        with open(self.data_file, 'r') as file:
            content = file.read()

        content = content.replace('\\"', '"')

        with open(self.data_file, 'w') as file:
            file.write(content)

        return content

class Facebook:
    def __init__(self, mw):
        self.mw = mw
        self.email = None
        self.password = None
        self.msg = ""
        self.msg_send_delay = 0
        self.finished_process_message = "Sending messages process completed successfully."
        self.login_success_message = "Login Successful"
        self.starting_process_message = "Starting message sending process..."

        self.mw.sendMessagePushButton.clicked.connect(self.start_send_message_thread)

    def start_send_message_thread(self):
        self.msg = self.mw.messageTextEdit.toPlainText()
        if self.verify_sending_message(self.msg):
            self.email = self.mw.facebookEmailLineEdit.text()
            self.password = self.mw.facebookPasswordLineEdit.text()
            self.msg_send_delay = self.mw.messageDelaySpinBox.value()
            self.messenger_group_link = self.mw.groupLinkLineEdit.text()
            self.target = self.mw.targetComboBox.currentText()

            # Initialize the worker thread
            self.worker = Worker(self.email, self.password, self.msg, self.msg_send_delay, self.target, self.messenger_group_link)

            # Connect the worker's signals to the respective slots
            self.worker.starting_process.connect(self.started_sending_process)
            self.worker.finished_process.connect(self.finished_process)
            self.worker.error.connect(lambda message: self.display_plain_text_edit(f"Error: {message}"))
            self.worker.login_message.connect(lambda: self.display_plain_text_edit(f"\n{self.login_success_message}"))

            # Start the worker thread
            self.worker.start()
    
    def started_sending_process(self):
        self.mw.facebookConsolePlainTextEdit.setPlainText("") # Clear all previous messages.
        self.change_send_message_button_status(False)
        self.display_plain_text_edit(f"\n{self.starting_process_message}")

    def display_plain_text_edit(self, message=None):
        self.mw.facebookConsolePlainTextEdit.appendPlainText(message)

    def change_send_message_button_status(self, enabled):
        self.mw.sendMessagePushButton.setEnabled(enabled)

    def finished_process(self):
        self.change_send_message_button_status(True) #Enable The Start button back.
        self.display_plain_text_edit(f"\n{self.finished_process_message}")

    def verify_sending_message(self, msg):
        return bool(msg.split())


