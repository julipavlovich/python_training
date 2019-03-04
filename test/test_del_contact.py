from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
    app.contact.delete_first_contact()


def test_cancel_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
    app.contact.cancel_delete_first_contact()

# def test_delete_several_contacts(app):
