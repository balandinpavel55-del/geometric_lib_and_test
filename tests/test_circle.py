import unittest
import math
import sys
sys.path.append('..')

from circle import area, perimeter


class CircleAreaTestCase(unittest.TestCase):
    """Тесты для функции area() модуля circle"""
    
    def test_area_radius_6(self):
        """Площадь круга с радиусом 6"""
        res = area(6)
        expected = math.pi * 36
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_area_radius_3(self):
        """Площадь круга с радиусом 3"""
        res = area(3)
        expected = math.pi * 9
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_area_radius_zero(self):
        """Площадь круга с радиусом 0"""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_radius_1(self):
        """Площадь круга с радиусом 1"""
        res = area(1)
        self.assertAlmostEqual(res, math.pi, places=5)
    
    def test_area_float_radius(self):
        """Площадь круга с вещественным радиусом"""
        res = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_area_large_radius(self):
        """Площадь круга с большим радиусом"""
        res = area(1000)
        expected = math.pi * 1000000
        self.assertAlmostEqual(res, expected, places=2)
    
    def test_area_small_radius(self):
        """Площадь круга с маленьким радиусом"""
        res = area(0.1)
        expected = math.pi * 0.01
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_area_negative_radius_raises_error(self):
        """Отрицательный радиус вызывает ValueError"""
        with self.assertRaises(ValueError):
            area(-5)
    
    def test_area_negative_radius_error_message(self):
        """Проверка сообщения об ошибке для отрицательного радиуса"""
        with self.assertRaises(ValueError) as context:
            area(-3)
        self.assertIn("-3", str(context.exception))


class CirclePerimeterTestCase(unittest.TestCase):
    """Тесты для функции perimeter() модуля circle"""
    
    def test_perimeter_radius_6(self):
        """Длина окружности с радиусом 6"""
        res = perimeter(6)
        expected = 2 * math.pi * 6
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_radius_3(self):
        """Длина окружности с радиусом 3"""
        res = perimeter(3)
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_radius_zero(self):
        """Длина окружности с радиусом 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_radius_1(self):
        """Длина окружности с радиусом 1"""
        res = perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_float_radius(self):
        """Длина окружности с вещественным радиусом"""
        res = perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_large_radius(self):
        """Длина окружности с большим радиусом"""
        res = perimeter(1000)
        expected = 2 * math.pi * 1000
        self.assertAlmostEqual(res, expected, places=2)
    
    def test_perimeter_small_radius(self):
        """Длина окружности с маленьким радиусом"""
        res = perimeter(0.1)
        expected = 2 * math.pi * 0.1
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_negative_radius_raises_error(self):
        """Отрицательный радиус вызывает ValueError"""
        with self.assertRaises(ValueError):
            perimeter(-5)
    
    def test_perimeter_negative_radius_error_message(self):
        """Проверка сообщения об ошибке"""
        with self.assertRaises(ValueError) as context:
            perimeter(-10)
        self.assertIn("-10", str(context.exception))


if __name__ == '__main__':
    unittest.main()