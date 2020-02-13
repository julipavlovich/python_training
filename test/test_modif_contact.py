from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewFirstName1", lastname="NewLastName1")
    change_id = old_contacts[index].id
    app.contact.modify_contact_by_id(change_id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)


# def test_modify_contact_to_empty(app):
#   if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
#    app.contact.modify_first_contact(Contact(firstname="", lastname=""))


# def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
#    app.contact.modify_first_contact(Contact(firstname="New First Name"))


# def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
#    app.contact.modify_first_contact(Contact(lastname="New Last Name"))
