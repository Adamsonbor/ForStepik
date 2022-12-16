class Morph:
    def __init__(self, *args):
        self.words = list(args)


    def validate(self, word):
        return word.lower().strip(' -!?,.;')


    def add_word(self, word):
        word = self.validate(word)
        if word not in self.words:
            self.words.append(word)


    def get_words(self):
        return tuple(self.words)


    def __eq__(self, word: str):
        return self.validate(word) in self.words

    def __repr__(self):
        return ' '.join(self.words)


s = '''- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях'''

s = [i.strip().split(', ') for i in s.strip('- ').split('-')]
dict_words = [Morph(*row) for row in s]
# print(dict_words)

text = 'связь связь дн я дня Дня, sdsf, формулах, Формул'
text = text.strip('.').split()
i = 0
for word in text:
    i = i + 1 if word in dict_words else i
print(i)


