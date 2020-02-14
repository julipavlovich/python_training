from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="ADDNewFirstName1", lastname="ADDNewLastName1"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # выбрать группу случайно
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    random_group_id = int(random_group.id)
    # выбрать контакт в группе
    if len(db.get_contacts_in_group(random_group_id)) == 0:
        ui_contacts_list = app.contact.get_contact_list()
        contact = random.choice(ui_contacts_list)
        c_id = int(contact.id)
        app.contact.add_contact_in_group(c_id, random_group_id)
    contacts_in_group = db.get_contacts_in_group(random_group_id)
    random_contact = random.choice(contacts_in_group)
    random_contact_id = int(random_contact[0])
    old_contacts_in_group = db.get_contacts_in_group(random_group_id)
    # удалить его, проверки
    app.contact.del_contact_in_group(random_contact_id, random_group_id)
    new_contacts_in_group = db.get_contacts_in_group(random_group_id)
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
