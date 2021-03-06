#2중연결리스트
class Node2():
    def __init__(self):
        self.plink = None  #정방향 
        self.data = None   
        self.nlink = None  #역방향

def printNodes(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 -->", end = ' ')
    print(current.data,end = ' ') 
    while current.nlink != None:
        current =current.nlink
        print(current.data, end = " ")

    print()
    print("역방향 -->", end=" ")
    print(current.data, end=" ")
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')

memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    # printNodes(head)

# 1) 새로운 data를 삽입하는 노드 삽입 함수 insertNode(data)
def insertnode(insertdata, finddata):
    global pre, current, head, memory
    

    if finddata == head.data: #순방향기준 맨 처음 데이터자리에 추가하는 조건문
        node = Node2()
        node.data = insertdata
        node.nlink = head  #head는 노드의 시작점을 의미합니다.
        node.plink = head 
        return
        
    
    current = head 
    while current.nlink != None:  
        pre = current
        current = current.nlink
        
        if current.data == finddata:
            node = Node2()
            node.data = insertdata
           
            pre.nlink = node
            node.nlink = current
            
            current.plink = node 
            node.plink = pre
            return

    pre = current   # finddata가 리스트에 없을 경우 마지막 노드 뒤에 추가하는 코드
    node = Node2()
    current = node
    node.data = insertdata
    pre.nlink = node
    current.plink = pre
    return

insertnode("선빈", "쯔위")
printNodes(head)

# 2) data를 갖는 노드를 삭제하는 노드 삭제 함수(deleteNode(data) )
def deletNode(finddata):
    global pre, current, head, memory
    last = memory[len(memory)-1]

    if finddata == head.data:
        current = head
        head = head.nlink
        head.plink = None
        del(current)
        return
    
    current = head
    while current.nlink != None:
        pre = current
        current = current.nlink
        
        if finddata == current.data and current.data != last.data: #다음조건은 마지막 노드 외에 노드를 삭제할 때 실행
            
            pre.nlink = current.nlink
            
            pre = current
            current = current.nlink
            current.plink = pre.plink
            
            del(current)
            return
            
        
        elif last.data == current.data: #해당 조건은 리스트에서  맨마지막 값을  처리하기위한 코드
            current.plink = head #역방향에서는 맨처음 데이터를 지우는 것으로 headf를 입력
            pre.nlink = None #pre의 노드가 마지막이므로 링크를 None으로 입력
            del(current) 
            return 
    
deletNode("사나")
printNodes(head)




# 3) data 값을 갖는 노드 탐색 함수(findNode(data))

def findNode(finddata):  #findNode() 함수는 같은 리스트의 값으로 나타내는 것이므로 이전에 했던 선형 리스트와 비슷하다.
    global pre, current, head, memory
    current = head

    if finddata == current.data:
        return current

    while current.nlink != None:
        current = current.nlink

        if current.data == finddata:
            return current
    return Node2()
        
f = findNode("재남") #없는 값을 입력하면 None을 출력합니다.
print() # 이전 코드와 한꺼번에 출력시에 줄바꿈용도
print(f.data)