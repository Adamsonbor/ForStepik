
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

stich = [[word.strip('-?!,.;')for word in row.split() if word != '–'] for row in stich]

class StringText:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)
        
    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

lst_text = [StringText(row) for row in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(row.lst) for row in lst_text_sorted]
print(lst_text_sorted)
