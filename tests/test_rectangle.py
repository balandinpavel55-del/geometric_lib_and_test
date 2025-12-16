import unittest
import sys
sys.path.append('..')

from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    """Тесты для функции area() модуля rectangle"""
    
    def test_area_10_20(self):
        """Площадь прямоугольника 10×20"""
        self.assertEqual(area(10, 20), 200)
    
    def test_area_5_10(self):
        """Площадь прямоугольника 5×10"""
        self.assertEqual(area(5, 10), 50)
    
    def test_area_zero_width(self):
        """Площадь с нулевой шириной"""
        self.assertEqual(area(0, 10), 0)
    
    def test_area_zero_length(self):
        """Площадь с нулевой длиной"""
        self.assertEqual(area(10, 0), 0)
    
    def test_area_both_zero(self):
        """Площадь с нулевыми сторонами"""
        self.assertEqual(area(0, 0), 0)
    
    def test_area_square(self):
        """Площадь квадратного прямоугольника"""
        self.assertEqual(area(10, 10), 100)
    
    def test_area_float_values(self):
        """Площадь с вещественными значениями"""
        self.assertEqual(area(2.5, 4.0), 10.0)
    
    def test_area_large_values(self):
        """Площадь с большими значениями"""
        self.assertEqual(area(1000, 1000), 1000000)
    
    def test_area_small_values(self):
        """Площадь с маленькими значениями"""
        self.assertAlmostEqual(area(0.1, 0.2), 0.02, places=5)
    
    def test_area_negative_width_raises_error(self):
        """Отрицательная ширина вызывает ValueError"""
        with self.assertRaises(ValueError):
            area(-5, 10)
    
    def test_area_negative_length_raises_error(self):
        """Отрицательная длина вызывает ValueError"""
        with self.assertRaises(ValueError):
            area(5, -10)
    
    def test_area_both_negative_raises_error(self):
        """Оба отрицательных значения вызывают ValueError"""
        with self.assertRaises(ValueError):
            area(-5, -10)
    
    def test_area_negative_width_error_message(self):
        """Проверка сообщения об ошибке для ширины"""
        with self.assertRaises(ValueError) as context:
            area(-7, 10)
        self.assertIn("-7", str(context.exception))
    
    def test_area_negative_length_error_message(self):
        """Проверка сообщения об ошибке для длины"""
        with self.assertRaises(ValueError) as context:
            area(10, -8)
        self.assertIn("-8", str(context.exception))


class RectanglePerimeterTestCase(unittest.TestCase):
    """Тесты для функции perimeter() модуля rectangle"""
    
    def test_perimeter_10_20(self):
        """Периметр прямоугольника 10×20"""
        self.assertEqual(perimeter(10, 20), 60)
    
    def test_perimeter_5_10(self):
        """Периметр прямоугольника 5×10"""
        self.assertEqual(perimeter(5, 10), 30)
    
    def test_perimeter_zero_width(self):
        """Периметр с нулевой шириной"""
        self.assertEqual(perimeter(0, 10), 20)
    
    def test_perimeter_zero_length(self):
        """Периметр с нулевой длиной"""
        self.assertEqual(perimeter(10, 0), 20)
    
    def test_perimeter_both_zero(self):
        """Периметр с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_square(self):
        """Периметр квадратного прямоугольника"""
        self.assertEqual(perimeter(10, 10), 40)
    
    def test_perimeter_float_values(self):
        """Периметр с вещественными значениями"""
        self.assertEqual(perimeter(2.5, 4.0), 13.0)
    
    def test_perimeter_large_values(self):
        """Периметр с большими значениями"""
        self.assertEqual(perimeter(1000, 1000), 4000)
    
    def test_perimeter_small_values(self):
        """Периметр с маленькими значениями"""
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6, places=5)
    
    def test_perimeter_negative_width_raises_error(self):
        """Отрицательная ширина вызывает ValueError"""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
    
    def test_perimeter_negative_length_raises_error(self):
        """Отрицательная длина вызывает ValueError"""
        with self.assertRaises(ValueError):
            perimeter(5, -10)
    
    def test_perimeter_both_negative_raises_error(self):
        """Оба отрицательных значения вызывают ValueError"""
        with self.assertRaises(ValueError):
            perimeter(-5, -10)
    
    def test_perimeter_negative_width_error_message(self):
        """Проверка сообщения об ошибке для ширины"""
        with self.assertRaises(ValueError) as context:
            perimeter(-3, 10)
        self.assertIn("-3", str(context.exception))
    
    def test_perimeter_negative_length_error_message(self):
        """Проверка сообщения об ошибке для длины"""
        with self.assertRaises(ValueError) as context:
            perimeter(10, -6)
        self.assertIn("-6", str(context.exception))


if __name__ == '__main__':
    unittest.main()