from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewFirstName1", lastname="NewLastName1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


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
