import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=id, name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2, email1=email, email2=email2, email3=email3, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contacts_not_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
            "select ab.id from addressbook ab LEFT JOIN address_in_groups ag on ab.id = ag.id where ab.deprecated='0000-00-00 00:00:00'and ag.group_id is NULL")
            return cursor.fetchall()
        finally:
            cursor.close()

    def get_contacts_in_group(self, group_id):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where group_id=%s",
                (int(group_id))
            )
            return cursor.fetchall()
            # row = cursor.fetchone()
            # list.append(row)
        finally:
            cursor.close()
        # return list
