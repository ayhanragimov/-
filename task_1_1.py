import sys
import math
import random

# 2. Версия, путь к интерпретатору и количество путей sys.path
print(f"Версия Python: {sys.version.split()[0]}")
print(f"Интерпретатор: {sys.executable}")
print(f"Количество путей поиска: {len(sys.path)}")

# 3. Первые 4 пути поиска
for p in sys.path[:4]:
    print(f"    {p}")

# 4. Вывод math.pi и случайного числа
print(f"math.pi = {math.pi}")
print(f"random.random() = {random.random()}")

# 5. Модули sys.modules
print(f"Всего загружено модулей: {len(sys.modules)}")
print(f"Пример: {sorted(sys.modules)[:5]}")

# 6. Публичные имена в math
public_math = [name for name in dir(math) if not name.startswith('_')]
print(f"Публичных имён в math: {len(public_math)}")
print(f"Первые 8: {public_math[:8]}")

print(f"Мой __name__ = {__name__}")
