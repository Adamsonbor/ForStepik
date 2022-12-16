class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False


    def set_read(self):
        self.is_read = True


    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self):
        self.inbox_list = []


    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list.extend([MailItem(*i.split('; '), 2) for i in lst_in])

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read()
mail.inbox_list[1].set_read()
inbox_list_filtered = list(filter(bool, mail.inbox_list))



