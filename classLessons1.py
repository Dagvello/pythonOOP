class Digital_number():
    """Число"""

    def __init__(self, num: int, sig: int) -> int:
        """Конструктор класса"""
        self.num = num
        self.sig = sig

    def sum_digit(self) -> int:
        """Сумма цифр числа"""
        summa = 0
        for i in range(self.sig):
            summa += self.num // (10 ** i) % 10
        return summa

    def product_of_numbers(self) -> int:
        """Произведение цифр числа"""
        pr = 1
        for i in range(self.sig):
            pr *= self.num // (10 ** i) % 10
        return pr


if __name__ == '__main__':
    while True:
        numb = input()
        if numb.isdigit():
            number = int(numb)
            break
        else:
            print('Некорректный ввод. Введите число.')

    significance = len(str(number))

    my_number = Digital_number(number, significance)

    print(f'Сумма цифр = {my_number.sum_digit()}')
    print(f'Произведение цифр = {my_number.product_of_numbers()}')
