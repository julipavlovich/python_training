# -*- coding: utf-8 -*-
# используем псевдокомментарий чтобы можно было использовать не латинские символы
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="testgroup1", header="testgroupheader1", footer="testgroupfooter1"))
    # app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
