from model.group import Group


def test_modify_group_to_empty(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="", header="", footer=""))


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="newname1", header="newheader1", footer="newfooter1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
