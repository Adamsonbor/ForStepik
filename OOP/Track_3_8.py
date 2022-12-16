class Track:
    def __init__(self, x, y, speed=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.next = None


    def add_point(self, x, y, speed):
        new_obj = Track(x, y, speed)
        obj = self
        while obj.next != None:
            obj = obj.next

        obj.next = new_obj


    def __len__(self):
        i = 0
        obj = self.next
        while obj != None:
            i += 1
            obj = obj.next
        return i 


    def __is_valid_key(self, key):
        if key < 0 or key >= len(self):
            raise IndexError('некорректный индекс')


    def __get_obj_by_id(self, key):
        i = 0
        obj = self.next
        while i != key:
            i += 1
            obj = obj.next
        return obj


    def __getitem__(self, key):
        self.__is_valid_key(key)
        obj = self.__get_obj_by_id(key)
        return (obj.x, obj.y), obj.speed


    def __setitem__(self, key, value):
        self.__is_valid_key(key)
        obj = self.__get_obj_by_id(key)
        obj.speed = value


    def __repr__(self):
        return f"{self.x}\t| {self.y}\t| {self.speed}"


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
# print(len(tr) if tr.next else 'False')
# print(tr)
# print(tr.next)
# print(tr.next.next)
# print(tr.next.next.next)
# print(len(tr))

tr[2] = 60
c, s = tr[2]
print(c, s)
c, s = tr[-2]
print(c)

# res = tr[3] # IndexError





