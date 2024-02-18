import unittest
import pytest
from top_3_names import get_flat_list, get_names, sort_counted_names


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
    ('name_and_count', 'expected'), [
        ([['Денис', 3], ['Максим', 4], ['Евгений', 5], ['Ринат', 1]],
         [['Евгений', 5], ['Максим', 4], ['Денис', 3], ['Ринат', 1]]),
        ([['Адилет', 1], ['Анна', 1], ['Владимир', 2], ['Дмитрий', 1]],
         [['Владимир', 2], ['Адилет', 1], ['Анна', 1], ['Дмитрий', 1]]),
        ([['Максим', 4], ['Александр', 10], ['Денис', 3], ['Евгений', 5]],
         [['Александр', 10], ['Евгений', 5], ['Максим', 4], ['Денис', 3]])
    ]
)
def test_sort_counted_names(name_and_count, expected):
    assert sort_counted_names(name_and_count) == expected
