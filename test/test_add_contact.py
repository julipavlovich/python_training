# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()  # инициализация созд-я фикстуры
    request.addfinalizer(fixture.destroy)  # указ-е на то,как разрушить
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="FirstName1", lastname="LastName1"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="", lastname=""))
    app.session.logout()
