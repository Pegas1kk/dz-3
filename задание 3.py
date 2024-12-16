def check_num(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return True
num1 = check_num(int(input('введите число')))
print(check_num(num1))