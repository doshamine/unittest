from math import sqrt

# тренажер 5 из урока про циклы
def solve(phrases: list) -> list:
    """
    Функция для поиска фраз-палиндромов.

    Входные данные:
    phrases - список фраз

    Возвращаемое значение:
    Список, содержащий только те элементы из phrases,
    которые являются палиндромами.
    """
    result = []
    for phrase in phrases:
        stacked_phrase = "".join(phrase.split())
        if stacked_phrase == stacked_phrase[::-1]:
           result.append(phrase)
    return result


# тренажер 1 из урока про функции
def discriminant(a: float, b: float, c: float) -> float:
    """
    Функция для нахождения дискриминанта.

    Входные данные: коэффициенты a, b, c квадратного трехчлена аx^2 + bx + c.

    Возвращаемое значение:
    Дискриминант, вычисленный по формуле D = b^2 - 4ac.
    """
    D = b ** 2 - 4 * a * c
    return D


def solution(a: float, b: float, c: float):
    """
    Функция для нахождения корней квадратного уравнения.

    Входные данные: коэффициенты a, b, c квадратного трехчлена аx^2 + bx + c.

    Возвращаемое значение:
    Действительные корни квадратного уравнения аx^2 + bx + c = 0.
    Если действительных корней нет, возвращается сообщение "действительных корней нет".
    """
    D = discriminant(a, b, c)

    if D > 0:
        x1 = (0.5 * (-b + sqrt(D))) / a
        x2 = (0.5 * (-b - sqrt(D))) / a
        return x1, x2

    elif D == 0:
        x = -0.5 * b / a
        return x

    else:
        return 'действительных корней нет'


# тренажер 2 из урока про функции
def vote(votes: list):
    """
    Определение числа, которое встречается чаще всего.

    Входные данные:
    votes - список чисел

    Возвращаемое значение:
    Число, которое встретилось в списке votes наибольшее количество раз.
    """
    votes_dict = {}

    for num in votes:
        votes_dict.setdefault(num, 0)
        votes_dict[num] += 1

    sorted_items = sorted(votes_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[0][0]






