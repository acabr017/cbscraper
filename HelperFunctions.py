import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import csv


def csv_writer(driver):
    #This portion will write out the total class csv file
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    #import pdb; pdb.set_trace()
    assignment_name = driver.find_element(By.CSS_SELECTOR, 'h1.text-center').text
    assessment_csv = str(assignment_name) + '.csv'
    header = ['Question Number', 'Topic', 'Skill', 'Blank', 'Incorrect', 'Correct', 'Partial']
    csvfile = open(assessment_csv, 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    c.writerow(header)
    questionNumberDict = {}

    for row in rows:
        rowElements = []
        try:
            question_number = str(row.find_element(By.CLASS_NAME, 'font-bold').text)

        except NoSuchElementException:
            continue
        rowElements.append(question_number)
        try:
            question_text = str(row.find_element(By.CSS_SELECTOR, 'span.font-normal.ml-8.self-center.hover\:underline').text)
        except NoSuchElementException:
            continue

        questionNumberDict[question_text] = question_number


        topics = row.find_elements(By.TAG_NAME, 'button ')
        topic = ""
        for t in topics:
            topic += str(t.text)
            topic += " "
        rowElements.append(topic)

        skills = row.find_elements(By.CLASS_NAME, 'PracticeSkillsContainer')
        skill = ""
        for s in skills:
            skill += str(s.text).replace("\n", " ")
            skill += " "
        rowElements.append(skill)

        try:
            blank = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--default').text
        except NoSuchElementException:
            blank = '0'
        rowElements.append(blank)
        try:
            incorrect = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--incorrect').text
        except NoSuchElementException:
            incorrect = '0'
        rowElements.append(incorrect)

        try:
            correct = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--correct').text
        except NoSuchElementException:
            correct = '0'
        rowElements.append(correct)
        try:
            partial = row.find_element(By.CSS_SELECTOR, 'div.cursor-pointer.stack.--partial').text
        except NoSuchElementException:
            partial = '0'
        rowElements.append(partial)

        c.writerow(rowElements)
    csvfile.close()


    #This portion will write out the individual student csv file
    student_link = driver.find_element(By.CSS_SELECTOR, 'div.flex.flex-1.justify-center.px-5.py-8.tab.border-b.border-gray-400.cursor-pointer.border-b-0')
    student_link.click()
    time.sleep(10)
    assignment_name = str(driver.find_element(By.CSS_SELECTOR, 'h1').text)
    student_doc = assignment_name + "(student data).csv"
    csvfile = open(student_doc, 'w', newline='', encoding='utf-8')
    c = csv.writer(csvfile)
    qheaders = driver.find_elements(By.CLASS_NAME, 'question_header')
    student_header = ['Name', 'Total Points']

    for index in range(len(questionNumberDict)):
        key = str(qheaders[index].text)
        student_header.append(questionNumberDict[key])

    c.writerow(student_header)

    students = driver.find_elements(By.TAG_NAME, 'tr')
    for student in students:
        student_data = []
        try:
            student_name = str(student.find_element(By.TAG_NAME, 'a').text)
        except NoSuchElementException:
            continue
        student_data.append(student_name)
        try:
            points = str(student.find_element(By.CLASS_NAME, 'performance_marker').text)
        except NoSuchElementException:
            continue
        student_data.append(points)

        questions = student.find_elements(By.TAG_NAME, 'td')
        for question in questions[3:]:
            try:
                question_html = question.get_attribute('outerHTML')
            except NoSuchElementException:
                continue
            #import pdb; pdb.set_trace()
            if question.text.isdigit():
                continue
            if """<td class="incorrect">""" in question_html:
                result = '0'
            elif """<td class="correct">""" in question_html:
                result = '1'
            else:
                result = ' '

            student_data.append(result)

        c.writerow(student_data)

    csvfile.close()


