from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="NewFirstName1", lastname="NewLastName1"))


def test_modify_contact_to_empty(app):
    app.contact.modify_first_contact(Contact(firstname="", lastname=""))


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New First Name"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="New Last Name"))
