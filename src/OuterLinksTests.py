import unittest
# importing module to use classes from it
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select


class OuterLinksTests(TestCase):
    driver = None
    base_url = "file:///" + os.getcwd() + "/web/"

    @classmethod
    def setUp(cls):
        '''this method will always run first in test'''
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        '''in charge to close the driver at the end of the tests'''
        print("--> Ending tests of MainPage")
        time.sleep(3)
        cls.driver.quit()

    def test_09_google_link(self):
        '''test google links and search'''
        print("test_google_link #9")
        self.driver.get(self.base_url + "home.html")
        google_link = self.driver.find_element(By.LINK_TEXT, "Google").click()
        self.assertEqual(self.driver.current_url, "https://www.google.com/", "Wrong URL")
        google_search_field = self.driver.find_element(By.ID, "APjFqb")
        google_search_field.send_keys("JUnit")
        google_search_field.send_keys(Keys.ENTER)
        link_junit = self.driver.find_element(By.XPATH, "//*[@id=\"rso\"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
        link_junit.click()
        self.driver.find_element(By.LINK_TEXT, "User Guide").click()
        junit_title = self.driver.find_elements(By.TAG_NAME, "h1")[0] # find the first h1 header by using find elements locator
        self.assertEqual("JUnit 5 User Guide", junit_title.text, "Wrong title")
        get_started_link = self.driver.find_element(By.LINK_TEXT, "1.4. Getting Started").click()

    def test_10_merriam_webster_link(self):
        '''test the link to the web and the link inside the web'''
        print("test_merriam_webster_link #10")
        self.driver.get(self.base_url + "home.html")
        merriam_webster_link = self.driver.find_element(By.LINK_TEXT, "Merriam-Webster Dictionary").click()
        games_quizzes_link = self.driver.find_element(By.LINK_TEXT, "Games & Quizzes").click()

    def test_11_jerusalem_muni(self):
        '''test the link to the web and link inside the web'''
        print("test_jerusalem_muni #11")
        self.driver.get(self.base_url + "home.html")
        jerusalem_link = self.driver.find_element(By.LINK_TEXT, "Jerusalem Municipality").click()
        time.sleep(2)
        # jerusalem_popup = self.driver.switch_to.active_element # הכנסתי את הקוד לתגובה כי ל"ג בעומר עבר ואין יותר את החלון פופ אפ באתר
        # jerusalem_popup.find_element(By.CLASS_NAME, "close").click()
        # time.sleep(2)
        ma_kore_bair = self.driver.find_element(By.LINK_TEXT,"מה קורה בעיר").click()
        time.sleep(2)
        # jerusalem_events = self.driver.find_element(By.CSS_SELECTOR, "#digikalHeader_4 > a > img").click() #click on inner link in new page
        # scroll_down_arrow = self.driver.find_element(By.CLASS_NAME, "scrollDown").click() #scroll down the new page

