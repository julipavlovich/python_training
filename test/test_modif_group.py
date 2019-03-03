from model.group import Group


def test_modify_group_to_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="", header="", footer=""))
    app.session.logout()


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="newname1", header="newheader1", footer="newfooter1"))
    app.session.logout()


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New footer"))
    app.session.logout()
