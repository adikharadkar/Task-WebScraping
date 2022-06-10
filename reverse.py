# s = input("Enter a string:")
# print("String type?", type(s))
# if isinstance(s, str):
#     l = []
#     for i in s:
#         l.append(i)
#     l.reverse()
#     s = "".join(l)
#     print("Reversed string: {}".format(s))
# else:
#     print("Not a string")



l = [10, 1,3,4,6,5,2,77,99,110,130,1,2,3,5]

for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

l1 = [10,2,30,4,50,6,70,8,90,0,3]
first = l1[0]
for i in range(0, len(l1)):
    if first > l1[i]:
        l1[i] = first - l1[i]
    else:
        l1[i] = l1[i] - first

# for i in range(0, len(l1)):
#     for j in range(i+1, len(l1)):
#         if l1[i] > l1[j]:
#             temp = l1[i]
#             l1[i] = l1[j]
#             l1[j] = temp
i = 0
while i < len(l1) - 1:
    if l1[i] > l1[i+1]:
        temp = l1[i]
        l1[i] = l1[i+1]
        l1[i+1] = temp
    i += 1

print(l1)

class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# l = LinkedList()

# l.head = Node(10)
# el2 = Node(1)
# el3 = Node(3)
# el4 = Node(2)
# el5 = Node(99)
# el6 = Node(93)
# l.head.next = el2
# el2.next = el3
# el3.next = el4
# el4.next = el5
# el5.next = el6

# head= l.head

# while head is not None:
#     print(head.data)
#     head = head.next
# while head is not None:
#     if head.data > head.next.data:
#         head.data, head.next.data = head.next.data, head.data
#         print(head.data)
#         print(head.next.data)
#         head.next = head.next.next
#         head = head.next


# temp = None
# while head is not None:
#     if head.data > head.next.data:
#         temp = head
#         head = head.next
#         head.next = temp
#         print(head.data)
#         print(head.next.data)
#         head.next = head.next.next
#         head = head.next

# while head is not None:
#     print(head.data)
#     head = head.next
        

