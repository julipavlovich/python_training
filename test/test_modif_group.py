from model.group import Group


def test_modify_group_to_empty(app):
    app.group.modify_first_group(Group(name="", header="", footer=""))


def test_modify_group(app):
    app.group.modify_first_group(Group(name="newname1", header="newheader1", footer="newfooter1"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(name="New footer"))
