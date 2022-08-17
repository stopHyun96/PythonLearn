# [예제1] 구구단을 2단부터 9단까지 출력하되, 계산값이 홀수인 경우만 출력하기

for i in range(2,10,1) :
    
    for num in range(1,10,1) :
        gugu = num * i
        
        if gugu % 2 == 1 :
            print(i, "*", num, "=", gugu)
            

# [예제2] 매일 아침 7시에 문구가 나오는 프로그램 만들기

for i in range(0,24,1) :
    
    if i == 7 :
        print("오전 7시입니다.~!~!")
    elif 1 <= i <= 11 :
        print(f"오전 {i}시")
    elif i == 12 :
        print(f"오후 12시")
    elif 13 <= i <= 23 :
        for a in range(1,12,1) :
            print(f"오후 {a}시")
        break
    else :
        print("오전 0시")
        
# [예제3] 1부터 6까지 있는 주사위를 두번 던져서 나온 숫자 구하기

dice = 0
random = 0

for i in {'1', '2', '3', '4', '5', '6'} : 
    dice = i
    break

for i in {'1', '2', '3', '4', '5', '6'} : 
    random = i
    break

print(int(dice) + int(random))

# [예제4] 국어, 영어, 수학 점수를 입력받아 최고점과 
# 최저점을 구하고 최고점와 최저 점의 차이를 출력하는 프로그램 만들기

kor = int(input("국어 점수 입력 >> "))
eng = int(input("영어 점수 입력 >> "))
math = int(input("수학 점수 입력 >> "))

score = [kor, eng, math]

max = score[0]
min = score[0]

for i in score :
    if i > max :
        max = i
print(f"최고점은 : {max}점 입니다.")

for i in score :
    if i < min :
        min = i
print(f"최저점은 : {min}점 입니다.")

minus = max - min

print(f"최고점과 최저점의 차는 {minus}입니다.")

# [예제 5] '오늘은 몇일차 과제인가?'라는 문제를 내고 4일차(번호로 넣어도됨)라는 정답을 입력했을 경우에는 "정답!" 
# 으로 출력하고, 그외에는 "틀렸습니다"라고 출력되는 프로그램 만들기

while (True) :
    choice = int(input("오늘은 몇일 차 과제인가? >> "))
    
    if choice == 4 :
        print("정답 ! !")
        break
    else :
        print("틀렸습니다.")