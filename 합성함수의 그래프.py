# 초기설정
from sympy import *
import sympy
x = sympy.symbols("x")

# 설명
print("(f ∘ g)(x)의 값을 구하고 그래프로 나타내는 계산기 입니다.")

# 입력
print("f(x)의 방정식을 입력해주세요.")
a, b, c = map(int, input().split())

print("g(x)의 그래프를 입력해주세요.")
e, f, g = map(int, input().split())
gx = e*x**2 + f*x + g

# 계산 및 출력
hx = a*gx**2 + b*gx + c
hx = sympy.expand(hx)
print(f"(f ∘ g)(x) = {hx}")
plot(hx)