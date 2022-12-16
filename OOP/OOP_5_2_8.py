def get_loss(w1, w2, w3, w4):
    try:
        a = w1 // w2
    except:
        print("деление на ноль")
    else:
        return 10 * a - 5 * w2 * w3 + w4

print(get_loss(1, 0, 1, 2))
