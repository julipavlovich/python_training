# -*- coding: utf-8 -*-
# используем псевдокомментарий чтобы можно было использовать не латинские символы
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # инициализация созд-я фикстуры
    request.addfinalizer(fixture.destroy)  # указ-е на то,как разрушить
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="testgroup1", header="testgroupheader1", footer="testgroupfooter1"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
