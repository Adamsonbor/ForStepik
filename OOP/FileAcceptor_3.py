class FileAcceptor:
    def __init__(self, *args):
        self.exts = args

    def validate(self, filename):
        return filename.strip(' -?!.,;:').split('.')[-1]

    def __call__(self, filename):
        return self.validate(filename) in self.exts

    def __add__(self, other):
        out = set(self.exts)
        if type(other) is str:
            out.add(other)

        elif type(other) is type(self):
            out.update(other.exts)

        elif type(other) is list:
            out.update(other)
        
        return FileAcceptor(*out)

    def __repr__(self):
        return ' '.join(map(str, self.exts))

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")

filenames = ["jpg", "jpeg", "png"]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)
