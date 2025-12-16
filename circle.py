import math
def area(r):
    """ 
    вычисляет площадь круга 
        параметры:
            r (float) : радиус круга 
        результат:
            float : площадь круга
        примеры:
           >>> area(6)
           113.097335529233 
           >>> area(3)
           28.274333882308
    
    """
    if r < 0:
        raise ValueError(f"Радиус не может быть отрицательным: {r}")
    return math.pi * r * r


def perimeter(r):
    """
    вычисляет периметр круга
        параметры:
            r (float) : радиус круга 
        результат:
            float : периметр круга
        примеры:
            >>> perimeter(6)
            37.699104
            >>> perimeter(3)
            18.849552
    """
    if r < 0:
        raise ValueError(f"Радиус не может быть отрицательным: {r}")
    return 2 * math.pi * r
