from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()  # передали ссылку на драйвер
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd  # извлекли ссылку на драйвер
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):  # разрушаем фикстуру
        self.wd.quit()

    def add_contact(self, contact):
        wd = self.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.submit_contact()

    def submit_contact(self):
        wd = self.wd
        # submit new contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
