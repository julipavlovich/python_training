from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="ADDNewFirstName1", lastname="ADDNewLastName1"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # выбрать группу, случайно => импортировать rand
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    random_group_db_id = int(random_group.id)
    # выбрать контакт, случайно, не состоит в группе
    contacts_not_in_group = db.get_contacts_not_in_group(random_group_db_id)
    if len(contacts_not_in_group) == 0:
        app.contact.create(Contact(firstname="ADDNewFirstName1", lastname="ADDNewLastName1"))
    random_contact = random.choice(contacts_not_in_group)
    random_contact_id = int(random_contact[0])
    old_contacts_in_group = db.get_contacts_in_group(random_group_db_id)
    # добавить контакт в группу, проверки
    app.contact.add_contact_in_group(random_contact_id, random_group_db_id)
    new_contacts_in_group = db.get_contacts_in_group(random_group_db_id)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
