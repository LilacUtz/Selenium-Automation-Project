# importing module to use classes from it
import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class MainPageBoxTests(TestCase):
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

    def test_05_Personal_information_form(self):
        ''' insert info to form valid info'''
        print("test_Personal_information_form #5")
        self.driver.get(self.base_url + "home.html")
        first_name = self.driver.find_element(By.ID, "first-name").send_keys("Lilac")  # insert valid value to field
        last_name = self.driver.find_element(By.NAME, "last-name").send_keys("Utz")
        city_list_box = self.driver.find_element(By.ID, "city")
        select_the_city = Select(city_list_box).select_by_index(2)  # choose option from the list button by items order
        email_address = self.driver.find_element(By.ID, "email").send_keys("blabla@gmail.com")
        phone_list_box = self.driver.find_element(By.NAME, "area-code")
        select_the_phone = Select(phone_list_box).select_by_index(2)
        mobile_number = self.driver.find_element(By.ID, "mobile").send_keys("5555444")
        gander_check_box = self.driver.find_element(By.ID, "female").click()
        prefered_proffesions = self.driver.find_element(By.ID, "biology").click()
        # time.sleep(3)
        # submit_form = self.driver.find_element(By.ID, "submit-form").click() #this code is in comment so the driver will stay open without sending
        # reset_form = self.driver.find_element(By.ID, "reset-form").click() # this code will delete all form info added

    def test_06_downloading_progress(self):
        '''checking the download and finish button'''
        print("test_downloading_progress #6")
        self.driver.get(self.base_url + "home.html")
        download_button = self.driver.find_element(By.CSS_SELECTOR, '[onclick="startDownload()"]').click()  # start the download progress
        time.sleep(3)
        finish_button = self.driver.find_element(By.CSS_SELECTOR,'[onclick="confirmMessage(this)"]').click()  # ok button when download finish
        time.sleep(3)

    def test_07_text_demo(self):
        '''insert text into alart box pop up window'''
        print("test_text_demo #7")
        self.driver.get(self.base_url + "home.html")
        insert_text_button = self.driver.find_element(By.XPATH,"/html/body/section/main/button[1]").click()  # click to send text to box
        pop_up_box = self.driver.switch_to.alert
        time.sleep(2)
        pop_up_box.send_keys("THIS IS A TEST!!!!!!!!!!!")  # insert text to box
        pop_up_box.accept()
        time.sleep(3)

    def test_08_next_page_link(self):
        '''test the link to the next page'''
        print("test_next_page_link #8")
        self.driver.get(self.base_url + "home.html")
        time.sleep(2)
        next_page_link = self.driver.find_element(By.LINK_TEXT,"Next Page").click()  # click on the inner link that lead to the next page
        first_tab_title = self.driver.title
        self.assertEqual("Next Page", first_tab_title, "NOT CORRECT")
        change_name_button = self.driver.find_element(By.XPATH,"/html/body/section/main/button").click()  # tab name change from "Next Page" to "Finish"
        seconed_tab_title = self.driver.title
        self.assertEqual("Finish", seconed_tab_title, "NOT CORRECT")  # check if tab title is correct
        print("the second title is:", seconed_tab_title)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)







