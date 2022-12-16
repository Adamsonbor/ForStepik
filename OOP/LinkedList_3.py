class Prop:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, var):
        setattr(instance, self.name, var)
        
class ObjList:
    data = Prop()
    prev = Prop()
    next = Prop()
    
    def __init__(self, data, _prev=None, _next=None):
        self.data = data
        self.prev = _prev
        self.next = _next

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def __len__(self):
        i = 0
        obj = self.head
        while obj != None:
            i += 1
            obj = obj.next

        return i

    def get_obj(self, indx):
        i = 0
        obj = self.head
        while i < indx:
            obj = obj.next
            i += 1
        
        return obj


    def remove_obj(self, indx):
        if indx == 0:
            self.head = self.head.next

        elif indx == len(self) - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            obj = self.get_obj(indx)
            obj.prev.next = obj.next
            obj.next.prev = obj.prev

    def __str__(self):
        obj = self.head
        out = []
        while obj != None:
            out.append(obj.data)
            obj = obj.next

        return ' '.join(out)

    def __call__(self, indx):
        return self.get_obj(indx).data

        

a = LinkedList()
a.add_obj(ObjList("data"))
a.add_obj(ObjList("hello"))
a.add_obj(ObjList("world"))
a.remove_obj(0)
a.remove_obj(1)
print(len(a))
print(a)
print(a.get_obj(0).__dict__)


