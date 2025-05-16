from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

facebook_pass = "??????????"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Facebook login page
driver.get("https://www.facebook.com/login/")

# Wait for the page to load and enter email
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(facebook_email)

# Enter password
driver.find_element(By.NAME, "pass").send_keys(facebook_pass)
driver.find_element(By.NAME, "pass").send_keys(Keys.RETURN)

time.sleep(5)

# Navigate to a specific conversation
driver.get("https://www.facebook.com/messages/t/8234639509912306")

time.sleep(10)
# print(driver.page_source)

# with open('output5.txt', 'w', encoding='utf-8') as file:
#     file.write(driver.page_source)
    # Loop through each <script> tag and write its content to the file
    # for index, script_element in enumerate(script_elements):
    #     script_content = script_element.get_attribute('innerHTML')
    #     if "Ala Trabelsi" in script_content:
    #         file.write(f"Script {index + 1}:\n")
    #         file.write(script_content + "\n")
    #         file.write("="*80 + "\n")  # Separator for readability
            
# Wait for the button to be present
# button = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Chat members']"))
# )

# # Click the button
# driver.execute_script("arguments[0].click();", button)

# # time.sleep(776670)
# # Locate all <script> tags on the page
# script_elements = driver.find_elements(By.TAG_NAME, 'script')

# # Open a text file in write mode

try:
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Continue' and @role='button']"))
    )

    driver.execute_script("arguments[0].click();", continue_button)
except:
    pass

message_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox']"))
)

messages = ["Hello Moadh! ^_^", "This is just test number 1This is just test number This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1This is just test number 1v1", "do you understand what am saying?", "can you see this test", "alright BYE"]

# Send a message
for msg in range(len(messages)):
    message_input.send_keys(messages[msg])
    time.sleep(2)
    message_input.send_keys(Keys.RETURN)
    time.sleep(2)


# Take a screenshot as proof
driver.save_screenshot("proof.png")

print("DOOOOONE")

# data = """
# {"require":[["ScheduledServerJS","handle",null,[{"__bbox":{"require":[["RelayPrefetchedStreamCache","next",[],["adp_CometHomeContactGroupsContainerQueryRelayPreloader_66c9099ea0e1c5051471593",{"__bbox":{"complete":true,"result":{"data":{"viewer":{"actor":{"__typename":"User","should_hide_group_conversations_list":false,"id":"100006564133381"},"chat_sidebar_is_collapsed":false,"chat_visibility":true,"message_threads":{"edges":[{"node":{"thread_key":{"thread_fbid":"7682488385206629"},"is_xac":false,"updated_time":1724439105,"customization_info":null,"name":"1er Science informatique (GLSI)","image":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t1.15752-9\/451794217_1306029250362582_286597163643691254_n.jpg?stp=cp0_dst-jpg_s50x50&_nc_cat=109&ccb=1-7&_nc_sid=935a9d&_nc_ohc=3GKQOrL_hyIQ7kNvgG_ivLW&_nc_ht=scontent.ftun4-2.fna&oh=03_Q7cD1QGYu_87_F2tWL_0YueRhbw4THNYaFkS1zwuKdviwzScLQ&oe=66F083D0"},"all_participants":{"edges":[{"node":{"messaging_actor":{"__typename":"User","id":"61550692685907","name":"Wiem Ben Aguil","short_name":"Wiem","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/419318787_122149923692023089_7203596712714731951_n.jpg?stp=c0.36.1080.1080a_cp0_dst-jpg_s40x40&_nc_cat=107&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=x5tOMHP6hEoQ7kNvgFmNcZd&_nc_ht=scontent.ftun4-2.fna&oh=00_AYCQk0WOALuk6-m5Zb6shdl_XaL8d5Dj7zjeQvCkUu3MIw&oe=66CED3E3"}},"id":"61550692685907"}},{"node":{"messaging_actor":{"__typename":"User","id":"61551644654790","name":"Boughattas Meriem","short_name":"Boughattas","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/414479398_122122222232054821_7898123788186238082_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=106&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=elAlgOSNLTIQ7kNvgGrPCDk&_nc_ht=scontent.ftun4-2.fna&oh=00_AYDgbHuXEVmgWiHXVtb6boTSp7MuG5W35JxF4oNXKpl66Q&oe=66CEC53C"}},"id":"61551644654790"}},{"node":{"messaging_actor":{"__typename":"User","id":"61553160521431","name":"Ala Trabelsi","short_name":"Ala","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/454743322_122161743962105350_717774291096187027_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=105&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=5N6ssNR9QdUQ7kNvgEdaWK4&_nc_ht=scontent.ftun4-2.fna&oh=00_AYD-vYRs97lFue5y4aLmYNedR_1QQnCpkB4GD1dWuxi0KQ&oe=66CED7B9"}},"id":"61553160521431"}},{"node":{"messaging_actor":{"__typename":"User","id":"61561610163204","name":"Laroussi Eya","short_name":"Laroussi","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/456115410_122114906318387005_6350871515876423934_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=100&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=8hrWyvj95WoQ7kNvgG0r2Sc&_nc_ht=scontent.ftun4-2.fna&oh=00_AYBBpGIQbETf4-vvLM7f4_iqE1Tcc12ud7HkGazLuyy4UA&oe=66CECF68"}},"id":"61561610163204"}},{"node":{"messaging_actor":{"__typename":"User","id":"61562998899857","name":"Hamzaoui Hajer","short_name":"Hamzaoui","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/453274102_122101819940433296_6455634484679684805_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=103&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=e_or3QP4r1MQ7kNvgEAnKTx&_nc_ht=scontent.ftun4-2.fna&oh=00_AYCjmlaSFgl-FfT-o0bTgKRxkt3KJYggxkGQMIHWrr7emw&oe=66CED32F"}},"id":"61562998899857"}},{"node":{"messaging_actor":{"__typename":"User","id":"100004404408003","name":"Ameni Attia","short_name":"Ameni","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/454957605_2867127186777400_2000494389277651075_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=108&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=27pvXpszOl8Q7kNvgEafAw6&_nc_ht=scontent.ftun4-2.fna&oh=00_AYBzS45HtYq9DUgmaXiZHjn0zvBFqUwVvjwICT-IxV71kg&oe=66CEF2A0"}},"id":"100004404408003"}},{"node":{"messaging_actor":{"__typename":"User","id":"100004960327453","name":"Mohamed Aziz","short_name":"Mohamed","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/392887286_2536981173143869_7968238287155655635_n.jpg?stp=cp6_dst-jpg_s40x40&_nc_cat=107&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=67KXU5YdTPkQ7kNvgHPiACL&_nc_ht=scontent.ftun4-2.fna&oh=00_AYDjdECPGHPRJH_wlsPaMJBrXKRATM-00DGTjfLGdvf-nQ&oe=66CEE12A"}},"id":"100004960327453"}},{"node":{"messaging_actor":{"__typename":"User","id":"100006564133381","name":"Moadh Oueslati","short_name":"Moadh","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/331767387_913137469886863_8121537572493047378_n.jpg?stp=c0.353.1536.1536a_cp0_dst-jpg_s40x40&_nc_cat=111&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=JJKyeS1LneQQ7kNvgFN-u7a&_nc_ht=scontent.ftun4-2.fna&oh=00_AYBauj6pvAUaHaoJN1ZK5XNiOpVv6rxBDi9m-QDWTaNq7A&oe=66CEF217"}},"id":"100006564133381"}},{"node":{"messaging_actor":{"__typename":"User","id":"100006833883210","name":"Jecem Ben Hlima","short_name":"Jecem","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/417519551_3740119599559133_8131213827952909200_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=109&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=Ep-8TbPuiZ0Q7kNvgGAOcmz&_nc_ht=scontent.ftun4-2.fna&oh=00_AYDEGMDiuNOMNV3hykxB-5fSbNLAwvUxgG_gwMYPb_B-0Q&oe=66CEE5A0"}},"id":"100006833883210"}},{"node":{"messaging_actor":{"__typename":"User","id":"100009463530796","name":"Med Aziz Azzaz","short_name":"Med Aziz","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/454803029_3936808909977855_1861781095350193932_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=101&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=YZuzyB_HEVYQ7kNvgHEXB5B&_nc_ht=scontent.ftun4-2.fna&oh=00_AYB7b3gDm3rNnt1C2eemHFAbVEISYBHYm2mjj8FWuItQWA&oe=66CEC38C"}},"id":"100009463530796"}},{"node":{"messaging_actor":{"__typename":"User","id":"100009620240135","name":"\u0633\u064a\u0631 \u064a\u0646\u0627\u0671 \u062c\u0627\u0621\u0628\u0627\u0644\u0644\u0647","short_name":"\u0633\u064a\u0631 \u064a\u0646\u0627\u0671","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/454873153_3681357915528180_3024634165159679063_n.jpg?stp=c0.0.720.720a_cp0_dst-jpg_s40x40&_nc_cat=103&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=d9LOlVK1QigQ7kNvgGAZZpx&_nc_ht=scontent.ftun4-2.fna&oh=00_AYACTnWXEK6k_eeyEfA7GojdP7yDfOROjHh8_usjFbnfPg&oe=66CEF2F1"}},"id":"100009620240135"}},{"node":{"messaging_actor":{"__typename":"User","id":"100010002404176","name":"Med Amine Nsr","short_name":"Med","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/419567595_2158443387832387_764007531600690871_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=104&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=zWqB1HE8gSUQ7kNvgGA5mCi&_nc_ht=scontent.ftun4-2.fna&oh=00_AYAKaV3XA3qUJLjkRPlJtk7qOk18mkMrQI7v2TJcoIrGYg&oe=66CED1A4"}},"id":"100010002404176"}},{"node":{"messaging_actor":{"__typename":"User","id":"100010784971209","name":"Ml\u0103\u00fd\u0119h \u00c2\u0155\u00efj","short_name":"Ml\u0103\u00fd\u0119h","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/418986226_2075774936125319_591667600844812963_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=102&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=rmnu-kxLR5cQ7kNvgEzmfl6&_nc_ht=scontent.ftun4-2.fna&oh=00_AYAYFYIkK2q28rQ-VB6dzzqZNK0ARFnF2InqSHUwmcmTLA&oe=66CED18D"}},"id":"100010784971209"}},{"node":{"messaging_actor":{"__typename":"User","id":"100010981178635","name":"Mahdi Mhedhbi","short_name":"Mahdi","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/321829745_858207021965029_4710264260728708789_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=102&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=J8PUlJTgt94Q7kNvgEjVmRw&_nc_ht=scontent.ftun4-2.fna&oh=00_AYBGxA7w22Vk_stHVOtm6aJLU9yPeLm7xulG3opCQpOTYw&oe=66CEE96B"}},"id":"100010981178635"}},{"node":{"messaging_actor":{"__typename":"User","id":"100012470523104","name":"Helmi Kh","short_name":"Helmi","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/417357166_1802116966880637_3990218358614226392_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=104&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=yYDR-X_ebp4Q7kNvgEIhwWb&_nc_ht=scontent.ftun4-2.fna&oh=00_AYD35ZiZwqsbWnCT6GjmtTqkbQdtv724GhnwveLkdyvh2A&oe=66CEF5AA"}},"id":"100012470523104"}},{"node":{"messaging_actor":{"__typename":"User","id":"100012616566759","name":"Lina Ben Amor","short_name":"Lina","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/275110991_1413690315728174_1362050331535486938_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=108&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=vzbY-uOXOfUQ7kNvgHjk77_&_nc_ht=scontent.ftun4-2.fna&oh=00_AYCLubP7uXwXnnI0Yqt-8ZJWi14tetPlQkvZFUsDPr-d5Q&oe=66CEF344"}},"id":"100012616566759"}},{"node":{"messaging_actor":{"__typename":"User","id":"100012768757494","name":"Nassir Boumnijel","short_name":"Nassir","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/432990896_1860754757693465_2525585000191754239_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=109&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=2BsQYNKMlUUQ7kNvgHEqHRB&_nc_ht=scontent.ftun4-2.fna&oh=00_AYBKok0H0CDcG6Ppb7ie-U5R5Qv8v2U9yMlHtMWP0FerHQ&oe=66CEF503"}},"id":"100012768757494"}},{"node":{"messaging_actor":{"__typename":"User","id":"100012785536176","name":"Fatma Ouni","short_name":"Fatma","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t39.30808-1\/453997496_1983668822069283_3804396638699195730_n.jpg?stp=cp0_dst-jpg_s40x40&_nc_cat=107&ccb=1-7&_nc_sid=0ecb9b&_nc_ohc=f_C_3PvtcXoQ7kNvgEOXOx1&_nc_ht=scontent.ftun4-2.fna&oh=00_AYDlQynFuYkr_iElaWLc1Vmipvxl7f1u7wGbbf7_8_2w1g&oe=66CED968"}},"id":"100012785536176"}},{"node":{"messaging_actor":{"__typename":"User","id":"100013314373362","name":"Yassine Mekki","short_name":"Yassine","profile_picture":{"uri":"https:\/\/scontent.ftun4-2.fna.fbcdn.net\/v\/t1.30497-1\/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=110&ccb=1-7&_nc_sid=136b72&_nc_ohc=ANaUE6Y_shwQ7kNvgHO_2st&_nc_ht=scontent.ftun4-2.fna&oh=00_AYDRhmcsmxzPyYA6fW87nmyi5jo6pOhDDatMN_5fn2HDKA&oe=66F083FA"}},"id":"100013314373362"}},{"node":{"messaging_actor":{"__typename":"User","…
# """

# import re

# # Regular expression to find user IDs
# user_ids = re.findall(r'"id":"(\d+)"', data)
# users = 0
# users_list = []

# # Print all found user IDs
# for user_id in user_ids:
#     if user_id == "100006564133381":pass
#     elif user_id not in users_list:
#         users+=1
#         users_list.append(user_id)
#         print(f"https://www.facebook.com/messages/t/{user_id}")

# print(users)

# # 61553160521431 : Ala trabelsi    6 times
# # 100004404408003 : Ameni Attia 6 times

# # omar : 100043850032586      31 timess


# Yassine Khcherem\",[19,\"1\"],\"\\\/messaging\\\/lightspeed\\\/media_fallback\\\/?entity_id=100089105923497
# Houssem Dorbez\",[19,\"1\"],\"\\\/messaging\\\/lightspeed\\\/media_fallback\\\/?entity_id=100029360269964
# Rayen Ben Ameur\",[19,\"1\"],\"\\\/messaging\\\/lightspeed\\\/media_fallback\\\/?entity_id=100022366401352
# Adnene Gsouma\",[19,\"1\"],\"\\\/messaging\\\/lightspeed\\\/media_fallback\\\/?entity_id=100091505891883
# Amir Abid\",[19,\"1\"],\"\\\/messaging\\\/lightspeed\\\/media_fallback\\\/?entity_id=100078575024174


#"Rayen Ben Ameur\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"594176\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100022451439396\"],[19,\"1\"]"

#"Abdelhamid Ben Ameur\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"594176\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100029360269964\"],[19,\"1\"]"

#"Yassine Khcherem\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"594176\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"61558302647909\"],[19,\"1\"]"

#"Houssem Dorbez\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"4352\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100031297274228\"],[19,\"1\"]"

#"Ala Trabelsi\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"590081\"],[19,\"0\"],[19,\"2\"],[19,\"1\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"61561610163204\"],[19,\"1\"]"

#"Malak Mokded\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"590081\"],[19,\"0\"],[19,\"1\"],[19,\"1\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100015056700943\"],[19,\"1\"]"

#"Chaima Boukadida\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"594176\"],[19,\"0\"],[19,\"1\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100033494716735\"],[19,\"1\"]"

#"Chaima Boukadida\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"594176\"],[19,\"0\"],[19,\"1\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"61554122911247\"],[19,\"1\"]"

#"Omar Aloui\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"256\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"100089105923497\"],[19,\"1\"]"

#"Omar Aloui\",false,false,[19,\"0\"],true,false,[19,\"60\"],[19,\"41418751\"],[19,\"256\"],[19,\"0\"],[19,\"2\"],[19,\"2\"],[9]]],[1,[5,\"verifyContactRowExists\",[19,\"61553368023150\"],[19,\"1\"]"



# Found 1 elements containing the name 'Yassine Khcherem':
# Tag name: script
# Text: 
# Attributes:
#  - data-content-len: 244757
#  - data-sjs: 
#  - type: application/json
# ========================================


# x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli x1sxyh0 xurb0ha xwib8y2 x1y1aw1k xykv574 xbmpl8g x4cne27 xifccgj xbktkl8
# x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli x1sxyh0 xurb0ha xwib8y2 x1y1aw1k xykv574 xbmpl8g x4cne27 xifccgj xbktkl8



#"Omar Aloui created this group\",[19,\"1\"],[9],[9],[9],[9],false,false,false,[19,\"0\"],[9],[9],[9],[19,\"0\"],[9],[19,\"0\"],false,[9],[9],[9],[9],false,[9],[19,\"0\"],[9],[19,\"0\"],[9],[19,\"8276133572438903\"],[9],[19,\"-1\"],[19,\"1\"],[19,\"0\"],\"\",[19,\"0\"],[9],[19,\"0\"],[9],[9],[9],[9],[9],[19,\"7\"],[9],[9],[9],[19,\"100043850032586\"],[19,\"37003\"],[9],[19,\"1\"],[19,\"-1\"],[9]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100006564133381\"],[19,\"0\"],[19,\"0\"],[19,\"0\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100022366401352\"],[19,\"1724154775517\"],[19,\"1724156627495\"],[19,\"1722885251697\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100022451439396\"],[19,\"1724154807570\"],[19,\"1724154807796\"],[19,\"0\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100029360269964\"],[19,\"1724154815981\"],[19,\"1724154818268\"],[19,\"0\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100043850032586\"],[19,\"1723885195765\"],[19,\"1723885207291\"],[19,\"0\"],[9],true,\"Group creator\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,true,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100089105923497\"],[19,\"1723134374351\"],[19,\"1723134377851\"],[19,\"1722919760832\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\"100091505891883\"],[19,\"1724154775517\"],[19,\"1724155991790\"],[19,\"1723037115831\"],[9],false,\"Added by Omar Aloui\",[19,\"0\"],[19,\"80\"],[9],[19,\"0\"],false,false,[19,\"0\"]]],[1,[5,\"clearPinnedMessages\",[19,\"8276133572438903\"]]],[1,[3,1,[19,\"4449569714558976734\"]],[3,2,[19,\"5052375503848170497\"]],[3,3,[19,\"108108383034278914\"]],[3,4,[19,\"4294967316\"]],[5,\"writeThreadCapabilities\",[19,\"8276133572438903\"],[2,1],[2,2],[2,3],[2,4]]],[1,[5,\"deleteThenInsertThread\",[19,\"1724001678119\"],[19,\"1724001678119\"],\"Aziz: Lfac 68\",\"1ere sc info 2024-2025\",\"https:\\\/\\\/scontent.ftun4-2.fna.fbcdn.net\\\/v\\\/t1.15752-9\\\/452696631_1634648257378995_3112829928626123331_n.jpg?stp=dst-jpg_s100x100&_nc_cat=103&ccb=1-7&_nc_sid=b70caf&_nc_ohc=I6qG1nV0gIoQ7kNvgHMp4rL&_nc_ht=scontent.ftun4-2.fna&



100006564133381
100022366401352
100022451439396
100029360269964
100043850032586
100089105923497
100091505891883


# I think i finally fucking got it lmfao:
# the user id is always after [5,\"addParticipantIdToGroupThread\",[19,\"8276133572438903\"],[19,\" (TEsted by omar group)
                            # [5,"addParticipantIdToGroupThread",[19,"8276133572438903"],[19,"
                            # [5,\addParticipantIdToGroupThread\,[19,\8276133572438903\],[19,\
# the user id is always after [5,\"addParticipantIdToGroupThread\",[19,\"7682488385206629\"],[19,\" (tested by info group)





