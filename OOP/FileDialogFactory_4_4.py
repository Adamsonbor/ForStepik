CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class FileDialogFactory:
    __os = {'windows':WindowsFileDialog,
            'linux':LinuxFileDialog}

    def __new__(cls, *args, **kwargs):
        return cls.__os[CURRENT_OS](*args, **kwargs)

    @classmethod
    def create_linux_filedialog(cls, title, path, exts):
        return LinuxFileDialog(title, path, exts)

    @classmethod
    def create_windows_filedialog(cls, title, path, exts):
        return WindowsFileDialog(title, path, exts)
            
print(FileDialogFactory('title', '/', 'jpg'))
