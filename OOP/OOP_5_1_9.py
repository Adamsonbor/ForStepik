s = "hello 1 world -2 4.5 True"
lst_in = s.split()

def validate(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


print(list(map(validate, lst_in)))
