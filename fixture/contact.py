from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.submit()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd  # извлекли ссылку на драйвер
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            self.app.open_home_page()

    def submit(self):
        wd = self.app.wd
        # submit new contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(5)  # поставить ожидание на элемент а не весь тест
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(5)  # поставить ожидание на элемент а не весь тест
        wd.find_element_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def cancel_delete_first_contact(self):  # доработать
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().dismiss()
        self.open_home_page()

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector(f"a[href='edit.php?id={id}']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("strong")
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                f_name = cells[2].text
                l_name = cells[1].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, lastname=l_name, firstname=f_name, address=address))
        return list(self.contact_cache)

        # for row in wd.find_elements_by_css_selector("tr[name='entry']"):
        #    cells = row.find_elements_by_css_selector('td')
        #    lastname = cells[1].text
        #    firstname = cells[2].text
            # wd.implicitly_wait(3)
            # id = cells[0].find_element_by_name("selected[]").get_attribute("value")
        #    id = cells[0].find_element_by_css_selector('input').get_attribute('value')
        #    contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        # return contacts
        # for element in wd.find_elements_by_css_selector("tr[name='entry']"):
        #    cells = element.find_elements_by_tag_name("td")
        #    id = element.find_element_by_name("selected[]").get_attribute("value")
        #    contacts.append(Contact(lastname=cells[1].text, firstname=cells[2].text, id=id))
        # return contacts

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone, address=address, email1=email1, email2=email2, email3=email3)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)
