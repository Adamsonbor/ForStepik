class VideoRating:
    __MIN_LIMIT = 0
    __MAX_LIMIT = 5

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < self.__MIN_LIMIT or value > self.__MAX_LIMIT:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = value


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()

v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError
