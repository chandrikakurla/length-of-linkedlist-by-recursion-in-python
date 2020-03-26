class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while True:
            if lastnode.next is None:
                break
            lastnode=lastnode.next
        lastnode.next=newnode
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
            print("elements in the linkedlist are:")
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #finding length of linkedlist using recursion
    def len_recurlist(self,currentnode):
        if currentnode is None:
            return 0
        return 1+self.len_recurlist(currentnode.next)
    #helper code
    def len_llist(self):
        return self.len_recurlist(self.head)
    
if __name__=='__main__':
    llist=LinkedList()
    firstnode=Node(1)
    secondtnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    llist.insert(firstnode)
    llist.insert(secondtnode)
    llist.insert(thirdnode)
    llist.insert(fourthnode)
    llist.printllist()
    len=llist.len_llist()
    print("length of linkedlist is")
    length=llist.len_llist()
    print(length)




        

