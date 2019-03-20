from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="ADDNewFirstName1", lastname="ADDNewLastName1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts[0:1] = []
    # assert old_contacts == new_contacts


# def test_cancel_delete_first_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="NewFirstName1", lastname="NewLastName1"))
#   app.contact.cancel_delete_first_contact()


# def test_delete_several_contacts(app):
