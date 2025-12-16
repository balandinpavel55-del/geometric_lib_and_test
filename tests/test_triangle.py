import unittest
import sys
sys.path.append('..')

from square import area, perimeter


class SquareAreaTestCase(unittest.TestCase):
    """Тесты для функции area() модуля square"""
    
    def test_area_side_5(self):
        """Площадь квадрата со стороной 5"""
        self.assertEqual(area(5), 25)
    
    def test_area_side_10(self):
        """Площадь квадрата со стороной 10"""
        self.assertEqual(area(10), 100)
    
    def test_area_side_zero(self):
        """Площадь квадрата со стороной 0"""
        self.assertEqual(area(0), 0)
    
    def test_area_float_side(self):
        """Площадь квадрата с вещественной стороной"""
        self.assertEqual(area(2.5), 6.25)
    
    def test_area_side_1(self):
        """Площадь единичного квадрата"""
        self.assertEqual(area(1), 1)
    
    def test_area_large_side(self):
        """Площадь квадрата с большой стороной"""
        self.assertEqual(area(1000), 1000000)
    
    def test_area_small_side(self):
        """Площадь квадрата с маленькой стороной"""
        self.assertAlmostEqual(area(0.1), 0.01, places=5)
    
    def test_area_negative_side_raises_error(self):
        """Отрицательная сторона вызывает ValueError"""
        with self.assertRaises(ValueError):
            area(-5)
    
    def test_area_negative_side_error_message(self):
        """Проверка сообщения об ошибке"""
        with self.assertRaises(ValueError) as context:
            area(-7)
        self.assertIn("-7", str(context.exception))


class SquarePerimeterTestCase(unittest.TestCase):
    """Тесты для функции perimeter() модуля square"""
    
    def test_perimeter_side_5(self):
        """Периметр квадрата со стороной 5"""
        self.assertEqual(perimeter(5), 20)
    
    def test_perimeter_side_10(self):
        """Периметр квадрата со стороной 10"""
        self.assertEqual(perimeter(10), 40)
    
    def test_perimeter_side_zero(self):
        """Периметр квадрата со стороной 0"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_float_side(self):
        """Периметр квадрата с вещественной стороной"""
        self.assertEqual(perimeter(2.5), 10)
    
    def test_perimeter_side_1(self):
        """Периметр единичного квадрата"""
        self.assertEqual(perimeter(1), 4)
    
    def test_perimeter_large_side(self):
        """Периметр квадрата с большой стороной"""
        self.assertEqual(perimeter(1000), 4000)
    
    def test_perimeter_small_side(self):
        """Периметр квадрата с маленькой стороной"""
        self.assertAlmostEqual(perimeter(0.1), 0.4, places=5)
    
    def test_perimeter_negative_side_raises_error(self):
        """Отрицательная сторона вызывает ValueError"""
        with self.assertRaises(ValueError):
            perimeter(-5)
    
    def test_perimeter_negative_side_error_message(self):
        """Проверка сообщения об ошибке"""
        with self.assertRaises(ValueError) as context:
            perimeter(-3)
        self.assertIn("-3", str(context.exception))


if __name__ == '__main__':
    unittest.main()