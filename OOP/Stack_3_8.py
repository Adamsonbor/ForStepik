class StackObj:

    def __init__(self, data: str):
        self.data = data
        self.next = None



class Stack:

    def __init__(self):
        self.top = None
        self.len = 0


    def push(self, new_obj):
        if self.top:
            obj = self.get_item_by_idx(self.len - 1)
            obj.next = new_obj
        else:
            self.top = new_obj
        self.len += 1


    def pop(self):
        obj = self.get_item_by_idx(self.len - 2)
        last_obj = obj.next
        obj.next = None
        self.len -= 1
        return last_obj


    def get_item_by_idx(self, idx):
        self.__is_valid_idx(idx)
        i = 0
        obj = self.top
        while i != idx:
            i += 1
            obj = obj.next

        return obj


    def __is_valid_idx(self, idx):
        if idx >= self.len:
            raise IndexError('неверный индекс')


    def __getitem__(self, key):
        self.__is_valid_idx(key)
        return self.get_item_by_idx(key)


    def __setitem__(self, key, value):
        self.__is_valid_idx(key)
        if key == 0:
            value.next = self.top.next
            self.top = value
        elif key == 1:
            value.next = self.top.next.next
            self.top.next = value
        else:
            obj = self.get_item_by_idx(key - 2)
            value.next = obj.next.next
            obj.next = value


    def __repr__(self):
        obj = self.top
        out = []
        while obj:
            out.append(obj.data)
            obj = obj.next

        return '\n'.join(out)



    
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
print(st)
res = st[3] # исключение IndexError
