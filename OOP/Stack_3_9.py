class StackObj:

    def __init__(self, data: any):
        self.data = data
        self.next = None



class Stack:

    def __init__(self):
        self.__top = None
        self.__len = 0


    def push_back(self, new_obj):
        self.__len += 1
        if self.__top == None:
            self.__top = new_obj
            return 

        obj = self.__top
        while obj.next:
            obj = obj.next

        obj.next = new_obj


    def push_front(self, new_obj):
        self.__len += 1
        if self.__top:
            new_obj.next = self.__top
        self.__top = new_obj


    def get_obj_by_idx(self, idx):
        self.__is_valid_idx(idx)
        i = 0
        obj = self.__top
        while i < idx:
            i += 1
            obj = obj.next
        return obj


    def __len__(self):
        return self.__len


    def __is_valid_idx(self, idx):
        if idx > self.__len or idx < 0: 
            raise IndexError('неверный индекс')


    def __getitem__(self, idx):
        return self.get_obj_by_idx(idx).data

    
    def __setitem__(self, idx, value):
        self.get_obj_by_idx(idx).data = value


    def __iter__(self):
        obj = self.__top
        while obj:
            yield obj
            obj = obj.next




st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
print(st[1])
# print(st[0], st[1])

# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
