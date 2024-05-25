from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Path to the ChromeDriver

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
session_path = "C:/selenium"
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--log-level=3")  # Set log level to suppress INFO and WARNING messages
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
chrome_options.add_argument(f"user-agent={mobile_user_agent}")

driver = webdriver.Chrome(options=chrome_options)

yourauth = input("Masukan Web Auth anda : ")
pharseuser = input("Masukan Pharse anda untuk login : ")
# Open the URL
URL = yourauth
wait = WebDriverWait(driver, 10)
first_button_xpath = '//*[@id="section-home"]/div/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button/span'
claim_button_xpath = '//*[@id="section-transaction"]/div[1]/div/div[3]/div/div/div/button/div/div'
value_text_xpath = '//*[@id="section-transaction"]/div[1]/div/div[3]/div/div/div/div[1]/div[2]'

def login():
    try:
        login_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-create-account relative"]/div/div[2]/button[1]')))
        login_btn.click()
        pharse_Area = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-login"]/div/div[1]/label/textarea')))
        pharse_Area.send_keys(pharseuser)
        next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-login"]/div/div[2]/button')))
        next_btn.click()
        print("Pharse benar, Berhasil login")
        input()
    except Exception as e:
        print(f"Login Success: {e}")
        return
driver.get(URL)
login()
while True:
    try:
        driver.get(URL)
        claim1 = driver.find_element(By.XPATH,first_button_xpath)
        claim1.click()
        time.sleep(1)
        waves = driver.find_element(By.XPATH, value_text_xpath)
        total_waktu = 0
        try:
            waktu_xpath = '//*[@id="section-transaction"]/div[1]/div/div[3]/div/div/div/div[2]/span'
            waktu_element = wait.until(EC.visibility_of_element_located((By.XPATH, waktu_xpath)))
            
            waktu_text = waktu_element.text

            matches = re.findall(r'(\d+)([hm])', waktu_text)

            total_waktu = sum(int(value) * (60 if unit == 'h' else 1) for value, unit in matches)
        except:
            pass
        if total_waktu > 1:
            print(f"Wave telah di claim, Menunggu {total_waktu} Menit untuk claim selanjutnya")
            time.sleep(total_waktu*60)
            print("Mencoba claim")
        else:
            claim = driver.find_element(By.XPATH, claim_button_xpath)
            claim.click()
            time.sleep(10)
    except:
        pass


