class BST :
    class Node :
        def __init__(self, element = None, left = None, right = None) :
            self.element = element
            self.left = left
            self.right = right

    def __init__(self) :
        self.root = None

# 순회
# 전휘 순회 함수
    def preshow(self) :
        def preorder(node) : #전위 순회 함수
            if node == None :
                return
            
            print(node.element, end = " ")  #먼저 루트노드 처리
            preorder(node.left)             #왼쪽 서브트리 처리
            preorder(node.right)            #오른쪽 서브트리 처리

        preorder(self.root)
        print()

# 중위 순회 함수
    def inorder(self, node) :
        if node == None :
            return
        
        self.inorder(node.left)         #왼쪽 서브트리 처리
        print(node.element, end = " ")
        self.inorder(node.right)        #오른쪽 서브트리 처리

    def inshow(self) :
        self.inorder(self.root)
        print()

# 후위 순회 함수
    def postorder(self, node) :
        if node == None :
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.element, end = " ")

    def postshow(self) :
        self.postorder(self.root)
        print()

# 추가
    def add(self, element) :
        newNode = self.Node(element)
        #1. 트리가 비어있다면 추가하고자 하는 요소가 root가 된다.
        if self.root == None :
            self.root = newNode
            return
        curr = self.root
        while curr != None :
            parent = curr
            if curr.element == element :
                return
            elif curr.element < element :
                curr = curr.right
            else :
                curr = curr.left

        if parent.element < element :
            parent.right = newNode
        else :
            parent.left = newNode

    #삭제
    def remove(self, key) :
        #1. root 노드가 없다면 삭제 실패
        if self.root == None :
            return
        # 삭제할 노드랑 부모노드 찾기            
        parent = self.root  #부모 노드를 저장할 변수 
        target = self.root  # 삭제할 노드를 담아줄 변수

        while target != None :
            if target.element == key :
                break
            else :
                parent = target
                if key > target.element :
                    target = target.right
                else :
                    target = target.left
            
        #1. while문을 다 돌고나면 target에는 삭제할 노드가, parent에는 삭제할 노드의 부모노드가 담기게 됨
        #2. 삭제하고자 하는 요소가 루트 노드라면 target와 parent에는 root 노드가 들어있게 됨
        #3. 삭제하고자 하는 요소가 tree에 없다면 target에는 None 값이 들어가게 됨.

        # 삭제할 요소를 찾지 못했다면 실패
        if target == None :
            return

        #2. 삭제할 노드의 자식이 없다면(리프 노드라면)
        if not target.left and not target.right :
            if parent == target :
                self.root = None
            elif target == parent.left :
                parent.left == None
            else :
                parent.right = None

        #3. 삭제할 노드가 두 자식을 갖고 있다면
        elif target.left and target :
            #계승할 노드 찾기
            succ_parent = target
            succ = target.left #계승할 노드
            while succ.right != None :
                succ_parent = succ
                succ = succ.right
            #while문이 끝나면 succ에는 계승할 노드가 들어있음

            target.element = succ.right
            if succ == succ_parent.right :
                succ_parent.right = succ.left
            else :
                succ_parent.left = succ.left

        #4. 삭제할 노드가 하나의 자식을 갖고 있다면
        else : 
            child = target.left or target
            if target == parent :
                self.root = child
            elif target == parent.left :
                parent.left = child
            else : 
                parent.right = child


    #탐색
    def select(self, key) :
        curr = self.root
        while curr != None :
            if key == curr.element :
                break
            elif key > curr.element :
                curr = curr.right
            else :
                curr = curr.left

        if curr == None :
            return
        return curr.element


#재귀 함수로 구현한 추가, 삭제, 검색 -----------------
    #추가
    def re_add(self, element) :
        self.root = self.re_add_value(self.root, element)

    def re_add_value(self, node, element) :
        if node == None :
            node = self.Node(element) 
        else :
            if element == node.element :
                return
            elif element > node.element :
                node.right = self.re_add_value(node.right, element)
            else :
                node.left = self.re_add_value(node.left, element)
            
        return node
    
    #삭제
    def re_remove(self, key) :
        self.root, removeNode = self.re.remove_value(self.root, key)

    def re_remove_value(self, node, key) :
        if node == None :
            return None, None
        elif key < node.element :
            node.left, removenode = self.re_remove_value(node.left, key)
        elif key > node.element :
            node.right, removenode = self.re_remove_value(node.right, key)
        else :  #내가 삭제하고자 하는 노드를 찾은 경우
                #자식이 없는 경우
            if not node.left and not node.right :
                removenode = node
                node = None
            #두 자식을 갖는 경우
            elif node.left and node.right :
                #계승할 노드 찾기
                succ = node.left
                while succ.right != None :
                    succ = succ.right

                node.element, succ.element = succ.element, node.element
                node.left, removeNode = self.re_remove_value(node.left, succ.element)
            
            #한 자식만 갖는 경우
            else :
                removeNode = node
                node = node.left or node.right

        return node, removeNode

    #탐색
    def re_select(self, key) :
        node = self.re_select_value(self.root, key) 
        if node != None :
            return node.element

    def re_select_value(self, node, key) :
        if node == None :   #검색실패
            return None
        if node.element == key :
            return node
        elif key > node.element :
            return self.re_select_value(node.right, key)
        else :
            return self.re_select_value(node.left, key)


tree = BST()
tree.add(50)
tree.add(25)
tree.add(65)
tree.add(10)
tree.add(40)
tree.add(13)
tree.inshow()
#tree.remove(13)
tree.inshow()
print("찾기결과 : ", tree.select(1000))
print("왼쪽에서 탐색 : ")
tree.root = tree.re_add_value(tree.root, 10)

tree = BST()
tree.add(11)
tree.add(5)
tree.add(4)
tree.add(7)
tree.add(15)
tree.add(13)
tree.add(18)

#전위 순회
# tree.preshow()
#중위 순회
# tree.inshow()
#후위 순회
# tree.postshow()

#삭제
tree.remove(18)
tree.inshow()

#탐색
print("찾기결과 : ", tree.select(13))