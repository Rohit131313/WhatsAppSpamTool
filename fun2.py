from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random

def stickerspam(phone_no,folder,n):

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
        

        time.sleep(n)
        files = os.listdir(folder)
        file_paths = [os.path.join(folder, file) for file in files if os.path.isfile(os.path.join(folder, file))]
        selected_files = random.sample(file_paths, n)
        for image_path in selected_files:
            element1 = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.XPATH,'//div[@title="Attach"]'))
            )

            # ActionChains object
            actions = ActionChains(driver)

            # Perform actions
            actions.move_to_element(element1)   
            actions.click() 
            actions.perform() 

            element2 = driver.find_element(By.XPATH,'//input[@accept="image/*"]')
            element2.send_keys(image_path)


            time.sleep(3)
            element3 = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
            element3.click()
            time.sleep(5)  

        time.sleep(5)  

    except Exception as e:
        print("Exception occurred:", str(e))

    finally:
        time.sleep(10)  
        driver.quit()

