
# import 모듈 이름 :
# 모듈이름.함수명
# import task7.mod1
# mod1.add(3, 4)

#[2] from 모듈이름 import 함수명 , 함수명
from src.day07.task7.mod1 import add
add(3,4) #함수명()

#[3] from 모듈이름 import *
from src.day07.task7.mod1 import *
sub(4,2)

#[4]
from src.day07.task7 import mod2

print(mod2.PI)

a= mod2.Math()
print(a)
print(a.solv(2))

print(mod2.add(3, 4))

from src.day07.task7.mod2 import Math,PI
print(PI)
b=Math()
print(b)

#[5]
from src.day06.Task6 import studentList
s=studentList()
print(s)