from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
    app.session.logout()


def test_modify_contact_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="", lastname=""))
    app.session.logout()
