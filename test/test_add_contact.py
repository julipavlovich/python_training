# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="FirstName1", lastname="LastName1"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname=""))
