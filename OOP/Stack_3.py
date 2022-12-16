class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None
        
    def get_last(self):
        obj = self.top
        while obj.next:
            obj = obj.next
        return obj

    def push_many(self, lst):
        first = StackObj(lst.pop(0))
        obj = first
        while lst != []:
            obj.next = StackObj(lst.pop(0))
        return first
        
    def push_back(self, other):
        if self.top:
            self.get_last().next = other
        else:
            self.top = other

    def pop_back(self, other):
        if self.top.next.next:
            obj = self.top
            while obj.next.next:
                obj = obj.next
            obj.next = None
        elif self.top.next:
            self.top.next = None
        else:
            self.top = None

    def __len__(self):
        i = 0
        obj = self.top
        while obj.next:
            i += 1
            obj = obj.next
        return i

    def __repr__(self):
        out = []
        obj = self.top
        while obj:
            out.append(obj.data)
            obj = obj.next
        return ", ".join(out)

    def __add__(self, other):
        if self.top:
            self.get_last().next = StackObj(other.data)
        else:
            self.top = other
        return self

    def __mul__(self, other):
        if self.top:
            self.get_last().next = self.push_many(other)
        else:
            self.top = self.push_many(other)
        return self
        


obj = StackObj('55')
            
st = Stack()
st = st + obj 
st += obj

st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    print(h.data)
    assert h._StackObj__data == d[i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1
    
assert i == len(d), "неверное число объектов в стеке"
