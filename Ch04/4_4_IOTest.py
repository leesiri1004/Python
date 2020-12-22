"""
날짜 : 2020/12/22
이름 : 이슬이
내용 : 파이썬 파일입출력 함수 실습하기
"""

# 파일읽기
file1 = open('C:/Users/bigdata/test.txt', 'r')
line = file1.readline()

print('line : ', line)
file1.close()

# 여러줄 파일 읽기
file2 = open('C:/Users/bigdata/test.txt', 'r')

while True:
    line = file2.read()

    if not line:
        break

    print('line : ', line)

file2.close()

# 파일쓰기
file3 = open('C:/Users/bigdata/test3.txt', 'w')  # w -> write mode, r -> read mode
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('부탁드려요.\n')
file3.close()


# 구구단 파일출력
file4 = open('C:/Users/bigdata/test4.txt', 'w')

for a in range(2, 10):
    file4.write('%d단\n' % a)
    for b in range(1, 10):
        file4.write('%d x %d = %d\n' % (a, b, a*b))

file4.close()


# with 문(파일생성과 close 를 한번에 실행하는 구문)
with open('C:/Users/bigdata/test5.txt', 'w') as file5:
    for i in range(11):
        file5.write('★'*i)
        file5.write('\n')
