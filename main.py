def euclid(number_1,number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 -= number_2
        if number_1 < number_2:
            number_2 -= number_1
    return number_1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'enter the first number')
    num1 = int(input())
    print(f'enter the second number')
    num2 = int(input())
    print(f'НОД - {euclid(num1,num2)}')