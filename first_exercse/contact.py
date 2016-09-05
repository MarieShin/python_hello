"""
contact class
"""

class Contact(object):
    # name = ''
    # email = ''
    # age = 0
    # addr = ''


    def __init__(self, name, email, age, addr):
        self.name = name
        self.email = email
        self.age = age
        self.addr = addr


    def to_string(self):
        return self.name + " " + self.email + " " + self.age + " " + self.addr




contact = Contact('shin', 'shin@gg.com', '25', 'incheon')


# print(contact.addr)
print(contact.to_string())