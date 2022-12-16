s = '8 11 abcd -7.5 2.0 -5'
lst_in = s.split()
out = 0

def to_int(value):
    try:
        return int(value)
    except:
        print(value)
        return 0


print(sum(map(to_int, lst_in)))
