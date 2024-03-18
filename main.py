from functools import reduce


def process_numbers(numbers):
    numbers = list(filter(lambda x: x > 0, numbers))
    print(f'Filter: {numbers}')
    numbers = list(map(lambda x: x**2, numbers))
    print(f'Map: {numbers}')
    res = reduce(lambda x, y: int(x) + int(y), numbers)
    return res


if __name__ == '__main__':
    input_list = []
    i = 0
    while i != 5:
        try:
            input_list.append(int(input('Введите число: \n')))
            i += 1
        except ValueError:
            print('Введите число! \n')

    print(f'Input list: {input_list}')
    print(f'Result: {process_numbers(input_list)}')
