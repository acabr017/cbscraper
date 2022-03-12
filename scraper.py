from HelperFunctions import *

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

url = "https://apclassroom.collegeboard.org/92/assessments/results/44022330/questions"
driver.get(url)
time.sleep(12)

csv_writer(driver)



#import pdb; pdb.set_trace()




#driver.quit()
