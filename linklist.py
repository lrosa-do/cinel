class Node:
   def __init__(self, dataval=None):
      self.data = dataval
      self.next = None
      
      
head = None

def append(s):
    global head
    if head == None:
        head = Node(s)
        return 0;
    current = head
    index = 0
    while (current.next != None):
        current = current.next
        index += 1
    current.next = Node(s)
    current.next.next=None
    return index

def push(s):
    global head
    if head == None:
        head = Node(s)
        return 0;
    new_node = Node(s)
    new_node.next=head
    head = new_node
    return 0

def remove(Removekey):
    global head
    HeadVal = head
    if (HeadVal is not None):
        if (HeadVal.data == Removekey):
            head = HeadVal.next
            HeadVal = None
            return
    while (HeadVal is not None):
        if HeadVal.data == Removekey:
            break
        prev = HeadVal
        HeadVal = HeadVal.next
    if (HeadVal == None):
        return
    prev.next = HeadVal.next
    HeadVal = None
         
def clearLst():
    global head
    if (head==None):
        return
    node = head
    while (head != None):
        node = head
        head = head.next
        node = None

    
    
def printStr():
    global head
    if (head==None):
        return
    node = head
    index = 0
    while (node != None):
        print(f" [{index }]  value : {node.data}")
        node = node.next
        index +=1
      
push(25)
push(1)
push(2)
push(3)
push(10)
push("Luis")

remove(25)


printStr()


