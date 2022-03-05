import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def csv_writer(driver):
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

    student_link = driver.find_element(By.CSS_SELECTOR, 'div.flex.flex-1.justify-center.px-5.py-8.tab.border-b.border-gray-400.cursor-pointer.border-b-0')
    student_link.click()
    time.sleep(13)
    assignment_name = str(driver.find_element(By.CSS_SELECTOR, 'h1').text)
    student_doc = assignment_name + "(student data).csv"
    file = open(student_doc, 'w')
    students = driver.find_elements(By.TAG_NAME, 'tr')
    for student in students:
        try:
            student_name = str(student.find_element(By.TAG_NAME, 'a').text)
        except NoSuchElementException:
            continue

        try:
            points = str(student.find_element(By.CLASS_NAME, 'performance_marker').text)
        except NoSuchElementException:
            continue

        question_results = ''
        questions = student.find_elements(By.TAG_NAME, 'td')
        for question in questions[3:]:
            try:
                question_html = question.get_attribute('outerHTML')
            except NoSuchElementException:
                continue
            if """<td class="incorrect">""" in question_html:
                result = '0'
            elif """<td class="correct">""" in question_html:
                result = '1'
            else:
                result = ' '

            question_results += result
            question_results += ','

        file.write(student_name + ',' + points + ',' + question_results + '\n')

    file.close()


