import unittest
import pytest
from courses_by_duration import make_courses_list_dict, make_durations_dict


@pytest.mark.parametrize(
    ("courses", "mentors", "durations", "expected"), [
        (["Fullstack-разработчик на Python"],
         [["Анна Юшина", "Сергей Сердюк"]], [12],
         [{"title": "Fullstack-разработчик на Python", "mentors":
             ["Анна Юшина", "Сергей Сердюк"], "duration": 12}]),
        (["Frontend-разработчик с нуля"],
         [["Евгений Шек", "Валерий Хаслер", "Татьяна Тен"]], [14],
         [{"title": "Frontend-разработчик с нуля", "mentors":
             ["Евгений Шек", "Валерий Хаслер", "Татьяна Тен"],
           "duration": 14}]),
        (["Python-разработчик с нуля"], [["Роман Гордиенко"]], [20],
         [{"title": "Python-разработчик с нуля", "mentors":
             ["Роман Гордиенко"], "duration": 20}])
    ]
)
def test_courses_list_dict(courses, mentors, durations, expected):
    assert make_courses_list_dict(courses, mentors, durations) == expected


class TestDuration(unittest.TestCase):
    def test_durations_dict(self):
        item = [{"title": "Frontend-разработчик с нуля", "mentors":
                ["Кирилл Табельский", "Александр Ульянцев",
                 "Александр Бардин"], "duration": 20},
                {"title": "Java-разработчик с нуля", "mentors":
                ["Павел Дерендяев"], "duration": 14},
                {"title": "Python-разработчик с нуля", "mentors":
                ["Николай Лопин", "Михаил Ларченко"], "duration": 20}
                ]
        expected = {20: [0, 2], 14: [1]}
        self.assertEqual(make_durations_dict(item), expected)
