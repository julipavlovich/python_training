# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(firstname="FirstName1", lastname="LastName1"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd, Contact(firstname="", lastname=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_contact(self, wd, contact):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.submit_contact(wd)

    def submit_contact(self, wd):
        # submit new contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
