# importing module to use classes from it
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class MainPageTitlesTests(TestCase):
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

    def test_01_tab_title(self):
        '''checking if the page title name is correct'''
        print("test_tab_title #1")
        self.driver.get(self.base_url + "home.html")
        tab_title = self.driver.title
        self.assertEqual("Automation Project", tab_title, "Wrong page title")

    def test_02_title_main_page(self):
        '''checking if the page header name is correct'''
        print("test_title_main_page #2")
        self.driver.get(self.base_url + "home.html")
        title_main_page = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual("Automation Project - Main Page", title_main_page.text, "NOT CORRECT")

    def test_03_h2_titles(self):
        '''checkin if the title is correct'''
        print("test_cities_of_the_world #3")
        self.driver.get(self.base_url + "home.html")
        exp_titles = ["Cities of the World", "Student Details", "Form", "A demonstration of how to access a PROGRESS element", "Text Demo", "Links"]
        act_titles = self.driver.find_elements(By.TAG_NAME, "h2") # find all elements h2 and checking if they are correct as in the list above
        for i in range(len(act_titles)):
            self.assertEqual(act_titles[i].text, exp_titles[i], "wrong title")

    def test_04_table_of_cities(self):
        '''test if the info is correct'''
        print("test_table_of_cities #4")
        self.driver.get(self.base_url + "home.html")
        cities_table_body = self.driver.find_elements(By.TAG_NAME, "table")[0].find_element(By.TAG_NAME, "tbody") #find all table in page and check the first one
        tr_elements = cities_table_body.find_elements(By.TAG_NAME, "tr")
        self.assertEqual(len(tr_elements), 3, "WRONG NUM OF ROWS") # check if the num of rows in table is the same

