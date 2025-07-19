#--------------PROGRAM WHICH GETS NEWS NOTIFS AND SENDS THEM 2 U!!!----------------------------------

import undetected_chromedriver as uc
from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import google.generativeai as genai
import time

#-------------PROMPT TO GET NOTIFS----------------
prompt = """
Give 4 or 5 of the latest newsheadlines from: Url to news of ur choice
They should be brief, and each should begin w/ a hyphen(in other words, this -). And make sure each headline is on a different line
At the end list should end w/: Catch more news highlights from Url to news of ur choice
GIVE ME NOTHING ELSE!!!!!!!!!!!!!!!!!
"""

genai.configure(api_key="AIzaSyBFvev9GtvNMiTyXluAJ-kDNnUGdEgwwPY")
model = genai.GenerativeModel('gemini-2.0-flash')
answer = model.generate_content([prompt], stream=False)
highlights = answer.text.strip()

#----------GOES TO GMAIL AND SIGNS IN-------------------
web = uc.Chrome()
web.get("https://mail.google.com/mail/u/0/#sent")

usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('Your Gmail Address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('Your Password')
passw.send_keys(Keys.ENTER)

#----------COMPOSES EMAIL-------------------
compose= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '/html/body/div[6]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div'))
            )
compose.click()

actions = ActionChains(web)

#Recipients
time.sleep(5)
actions.send_keys("Your Gmail Address").perform()
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.TAB).perform()

#Subject
actions.send_keys("News Headlines!!!!").perform()
actions.send_keys(Keys.TAB).perform()

#Body
actions.send_keys(f"News Headlines:\n{highlights}").perform()


#Send email
time.sleep(2)
actions.send_keys(Keys.TAB).perform()
actions.send_keys(Keys.ENTER).perform()

time.sleep(7)