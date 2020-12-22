"""
날짜 : 2020/12/22
이름 : 이슬이
내용 : 파이썬 함수 고급 실습하기
"""


# 기본값 매개변수
def hello(name='홍길동', old=20):  # 매개변수에서 초기화
    print('----------------------')
    print('이름은 %s 입니다.' % name)
    print('나이는 %d 입니다.' % old)


hello()
hello('김춘추')
hello('김유신', 25)


# 가변 매개변수
def total(*param):
    tot = 0
    for k in param:
        tot += k

    return tot


r1 = total(1)
r2 = total(1, 2, 3)
r3 = total(1, 2, 3, 4, 5)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)


# 여러개의 값을 반환하는 함수
def sum_and_mul(x, y):
    z1 = x + y
    z2 = x * y

    return z1, z2


rs1, rs2 = sum_and_mul(1, 2)
rs3, rs4 = sum_and_mul(2, 3)

print('rs1 : ', rs1)
print('rs2 : ', rs2)
print('rs3 : ', rs3)
print('rs4 : ', rs4)

# 함수의 지역변수, 전역변수
var1 = 1


def scope_test():
    # 전역변수 var1을 참조하기 위한 global 선언
    global var1
    var1 += 2
    print('var1 : ', var1)


scope_test()


# 함수를 변수에 저장해서 호출하기
def message(param):
    print('param : ', param)


val1 = message
val2 = message

val1('김유신')
val2('김춘추')


def plus(x, y):
    return x+y


def minus(x, y):
    return x-y


list1 = [plus, minus]
r1 = list1[0](1, 2)
r2 = list1[1](1, 2)

print('r1 : ', r1)
print('r2 : ', r2)
