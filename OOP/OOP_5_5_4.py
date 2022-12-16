class PrimaryKey:
    def __enter__(self):
        print("enter!")

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(exc_type)
        return exc_type


with PrimaryKey() as pk:
    raise ValueError
