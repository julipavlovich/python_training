# -*- coding: utf-8 -*-
# используем псевдокомментарий чтобы можно было использовать не латинские символы
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()  # сохраняем старый список групп
    app.group.create(Group(name="testgroup1", header="testgroupheader1", footer="testgroupfooter1"))
    # app.session.logout()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()  # сохраняем старый список групп
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
