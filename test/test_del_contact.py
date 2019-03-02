def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_cancel_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.cancel_delete_first_contact()
    app.session.logout()

# def test_delete_several_contacts(app):
