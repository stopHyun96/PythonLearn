#단순 연결 리스트
class Node():
  def __init__(self) :
    self.data = None
    self.link = None

node1 = Node()
node1.data = "짱구"
# print(node1.data)

#노드연결
node2 = Node()
node2.data = '철수'
node1.link = node2

node3 = Node()
node3.data = "훈이"
node2.link = node3

node4 = Node()
node4.data = "맹구"
node3.link = node4

print(node1.data, end = "->")
print(node1.link.data, end = "->")
print(node1.link.link.data, end = "->")
print(node1.link.link.link.data, end = "->")

# 1.첫번째 노드를 현재(current) 노드로 지정하고 현재 노드의 데이터 짱구를 출력함
# 2. 현재 노드의 링크가 비어있지 않다면 현재 노드를 현재 노드의 링크가 가리키는 노드로 변경한 후
# 현재 노드의 데이터인 철수를 출력
# 3. 현재 노드의 링크가 비어있으면 종료함

current = node1
print(current.data, end = " ")
while current.link != None :
  current = current.link
  print(current.data, end = " ")

newnode = Node()
newnode.data = "유리"
newnode.link = node2.link
node2.link = newnode

current = node1
print(current.data, end = " ")
while current.link != None :
  current = current.link
  print(current.data, end = " ")

#   노드 생성, 연결, 삭제

#노드생성
class Node():
  def __init__(self) :
    self.data = None
    self.link = None

node1 = Node()
node1.data = "짱구"
# print(node1.data)

#노드연결
node2 = Node()
node2.data = '철수'
node1.link = node2

node3 = Node()
node3.data = "훈이"
node2.link = node3

node4 = Node()
node4.data = "맹구"
node3.link = node4

#노드삭제
node2.link = node3.link
del(node3)

current = node1
print(current.data, end = " ")

while current.link != None :
  current = current.link
  print(current.data, end = " ")

