import math
import unittest
from parameterized import parameterized

from app.error import InvalidInputException
from app.main import Calculator

from math import e


class TestCalcLog(unittest.TestCase):
    """
    Класс тестирует функцию log() калькулятора
    """

    def setUp(self) -> None:
        # функция которая выполняется перед каждым тестом
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    # Параметризованный тест parameterized
    # Каждый параметр в форме кортежа
    @parameterized.expand(
        [
            ("usual_1", 4, 2, 2),
            ("usual_2", 8, 2, 3),
            ("usual_2", 2**(-5), 2, -5),
        ]
    )
    def test_usual_use_cases(self, name, a, base, expected_result) -> None:
        """
        Тест работы функции при нормальных условиях
        """
        actual_result = self.calc.log(a, base)
        self.assertAlmostEqual(expected_result, actual_result)

    @parameterized.expand(
        [
            ("error_basic", "see", 2, TypeError),
            ("error_basic", 'hello', "eeee", TypeError),
            ("error_basic", 2, "eeee", TypeError),
            ("error_basic", True, TypeError, TypeError),
            ("error_basic", Calculator(), 2, TypeError),
            ("error_basic", isinstance, 4, TypeError),
        ]
    )
    def test_TypeError(self, name, a, base, expected_result) -> None:
        """
        Тест обработки ошибки TypeError
        """
        with self.assertRaises(expected_result):
            test_result = self.calc.log(a, base)

    @parameterized.expand(
        [
            ("error_basic", 1, 1, InvalidInputException),
            ("error_basic", 1, 0, InvalidInputException),
            ("error_basic", 1, 0, InvalidInputException),
            ("error_negative", -2, 1, InvalidInputException),
            ("error_negative", 2, -23, InvalidInputException),
            ("error_negative", -1, -23, InvalidInputException),
            ("error_zero", 0, 1, InvalidInputException),
            ("error_zero", 2, 0, InvalidInputException),
            ("error_zero", 0, 0, InvalidInputException),
        ]
    )
    def test_InvalidInputException(self, name, a, base, expected_result) -> None:
        """
        Тест обработки ошибки InvalidInputException
        """
        with self.assertRaises(expected_result):
            test_result = self.calc.log(a, base)

    @parameterized.expand(
        # 1. arrange
        [
            ("basic", e, e, 1),
            ("basic", e**2, e, 2),
            ("basic", e**4, e, 4),
            ("basic", e**(-4), e, -4),
        ]
    )
    def test_log_e(self, name, a, base, expected_result) -> None:
        """
        Тест работы с числом e
        """
        # 2. act
        actual_result = self.calc.log(a, base)
        # 3. assert
        self.assertAlmostEqual(expected_result, actual_result)


if __name__ == "__main__":
    # С библиотекой parameterized запуск осуществляется только так
    unittest.main()
