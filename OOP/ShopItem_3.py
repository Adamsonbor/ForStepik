class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower().strip(' -.,?!;:'), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return str(self.name)

s = '''Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000'''

s = [i for i in s.split('\n')]
print(s)
d = {}

for i in s:
    name, body = i.split(':')
    weight = body.split()[0]
    price = body.split()[-1]
    obj = ShopItem(name, weight, price)
    count = d[obj][1] + 1 if obj in d else 1
    d[obj] = [obj, count]

print(d)


# s1 = ShopItem('name', 100, 100)
# s2 = ShopItem('name', 100, 100)
# print(s1 == s2)

