
# [5,"addParticipantIdToGroupThread",[19,"26241351905508371"],[19,"100006564133381"]
# [5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100006564133381\"]


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

facebook_link = "https://www.facebook.com/login/"
messenger_group_link = "https://www.facebook.com/messages/t/8276133572438903"
facebook_email = "moadh2002@hotmail.co.uk"
facebook_pass = "moadhos33890!?!"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Facebook login page
driver.get(facebook_link)

# Wait for the page to load and enter email
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(facebook_email)

# Enter password
driver.find_element(By.NAME, "pass").send_keys(facebook_pass)
driver.find_element(By.NAME, "pass").send_keys(Keys.RETURN)

time.sleep(5)

# Navigate to a specific conversation
driver.get(messenger_group_link)

time.sleep(5)

with open('output5.txt', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

time.sleep(5)

driver.quit()

time.sleep(5)

# FOR CLEANING THE CONTENT FROM FUCKING BACKWARD SLASH :d
with open('output5.txt', 'r') as file:
    content = file.read()

content = content.replace('\\"', '"')

with open('output5.txt', 'w') as file:
    file.write(content)


# FOR FINDING ALL THE USER IDS (EVEN REPEATED ONES)
group_id = messenger_group_link.split("/")[-1]

pattern = rf'\[5,"addParticipantIdToGroupThread",\[19,"{group_id}"],\[19,"(\d+)"\]'
users_ids = re.findall(pattern, content)

# CLEANING REPEATED USER_IDS
cleaned_users_ids = []
for user_id in users_ids:
    if user_id not in cleaned_users_ids:
        cleaned_users_ids.append(user_id)


print(f"There are {len(cleaned_users_ids)} user ids :")
print("="*100)
print(cleaned_users_ids)
print("="*100)








