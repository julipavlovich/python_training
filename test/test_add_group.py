# -*- coding: utf-8 -*-
# используем псевдокомментарий чтобы можно было использовать не латинские символы
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()  # сохраняем старый список групп
    app.group.create(group)
    # app.session.logout()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
