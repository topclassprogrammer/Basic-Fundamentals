import unittest
import pytest
from unique_names import get_flat_list, get_names, get_unique_sorted_names


class TestListItems(unittest.TestCase):
    def test_if_sub_list_is_list(self):
        item_1 = [["Александр Беспоясов", "Денис Ежков"], ["Вадим Ерошевичев"]]
        item_2 = ['Олег Булыгин', "Роман Гордиенко"]
        self.assertIsInstance(get_flat_list(item_1), list)
        self.assertNotIsInstance(get_flat_list(item_2), list)


@pytest.mark.parametrize(
    ('full_name', 'expected'), [
        (["Антон Глушков", "СергейИндюков", "Максим Воронцов"], None),
        (["Александр", "Антон Солонилин"], None),
        (["Анна Юшина", "Иван Бочаров", "Анатолий Корсаков"],
         ['Анна', 'Иван', 'Анатолий'])
    ]
)
def test_correct_names(full_name, expected):
    assert get_names(full_name) == expected


@pytest.mark.parametrize(
    ('names', 'expected'), [
        (["Анна", "Иван", "Олег", "Анна", "Анатолий"],
         ["Анатолий", "Анна", "Иван", "Олег"]),
        (["Ринат", "Сергей", "Ринат", "Евгений", "Ринат", "Евгений"],
         ["Евгений", "Ринат", "Сергей"]),
        (["Павел", "Денис", "Елена", "Михаил"],
         ["Денис", "Елена", "Михаил", "Павел"])
    ]
)
def test_unique_sorted_names(names, expected):
    assert get_unique_sorted_names(names) == expected
