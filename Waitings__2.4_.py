from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

'''
#step 5 of 9
driver.implicitly_wait(5)

driver.get("http://suninjuly.github.io/wait1.html")

button = driver.find_element_by_id("verify")
button.click()
message = driver.find_element_by_id("verify_message")

assert "successful" in message.text
'''

'''
#step 6 of 9
driver.get('http://suninjuly.github.io/cats.html')
driver.find_element(By.ID,'button')
'''


#step 8 of 9
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get('http://suninjuly.github.io/explicit_wait2.html')
WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
driver.find_element(By.ID, 'book').click()
driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.ID, 'input_value'))
value = driver.find_element(By.ID, 'input_value').text
driver.find_element(By.ID, 'answer').send_keys(calc(value))
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.quit()
