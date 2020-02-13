import re
from model.contact import Contact
from fixture.db import DbFixture


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))


def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_names_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_contacts_info_on_home_page_vs_db(app, db, check_ui):
    contact_info_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_info_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    index = 0
    while index <= int((len(contact_info_ui) - 1)):
        contact = contact_info_db[index]
        if check_ui:
            assert contact_info_ui[index].firstname == contact_info_db[index].firstname
            assert contact_info_ui[index].lastname == contact_info_db[index].lastname
            assert contact_info_ui[index].address == contact_info_db[index].address
            assert contact_info_ui[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact)
            assert contact_info_ui[index].all_emails_from_home_page == merge_emails_like_on_home_page(contact)
        index = index + 1
    print(index)
