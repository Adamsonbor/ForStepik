class A:
    pass

class B:
    pass

class C(A):
    pass

print(issubclass(C, A))
print(issubclass(B, object))
print(issubclass(C, object))
print(isinstance(C, object))

