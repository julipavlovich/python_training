def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_cancel_delete_first_contact(app):
    app.contact.cancel_delete_first_contact()

# def test_delete_several_contacts(app):
