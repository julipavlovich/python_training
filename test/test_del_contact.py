from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="ADDNewFirstName1", lastname="ADDNewLastName1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)

# def test_cancel_delete_first_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
#   app.contact.cancel_delete_first_contact()


# def test_delete_several_contacts(app):
