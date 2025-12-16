import unittest
import sys
sys.path.append('..')

from triangle import area, perimeter


class TriangleAreaTestCase(unittest.TestCase):
    """Тесты для функции area() модуля triangle"""
    
    def test_area_base_2_height_4(self):
        """Площадь треугольника a=2, h=4"""
        self.assertEqual(area(2, 4), 4.0)
    
    def test_area_base_5_height_6(self):
        """Площадь треугольника a=5, h=6"""
        self.assertEqual(area(5, 6), 15.0)
    
    def test_area_zero_base(self):
        """Площадь треугольника с нулевым основанием"""
        self.assertEqual(area(0, 5), 0)
    
    def test_area_zero_height(self):
        """Площадь треугольника с нулевой высотой"""
        self.assertEqual(area(5, 0), 0)
    
    def test_area_both_zero(self):
        """Площадь треугольника с нулевыми значениями"""
        self.assertEqual(area(0, 0), 0)
    
    def test_area_float_values(self):
        """Площадь треугольника с вещественными числами"""
        self.assertEqual(area(3.5, 4.0), 7.0)
    
    def test_area_large_values(self):
        """Площадь треугольника с большими значениями"""
        self.assertEqual(area(1000, 2000), 1000000)
    
    def test_area_small_values(self):
        """Площадь треугольника с маленькими значениями"""
        self.assertAlmostEqual(area(0.2, 0.5), 0.05, places=5)
    
    def test_area_negative_base_raises_error(self):
        """Отрицательное основание вызывает ValueError"""
        with self.assertRaises(ValueError):
            area(-3, 4)
    
    def test_area_negative_height_raises_error(self):
        """Отрицательная высота вызывает ValueError"""
        with 