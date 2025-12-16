# Geometric Lib

Библиотека для вычисления геометрических характеристик фигур на Python.

---

##  Описание

**Geometric Lib** — это простая и удобная библиотека, позволяющая вычислять площадь и периметр основных геометрических фигур:

-  Круг (Circle)
-  Квадрат (Square)
-  Треугольник (Triangle)
-  Прямоугольник (Rectangle)

---

##  Структура проекта

```
geometric_lib/
├── README.md              # Документация проекта
├── circle.py              # Модуль для работы с кругом
├── square.py              # Модуль для работы с квадратом
├── triangle.py            # Модуль для работы с треугольником
├── rectangle.py           # Модуль для работы с прямоугольником
└── tests/                 # Директория с тестами
    ├── __init__.py
    ├── test_circle.py     # Тесты для круга
    ├── test_square.py     # Тесты для квадрата
    ├── test_triangle.py   # Тесты для треугольника
    └── test_rectangle.py  # Тесты для прямоугольника

```


##  Установка

### Клонирование репозитория

```bash
git clone https://github.com/balandinpavel55-del/geometric_lib_and_test
cd geometric_lib_and_test
```

### Требования

- Python 3.6 или выше
- Модуль `unittest` (входит в стандартную библиотеку Python)

---

##  Использование

### Импорт модулей

```python
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
```


##  Обработка ошибок

Все функции библиотеки выполняют валидацию входных данных. При передаче отрицательных значений выбрасывается исключение `ValueError`.

### Пример обработки ошибок

```python
from circle import area

try:
    result = area(-5)
except ValueError as e:
    print(f"Ошибка: {e}")
    # Ошибка: Радиус не может быть отрицательным: -5
```

### Типы исключений

| Ситуация | Исключение | Сообщение |
|----------|------------|-----------|
| Отрицательный радиус | `ValueError` | "Радиус не может быть отрицательным" |
| Отрицательная сторона | `ValueError` | "Сторона не может быть отрицательной" |
| Отрицательная высота | `ValueError` | "Высота не может быть отрицательной" |

---

##  Математические формулы

### Площадь (Area)

| Фигура | Формула | Функция |
|--------|---------|---------|
| Круг | S = πr² | `circle.area(r)` |
| Квадрат | S = a² | `square.area(a)` |
| Треугольник | S = ½ × a × h | `triangle.area(a, h)` |
| Прямоугольник | S = a × b | `rectangle.area(a, b)` |

### Периметр (Perimeter)

| Фигура | Формула | Функция |
|--------|---------|---------|
| Круг | P = 2πr | `circle.perimeter(r)` |
| Квадрат | P = 4a | `square.perimeter(a)` |
| Треугольник | P = a + b + c | `triangle.perimeter(a, b, c)` |
| Прямоугольник | P = 2(a + b) | `rectangle.perimeter(a, b)` |

---

##  API Reference

### circle.py

#### `area(r)`
Вычисляет площадь круга.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `r` | float | Радиус круга (≥ 0) |

**Возвращает:** `float` — площадь круга

**Исключения:** `ValueError` — если радиус отрицательный


#### `perimeter(r)`
Вычисляет длину окружности.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `r` | float | Радиус окружности (≥ 0) |

**Возвращает:** `float` — длина окружности

**Исключения:** `ValueError` — если радиус отрицательный

---

### square.py

#### `area(a)`
Вычисляет площадь квадрата.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Длина стороны квадрата (≥ 0) |

**Возвращает:** `float` — площадь квадрата

**Исключения:** `ValueError` — если сторона отрицательная

#### `perimeter(a)`
Вычисляет периметр квадрата.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Длина стороны квадрата (≥ 0) |

**Возвращает:** `float` — периметр квадрата

**Исключения:** `ValueError` — если сторона отрицательная

---

### triangle.py

#### `area(a, h)`
Вычисляет площадь треугольника.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Длина основания (≥ 0) |
| `h` | float | Высота треугольника (≥ 0) |

**Возвращает:** `float` — площадь треугольника

**Исключения:** `ValueError` — если основание или высота отрицательные

#### `perimeter(a, b, c)`
Вычисляет периметр треугольника.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Длина первой стороны (≥ 0) |
| `b` | float | Длина второй стороны (≥ 0) |
| `c` | float | Длина третьей стороны (≥ 0) |

**Возвращает:** `float` — периметр треугольника

**Исключения:** `ValueError` — если любая сторона отрицательная

---

### rectangle.py

#### `area(a, b)`
Вычисляет площадь прямоугольника.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Ширина прямоугольника (≥ 0) |
| `b` | float | Длина прямоугольника (≥ 0) |

**Возвращает:** `float` — площадь прямоугольника

**Исключения:** `ValueError` — если ширина или длина отрицательные

#### `perimeter(a, b)`
Вычисляет периметр прямоугольника.

| Параметр | Тип | Описание |
|----------|-----|----------|
| `a` | float | Ширина прямоугольника (≥ 0) |
| `b` | float | Длина прямоугольника (≥ 0) |

**Возвращает:** `float` — периметр прямоугольника

**Исключения:** `ValueError` — если ширина или длина отрицательные

---

##  Тестирование

### Запуск всех тестов

```bash
python -m unittest discover tests -v
```

### Запуск тестов для отдельного модуля

```bash
# Тесты для круга
python -m unittest tests.test_circle -v

# Тесты для квадрата
python -m unittest tests.test_square -v

# Тесты для треугольника
python -m unittest tests.test_triangle -v

# Тесты для прямоугольника
python -m unittest tests.test_rectangle -v
```



### Покрытие тестами

| Модуль | Позитивные тесты | Негативные тесты | Всего | Покрытие |
|--------|------------------|------------------|-------|----------|
| circle.py | 10 | 4 | 14 | 100% |
| square.py | 10 | 4 | 14 | 100% |
| triangle.py | 12 | 8 | 20 | 100% |
| rectangle.py | 14 | 10 | 24 | 100% |
| **Всего** | **46** | **26** | **72** | **100%** |

---

# Запуск тестов

##  Быстрый старт

### 1. Перейдите в папку проекта

```bash
cd geometric_lib_and_test
```

### 2. Запустите все тесты

##  Варианты запуска

### Запуск всех тестов (кратко)

```bash
python -m unittest discover tests
```

**Вывод:**
```
......................
----------------------------------------------------------------------
Ran 72 tests in 0.030s

OK
```

---

### Запуск всех тестов (подробно)

```bash
python -m unittest discover tests -v
```

**Вывод:**
```
test_area_radius_6 (test_circle.CircleAreaTestCase) ... ok
test_area_radius_3 (test_circle.CircleAreaTestCase) ... ok
test_area_negative_radius_raises_error (test_circle.CircleAreaTestCase) ... ok
...
----------------------------------------------------------------------
Ran 72 tests in 0.030s

OK
```

---

## Запуск тестов для отдельного модуля

| Модуль | Команда |
|--------|---------|
| Круг | `python -m unittest tests.test_circle -v` |
| Квадрат | `python -m unittest tests.test_square -v` |
| Треугольник | `python -m unittest tests.test_triangle -v` |
| Прямоугольник | `python -m unittest tests.test_rectangle -v` |

---

## Запуск конкретного теста

### Один тестовый класс

```bash
python -m unittest tests.test_circle.CircleAreaTestCase -v
```

### Один тестовый метод

```bash
python -m unittest tests.test_circle.CircleAreaTestCase.test_area_radius_6 -v
```

---

## Запуск из файла напрямую

```bash
cd tests
python test_circle.py
python test_square.py
python test_triangle.py
python test_rectangle.py
```



##  Возможные ошибки и решения

### Ошибка: `ModuleNotFoundError: No module named 'circle'`

**Причина:** Запуск из неправильной директории

**Решение:**

```bash
# Правильно
cd geometric_lib
python -m unittest discover tests -v

# Неправильно
cd geometric_lib/tests
python -m unittest discover . -v
```

---

### Ошибка: `No tests found`

**Причина:** Отсутствует файл `__init__.py` в папке tests

**Решение:**

| Система | Команда |
|---------|---------|
| Windows | `type  tests\__init__.py` |
| Linux/Mac | `touch tests/__init__.py` |

---


##  История изменений

### Версия 1.1.0
-  Добавлена валидация входных данных
-  Исключение `ValueError` при отрицательных значениях
-  Добавлены негативные тесты
-  Обновлена документация

### Версия 1.0.0
-  Добавлены модули circle, square, triangle, rectangle
-  Реализованы функции area() и perimeter() для всех фигур
-  Добавлены unit-тесты
-  Создана документация

---