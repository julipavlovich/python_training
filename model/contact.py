from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None, email1=None, email2 = None, email3=None, address=None, all_emails_from_home_page=None,  all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3

    def __repr__(self):
        return "%s:%s:%s" % (str(self.id), self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
