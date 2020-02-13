from model.group import Group
from random import randrange


# def test_modify_group_to_empty(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="name1", header="header1", footer="footer1"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="newname1", header="newheader1", footer="newfooter1")
    change_id = old_groups[index].id
    app.group.modify_group_by_id(change_id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="name1", header="header1", footer="footer1"))
#    old_groups = app.group.get_group_list()
#    group = Group(name="New name")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#   if app.group.count() == 0:
#      app.group.create(Group(name="name1", header="header1", footer="footer1"))
#    old_groups = app.group.get_group_list()
#    group = Group(header="New header")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_footer(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="name1", header="header1", footer="footer1"))
#    old_groups = app.group.get_group_list()
#    group = Group(footer="New footer")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
