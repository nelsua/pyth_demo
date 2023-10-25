import random


class Logic:
    def a_logic(self):
        arr = [14, 4, 5, 66, 21, 12]
        val = (arr[1] + 12)
        for a in arr:
            if a < val:
                print(a)

    def ar_py(self, arr=[]):
        for a in range(7):
            arr.append(random.randint(0, 23))
        print(arr)


def hello_world(name):
    print(f'hola {name}')
