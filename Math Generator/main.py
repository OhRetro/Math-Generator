import random
from utils import Utils

Utils.setTitle('Math Generator')

operations = [
    {"operation": "+", "method": lambda x, y: x + y},
    {"operation": "-", "method": lambda x, y: x - y},
    {"operation": "*", "method": lambda x, y: x * y},
    {"operation": "/", "method": lambda x, y: x / y},
]

while True:
    a = random.randint(1, 200)
    b = random.randint(1, 200)
    operation = random.choice(operations)
    c = operation['method'](a, b)

    print('=======================================================================')
    e = input(f'{a} {operation["operation"]} {b} = ')
    if int(e) == int(c):
        print('Right!')
    else:
        print(f"Wrong, it's {c}")
    print('Press Enter to continue.')
    print('=======================================================================')
    input()
    Utils.clearConsole()
