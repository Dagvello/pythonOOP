from loguru import logger

logger.add('debug.json', format='{time} {level} {message}',
           level="DEBUG", rotation="1 week", compression="zip",
           serialize=True)


@logger.catch
def generate_permutations(number):
    num_str = str(number)
    visited = [False] * len(num_str)
    result = []

    def backtrack(current):
        if len(current) == len(num_str):
            result.append(int(current))
            return

        for i in range(len(num_str)):
            if not visited[i]:
                visited[i] = True
                backtrack(current + num_str[i])
                visited[i] = False

    backtrack("")

    return result


if __name__ == '__main__':
    while True:
        numb = input()
        if numb.isdigit():
            number = int(numb)
            break
        else:
            print('Некорректный ввод. Введите число с различными цифрами.')

    permutations = generate_permutations(number)

    print()

    for num in permutations:
        print(num)
