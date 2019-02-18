# -*- coding: utf-8 -*-
# используем псевдокомментарий чтобы можно было использовать не латинские символы
from selenium import webdriver
import unittest
from group import Group


class test_add_group(unittest.TestCase):  # функ-я инициализации, вып-ся ДО рана теста,напр. можем запустить браузер
    def setUp(self):
        self.wd = webdriver.Firefox()  # передали ссылку на драйвер
        self.wd.implicitly_wait(30)
    
    def test_add_group(self):
        wd = self.wd  # извлекли ссылку на драйвер
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="testgroup1", header="testgroupheader1", footer="testgroupfooter1"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")
    
    def tearDown(self):  # функция зачистки
        self.wd.quit()


if __name__ == "__main__":  # если явно не указывать pytest
    unittest.main()
