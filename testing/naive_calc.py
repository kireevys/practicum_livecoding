if __name__ == '__main__':
    print("Калькулятор. Версия 0.1\n")
    try:
        while True:
            inp = input("Введите выражение: ")
            if '+' in inp:
                a, b = map(int, inp.split('+'))
                print(f"{a}+{b}={a + b}")
            elif '-' in inp:
                a, b = map(int, inp.split('-'))
                print(f"{a}-{b}={a - b}")
            elif '*' in inp:
                a, b = map(int, inp.split('*'))
                print(f"{a}*{b}={a * b}")
            elif '/' in inp:
                a, b = map(int, inp.split('/'))
                print(f"{a}/{b}={a / b}")
            else:
                print("Непонятный ввод, сорян :(")
    except ZeroDivisionError:
        print("Некорректный ввод")
    except ValueError:
        print("Некорректный ввод")
