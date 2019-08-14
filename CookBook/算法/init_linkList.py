# 初始化链表
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = Node("head")
        
    def append_list(self,head,value):
        newNode = Node(value)
        head.next = newNode
        
    def display_list(self, head=None):
        tempHead = head or self.head
        count = -1
        while tempHead.next != None:
            count += 1
            print(tempHead.value,end=" ")
            tempHead = tempHead.next
        print("\nThe count of single Link list is : {}".format(count))

    def delete_item(self,value):
        tempHead = self.head
        deleteNode = tempHead.next
        if tempHead.value == value:
            tempHead = tempHead.next
            return 
        elif deleteNode.value == value:
            tempHead.next = deleteNode.next
            return 
        else:
            while deleteNode.value != value:
                tempHead = tempHead.next
                deleteNode = tempHead.next
            tempHead.next = deleteNode.next
        

    def init_list_by_arry(self,arry=[]):
        head = self.head
        if arry:
            for item in arry:
                self.append_list(head,item)
                head = head.next
        else:
            raise IOError("Arry is null ! ")
    
    def reverse_list_by_swap(self):
        if self.head is None or self.head.next is None:
            return self.head
        head = self.head
        pre = None
        cur = head
        while cur:
            head = cur
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return head
    
    def reverse_list_recursion(self,head=None, newhead=None):
        head = head or self.head
        if head is None:
            return  
        if head.next is None:
            rhead = head 
        else:
            rhead = self.reverse_list_recursion(head=head.next,newhead=rhead)
            head.next.next = head
            head.next = None
        return rhead
        
def task():
    begin = yield
    end = yield  
    yield
    for x in range(begin,end):
        yield x



if __name__ == "__main__":
    ll = LinkList()
    ll.init_list_by_arry([1,2,3,4,5,6,7,8,9])
    ll.display_list()
    # ll.delete_item(5)
    rl = ll.reverse_list_by_swap()
    ll.display_list(rl)
    # rl = ll.reverse_list_recursion()
    # ll.display_list(rl)
    t = task()
    t.send(None)
    t.send(3)