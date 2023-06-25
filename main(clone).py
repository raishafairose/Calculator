def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def bran(opa, one, two):
    if opa == '+':
        print(f"\n{formatNumber(one)} + {formatNumber(two)} = {formatNumber(one + two)}\n")
    elif opa == '-':
        print(f"\n{formatNumber(one)} - {formatNumber(two)} = {formatNumber(one - two)}\n")
    elif opa == '*':
        print(f"\n{formatNumber(one)} * {formatNumber(two)} = {formatNumber(one - two)}\n")
    elif opa == '/':
        try:
            print(f"\n{formatNumber(one)} / {formatNumber(two)} = {formatNumber(one / two)}\n")
        except ZeroDivisionError:
            print("\nerror!!!\n")
    else:
        print("\ninvalid!!!\n")


def ui():
    print("\nWelcome\n")
    while True:
        chose_opa = input("\nchose an operation\n(+)addition\n(-)subtraction\n(*)multiplication\n(/)division\n=>")
        input_one = float(input("\nenter number one: "))
        input_two = float(input("\nenter number two: "))
        bran(chose_opa, input_one, input_two)


if __name__ == "__main__":
    ui()
