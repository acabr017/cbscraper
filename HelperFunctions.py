
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def cb_cvs_writer(driver):
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    #import pdb; pdb.set_trace()
    assignment_name = driver.find_element(By.CSS_SELECTOR, 'h1.text-center').text
    assessment_csv = str(assignment_name) + '.csv'
    header = 'Question Number, Topic, Skill, Correct, Partial, Incorrect, Blank, Total \n'
    file = open(assessment_csv, 'w')
    file.write(header)
    for row in rows:
        try:
            question_number = str(row.find_element(By.CLASS_NAME, 'font-bold').text)
        except NoSuchElementException:
            continue
        topics = row.find_elements(By.TAG_NAME, 'button ')
        topic = ""
        for t in topics:
            topic += str(t.text)
            topic += " "

        skills = row.find_elements(By.CLASS_NAME, 'PracticeSkillsContainer')
        skill = ""
        for s in skills:
            skill += str(s.text).replace("\n", " ")
            skill += " "
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

        try:
            partial = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--partial').text
        except NoSuchElementException:
            partial = '0'

        file.write(
            question_number + ',' + topic + ',' + skill + ',' + correct + ',' + partial + ',' + incorrect + ',' + blank + ',' + str(
                int(correct) + int(incorrect) + int(blank) + int(partial)) + '\n')
    file.close()
