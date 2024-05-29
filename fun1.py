from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains 
import time

def messagespam(phone_no,n,message):

    chromedriver_path = r"D:\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=chromedriver_path)

    user_data_dir = r"C:\Users\ROHIT MOTWANI\AppData\Local\Google\Chrome\User Data"
    profile_directory = "Profile 1"

    # Set up Chrome options
    options = Options()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument(f"profile-directory={profile_directory}")

    driver = webdriver.Chrome(options=options,service=service)

    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH,'//*[@class="_ak1l"]/div[1]/div[1]/p[1]'))
        )
        
        # ActionChains object
        actions = ActionChains(driver)

        # Perform actions
        actions.move_to_element(element)   
        actions.click()
        for i in range(0,n):
            actions.send_keys(message)    
            actions.perform()  
        
            element1 = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH,'//*[@class="_ak1t _ak1u"]/button[1]/span[1]'))
            )
            actions.move_to_element(element1).click()  
            actions.perform()

        time.sleep(5)  
        
    except Exception as e:
        print("Exception occurred:", str(e))

        
    finally:
        time.sleep(10)  
        driver.quit()

