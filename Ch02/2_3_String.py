"""
날짜 : 2020/12/21
이름 : 이슬이
내용 : 파이썬 문자열 연산
"""

# 문자열 더하기
str1 = 'Hello '
str2 = 'Python!'
str3 = str1 + str2
print('str3 : ', str3)

# 문자열 곱하기
result = str2 * 5
print('result : ', result)

# 문자열 길이
rs2 = len(str3)
print('rs2 : ', rs2)

# 문자열 인덱셍
sample = 'Hello World'

print('sample[0] : ', sample[0])  # 문자 배열/ 인덱스
print('sample[0] : ', sample[6])

# 문자열 슬라이싱
print('sample[0:7] : ', sample[0:7])
print('sample[1:7] : ', sample[1:7])
print('sample[:7] : ', sample[:7])
print('sample[7:] : ', sample[7:])
print('sample[-1] : ', sample[-1])
print('sample[-2] : ', sample[-2])

# 문자열 분리
people = '김유신,김춘추,장보고,강감찬,이순신'
p1, p2, p3, p4, p5 = people.split(',')

print('p1 : ', p1)
print('p2 : ', p2)
print('p3 : ', p3)
print('p4 : ', p4)
print('p5 : ', p5)

# 문자열 포맷
f_str1 = '오늘은 %d월 입니다.'  # under-bar 표기로 변수명을 쓴다
f_str2 = '오늘은 %d월 %d일 입니다.'  # 서식문자 : 값이 정해지지않은 문자 %d: decimal 숫자 / %s: string 문자열
f_str3 = '오늘은 %s요일 입니다.'
f_str4 = '오늘은 %s년 %s월 %d일 %s요일 입니다.'  # %s
f_str5 = '오늘은 %d년 %d월 %d일 %s요일 입니다.'  # %d

print(f_str1 % 12)
print(f_str2 % (12, 21))
print(f_str3 % '월')
print(f_str4 % ('2020', '12', 21, '월'))
print(f_str5 % (2020, 12, 21, '월'))
