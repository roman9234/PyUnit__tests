import unittest
from parameterized import parameterized


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        # функция которая выполняется перед каждым тестом
        ...


    def tearDown(self) -> None:
        ...

    # Параметризованный тест parameterized
    # Каждый параметр в форме кортежа
    @parameterized.expand(
        # 1. arrange
        [
            ("integers",1,2,3),
            ("negative",-5,2,-3),
            ("floats",1.2,2.3,3.5),
        ]
    )
    def test_sum(self, name, a, b, expected_result) -> None:
        # 2. act
        actual_result = a+b

        # 3. assert
        self.assertEqual(actual_result, expected_result)

    def test_invalid_values(self):
        # 2. act
        a,b = 2, "hello"
        actual_result = TypeError

        # 3. assert
        # Проверка что будет выведена ошибка
        with self.assertRaises(actual_result):
            a+b


if __name__ == "__main__":
    # С библиотекой parameterized хапуск осуществляется только так
    unittest.main()



