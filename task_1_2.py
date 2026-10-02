import mymodule
from mymodule import circle_area
from mymodule import circle_len as perimeter
import mymodule as mm

print(f"1) mymodule.circle_area(5) = {mymodule.circle_area(5)}")
print(f"2) circle_area(5)          = {circle_area(5)}")
print(f"3) perimeter(5)            = {perimeter(5)}")
print(f"4) mm.PI                   = {mm.PI}")

print(f"dir(mymodule) -> {dir(mymodule)}")
print(f"mymodule.__name__ = {mymodule.__name__}")
print(f"mymodule.__file__ = {mymodule.__file__}")
print(f"mm._helper() = {mm._helper()}")
