import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

PATH = Service('C:\Program Files (x86)\chromedriver.exe')
sign_in_url = 'https://myap.collegeboard.org/login'
driver = webdriver.Chrome(service=PATH)
driver.get(sign_in_url)
time.sleep(1)
educator = driver.find_element(By.XPATH, '//*[@id="cb-atlas-identity-2"]/div[2]/div/div/div[2]/div/div/div[2]/a')
educator.click()
time.sleep(2)
username = driver.find_element(By.ID, 'username')
username.send_keys('')
password = driver.find_element(By.ID, 'password')
password.send_keys('')
button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[3]/button')
button.click()
time.sleep(5)

testing_url = "https://apclassroom.collegeboard.org/92/assessments/results/44812277/questions"
driver.get(testing_url)
time.sleep(10)

rows = driver.find_elements(By.TAG_NAME, 'tr')
assessment_csv = 'assessment.csv'
header = 'Question Number, Topic, Skill, Correct, Incorrect, Blank, Total \n'
file = open(assessment_csv, 'w')
file.write(header)

#import pdb; pdb.set_trace()

for row in rows[1:22]:

    question_number = str(row.find_element(By.CLASS_NAME, 'font-bold').text)
    topic = str(row.find_element(By.TAG_NAME, 'button ').text)
    skill = str(row.find_element(By.CLASS_NAME, 'PracticeSkillsContainer').text)
    try:
        blank = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--default').text
    except NoSuchElementException:
        blank = '0'

    try:
        incorrect = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--incorrect').text
    except NoSuchElementException:
        incorrect = '0'

    try:
        correct = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--correct').text
    except NoSuchElementException:
        correct = '0'

    #import pdb; pdb.set_trace()
    file.write(question_number + ',' + topic + ',' + skill + ',' + correct + ',' + incorrect + ',' + blank + ',' + str(int(correct) + int(incorrect) + int(blank)) + '\n')
    #import pdb; pdb.set_trace()
file.close()
