def test_counter():
    y =0
    def wrapper():
        nonlocal y
        y+=1
        return y
    return wrapper

def add_x(x):
    x+=100
    return x

f = test_counter()
print(f())
print(f())
print(f())
f = test_counter()
print(f())
print(f())
print(f())