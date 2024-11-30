from task1 import solve, vote, solution
import pytest

def test_solve():
    phrases = ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "карман мрак", "пуст суп"]

    expected = ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"]

    result = solve(phrases)

    assert result == expected


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (-4, 28, -49, 3.5),
        (1, 1, 1, 'действительных корней нет')
    )
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected


@pytest.mark.parametrize(
    'votes, expected',
    (
        ([1, 1, 1, 2, 3], 1),
        ([1, 2, 3, 2, 2], 2)
    )
)
def test_vote(votes, expected):
    result = vote(votes)
    assert result == expected