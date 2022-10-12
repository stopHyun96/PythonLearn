#1. 스택 구현

#배열구조로 구현
#1. Stack 클래스 생성, 데이터 멤버를 선언하고 초기화,
#   스택의 유일한 데이터인 top을 리스트로 선언
#2. 모든 메소드의 첫번째 파라미터로 self를 추가
#3. 모든 메소드에서 클래스의 멤버를 사용할 때 self.를 추가하여
#   클래스 내의 변수 및 메소드임을 표시
#4. 홀수, 짝수 저장을 위한 스택 객체를 만들고
#5. 반복문을 통해(range) 0~9까지 값을 각 스택에 저장하도록 한다.

class Stack :
  def __init__(self, max = 10) :
    self.stk = [] 
    self.max = max

  def show(self) :
      print(self.stk)

  def push(self, element) :
    if self.max > len(self.stk) :
      self.stk.append(element)

  def peek(self) :
    if len(self.stk) != 0 :
      return self.stk[-1]

s1 = Stack()
s2 = Stack()

for i in range(0, 10) :
    if i % 2 == 0 :
        s2.push(i)
    else :
        s1.push(i)

print("스택 even psuh 5회 : ", end = "")
s1.show()
print("스택 odd psuh 5회 : ", end = "")
s2.show()
print("스택 even peek :", s2.peek())
print("스택 odd peek :", s1.peek())


# 2. 원형 큐(링버퍼) 구현
# 1) Circularqueue로 클래스 생성
# 2) 항목들은 리스트에 저장
# 3) 크기는 MAX_QSIZE
# 4) 공백 상태와 포화상태 검사 및 초기화 연산, 포화 상태 검사를 위해
# 나머지 연산자 사용
# 5) 현재 큐에 저장된 항목의 개수
# 6) 원형큐 출력위한 함수

MAX_QSIZE = 10
class Circularqueue :
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self) :
        return self.front == self.rear

    def isFull(self) :
        return self.front == (self.rear + 1) % MAX_QSIZE

    def clear(self) :
        self.front = self.rear

    #삽입, 삭제, peek 연산
    def enqueue(self, item) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % MAX_QSIZE #rear회전
            self.items[self.rear] = item    #rear 위치에 삽입
    
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % MAX_QSIZE   #front 회전
            return self.items[self.front]   #front 위치의 항목 반환
    
    def size(self) :
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def queueshow(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front + 1 : self.rear + 1]
        else :
            out = self.items[self.front + 1 : MAX_QSIZE] + self.items[0:self.rear + 1]
        
        print(f"[front = {self.front}, rear = {self.rear}] => {out}")

q = Circularqueue()

for i in range(7) :
    q.enqueue(i)
q.queueshow()

for i in range(3) :
    q.dequeue()
q.queueshow()

for i in range(7, 12) :
    q.enqueue(i)
q.queueshow()

#3. 이름과 핸드폰 번호를 입력하면 이름 순서대로 단순 연결 리스트를 생성하는 프로그램 만들기

class Node() :
    def __init__(self) :
        self.data = None
        self.link = None
    
def printNodes(start) :
    current = start
    if current == None :
        return

    print(current.data, end = " ")

    while current.link != None :
        current = current.link
        print(current.data, end = " ")

    print()

def makeLinkedlist(namephone) :
    global memory, head, current, pre
    printNodes(head)

    node = Node()
    node.data = namephone
    memory.append(node)
    
    if head == None :
        head = node
        return

    if head.data[0] > namephone[0] :
        node.link = head
        head = node
        return

    #중간 노드로 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        
        if current.data[0] > namephone[0] :
            pre.link = node
            node.link = current
            return

    #삽입하는 노드가 가장 큰 경우
    current.link = node

memory = []
head, current, pre = None, None, None
dataarray = [["짱구", "010-1234-1234"], ["철수", "010-8282-8282"], ["훈이", "010-7777-7777"], ["맹구", "010-5678-5678"], ["유리", "010-9876-5432"]]

for i in dataarray :
    makeLinkedlist(i)

printNodes(head)

#4. 1~45까지 숫자 6개를 뽑는 로또 추첨 프로그램 만들기

import random
lotto_num = random.randint(1, 45)
lotto = []

for i in range(6):
    while lotto_num in lotto:
        lotto_num = random.randint(1, 45)
    lotto.append(lotto_num)

class Node1():
  def __init__(self) :
    self.data = None
    self.link = None

node1 = Node1()
node1.data = lotto[0]

node2 = Node1()
node2.data = lotto[1]
node1.link = node2

node3 = Node1()
node3.data = lotto[2]
node2.link = node3

node4 = Node1()
node4.data = lotto[3]
node3.link = node4

node5 = Node1()
node5.data = lotto[4]
node4.link = node5

node6 = Node1()
node6.data = lotto[5]
node5.link = node6

current = node1
print(current.data, end = "\t")

while current.link != None :
  current = current.link
  print(current.data, end = "\t")