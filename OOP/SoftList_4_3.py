class SoftList(list):
    def __getitem__(self, idx):
        try:
            return super().__getitem__(idx)
        except:
            return False

a = SoftList("python")
print(a[6])
