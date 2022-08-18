# 예제1) 사용자로부터 5개의 양의 정수를 입력받아 합계를 구하는 프로그램 만들기
# 만약 0 이하의 값이 입력되면 사용자에게 "재입력하세요"라고 재요구하기

li = []
count = 5

while True :

  num = int(input("양의 정수 입력 >> "))
  count -= 1



  li.append(num)

  all = sum(li)

  if count == 0 :
    print()
    print(f"입력한 값의 총 합은 {all}입니다.")

    break

  elif num <= 0 :
    print("다시 입력하세요.")
    count += 1
  
  print()
  print(f"남은 입력 횟수 : {count}회")
  
  # 예제2) 영어사전 만들기로 했다. 딕셔너리를 이용하여 sun=해, moon=달, star=별, space=우주를 입력하여 설정하고 각 뜻을 출력하기

engBook = {"sun" : "해", "moon" : "달", "star" : "별", "space" : "우주"}

for e, k in engBook.items() :
  print(f"eng : {e}","->", f"kor : {k}")
  
  # 예제3) 500000만원짜리 물건을 할부로 구입한 뒤 매달 내는 돈을 계산해서 보여주는 프로그램 만들기
# (할부 개월은 사용자로부터 입력받도록 설정)

money = 500000

while True :
  print(f"{money}원 어치 물건을 구매하셨습니다.")
  
  month = int(input("몇개월 할부 ? >> "))

  print(f"거래해주셔서 감사합니다. 고객님께서 선택하신 할부는 {month}개월이며 매달 납부 금액은 {money // month}원입니다.")

  break

# 예제4) 1부터 100까지 중 홀수만 한칸씩 띄어쓰고 출력되도록하기

for i in range(1,101,1) :
  
  if i % 2 == 1 :
    print(i, end=" ")