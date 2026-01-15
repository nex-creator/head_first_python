class Node:
    def __init__(self,data):
        self.data = data # contains data
        self.next = None # adress to the next address

class LinkedList:
    def __init__(self):
        self.head = None # keep track of head
    def append(self,data):
        new_node = Node(data)
        # when list is empty
        if self.head == None:
            self.head= new_node # will move to the next adress
        # when list is not empty i need to traverse to the end
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        if self.head == None:
            print("list is empty")
            return
        else:
            while current is not None:
                print(current.data, end =" -> ")
                current = current.next
            print("None")

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


li = LinkedList()
li.append(10)
li.append(90)
li.append(30)
li.append(50)
li.display()
li.prepend(20)
li.display()