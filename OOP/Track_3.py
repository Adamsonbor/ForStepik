class Track:
    def __init__(self, x=0, y=0):
        self.head = TrackLine(x, y)

    def get_last(self):
        obj = self.head
        while obj.next:
            obj = obj.next
        return obj
        
    def add_track(self, obj):
        if self.head.next == None:
            self.head.next = obj
        else:
            self.get_last().next = obj

    def get_tracks(self):
        out = []
        obj = self.head
        while obj:
            out.append(obj)
            obj = obj.next
        return set(out)

    def __len__(self):
        if self.head.next == None:
            return 0
        s = 0
        obj = self.head
        obj2 = obj.next
        while obj2:
            s += ((obj2.x - obj.x)**2 + (obj2.y - obj.y)**2)**0.5
            obj = obj2
            obj2 = obj2.next

        return int(s)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

        
        
class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.x = to_x
        self.y = to_y
        self.max_speed = max_speed
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq, len(track1), len(track2))
