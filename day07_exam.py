# [예제1] 학생 수와 학생별 파이썬, 자바, C언어 점수를 입력받고, 학생별 평균 점수를 구하는 프로그램
# (점수는 0 ~ 100 사이의 양의 정수만 가능 하며, 평균 점수는 소수점 셋째 자리에서 반올림하여 계산)


stu = int(input("학생 수 입력 >> "))
stuNum = 1
stuNum2 = 0

stuLi = []
stuScoreLi = []

    
while True :
    
    for i in range(stu) :
        stuName = input(f"학생{stuNum} 이름 입력 >> ")
        stuNum += 1
        stuLi.append(stuName)
            
    print(stuLi)

    for i in range(stu) :
 
        pythonScore = int(input(f"{stuLi[stuNum2]} 파이썬 점수 입력 >> "))
        javaScore = int(input(f"학생{stuLi[stuNum2]} 자바 점수 입력 >> "))
        cScore = int(input(f"학생{stuLi[stuNum2]} C언어 점수 입력 >> "))
        stuNum2 += 1

        if 0 <= pythonScore and javaScore and cScore <=100 : 
            sum = int(pythonScore + javaScore + cScore)
            avg = float(sum // 3)
            avgScore = round(avg, 3)
            stuScoreLi.append(avgScore)
        else :
            print("잘못 된 점수 입니다. 다시 입력하세요.")
            print()
            
    break

for stuGrade in zip(stuLi, stuScoreLi) :
    print(stuGrade)

# [예제2] 오늘 저녁 메뉴를 고민중이다. 저녁 메뉴 추천기 프로그램
# (문자열 정렬 메소드 이용해 아래와 같은 결과가 출력되도록하기
# 조금씩 달라지는 부분은 무시해도됨, 각 10칸 기준으로 작성)

# [결과]
# 갈비탕		 12000원
# 소불고기		  9000원
# 김치찌개		  7000원
# 된장찌개		  7000원
# 떡볶이		  4000원

# print("{}:^0d}".format("갈비탕"))
# print("{:<10d}".format(123))
print("갈비탕{:>10s}".format("12000원"))
print("소불고기{:>10s}".format("9000원"))
print("김치찌개{:>10s}".format("7000원"))
print("된장찌개{:>10s}".format("7000원"))
print("떡볶이{:>10s}".format("4000원"))

# 1. string = 'abc14536qaaawer2po4ai5aua6' 에서 a를 대문자 A로 변경하기

string = "abc14536qaaawer2po4ai5aua6"

print(string.replace("a", "A"))

# 2. 리스트 숫자를 역방향으로 출력하기
# num = [1, 2, 3, 4, 5]

num = [1, 2, 3, 4, 5]

print(sorted(num, reverse = True))

# 3. 회사 이름이 ','로 구분되어 하나의 문자열로 저장되어있을때 리스트로 분리저장하여 출력하기
# a = "카카오, NAVER, 삼성전자, LG전자"

a = "카카오, NAVER, 삼성전자, LG전자"

print(a.split(','))

# 4. 1부터 99까지의 정수 중 짝수만 저장된 튜플로 출력하기

for i in range(1, 100, 1) :
  if i % 2 == 0 :
    print(i, end = " ")

# 5. icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000} 일때 key값으로만 구성된 리스트 출력하기

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(list(icecream))

# 6. 두개의 튜플을 하나의 딕셔너리로 변환하여 출력하기
# a = ("apple", " peach", "banana", "melon")
# b = (3000, 4000, 1500, 5000)

a = ("apple", " peach", "banana", "melon")
b = (3000, 4000, 1500, 5000)

di = zip(a, b)
print(dict(di))

# 7. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하기
# (011이면 SKT, 016이면 KT, 019이면 LGU, 010이면 알수없음)

phoneNum = str(input("번호 입력 >> "))

if phoneNum[0:3] == "011" :
  print("SKT")
elif phoneNum[0:3] == "016" :
  print("KT")
elif phoneNum[0:3] == "019" :
  print("LG")
else :
  print("알 수 없음")
  
# 8. 리스트에서 세글자 이상의 문자를 화면에 출력하기
# ["I", "study", "python", "language", "!", "I", "can", "do", "it!"]

li = ["I", "study", "python", "language", "!", "I", "can", "do", "it!"]

for i in li :
  if len(i) >= 3 :
    print(i)
    
# 9. 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]

# [결과]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호

apart = [ [101, 102], [201, 202], [301, 302] ]

apart.reverse()

for i in apart :
  for a in i :
    print(f"{a} 호")