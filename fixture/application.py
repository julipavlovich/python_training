from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()  # передали ссылку на драйвер
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd  # извлекли ссылку на драйвер
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd  # извлекли ссылку на драйвер
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd  # извлекли ссылку на драйвер
        self.open_groups_page()
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
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd  # извлекли ссылку на драйвер
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd  # извлекли ссылку на драйвер
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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
