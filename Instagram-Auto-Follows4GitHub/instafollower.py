from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

INSTA_URL = "https://www.instagram.com/accounts/login/"
SIMILAR_ACCOUNT = "https://www.instagram.com/astro_photography_/"
USERNAME = "your_username"
PASSWORD = "your_password"


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(INSTA_URL)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, value='username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(PASSWORD)
        button = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
        button.click()
        time.sleep(6)
        not_now1 = self.driver.find_element(By.XPATH, value='//*[text()="Not now"]')
        not_now1.click()
        time.sleep(2)
        not_now2 = self.driver.find_element(By.XPATH, value='//*[text()="Not Now"]')
        not_now2.click()

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, value='//*[text()=" followers"]')
        followers.click()
        time.sleep(3)

        scr1 = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/'
                                                        'div/div/div/div/div[2]/div/div/div[3]')
        for i in range(100):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, value='//*[text()="Follow"]')
        print(follow_buttons)
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.5)
            except ElementClickInterceptedException:
                time.sleep(3)
                try:
                    cancel = self.driver.find_element(By.XPATH, value='//*[text()="Cancel"]')
                    cancel.click()
                except NoSuchElementException:
                    pass

