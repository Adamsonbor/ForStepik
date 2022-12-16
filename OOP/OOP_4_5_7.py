from abc import ABC, abstractmethod

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """push_back method"""

    @abstractmethod
    def pop_back(self):
        """pop_back method"""


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, new_obj):
        if self._top:
            obj = self._top 
            while obj._next:
                obj = obj._next
            obj._next = new_obj
        else:
            self._top = new_obj

    def pop_back(self):
        if self._top._next:
            obj = self._top
            while obj._next._next:
                obj = obj._next
            out = obj._next
            obj._next = None
            
        else:
            out = self._top
            self._top = None

        return out


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    def __str__(self):
        return self._data



st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj)
