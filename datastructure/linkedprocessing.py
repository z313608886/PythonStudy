#链表操作代码

#遍历
probe = head
while probe.next != None:
	<use or modify probe.data>
	probe = probe.next
	
#搜索目标项
probe = head
while probe.next != None and targetItem != probe.data :
	probe.next = probe

if probe.next != None:
	<targetItem has been found>
else:
	<targetItem is not in the linked datastructure>
	
#搜索第i项
probe = head
n = i
while probe.next != None and n > 0:
	probe = probe.next
	n -= 1
if probe.next != None:
	return probe.data
else:
	return False #检索超过链表长度

#替换目标项
probe = head
while probe.next != None and targetItem != probe.data :
	probe.next = probe

if probe.next != None:
	probe.data = newItem
else:
	return False
	
#在开始处插入
head = Node(newItem,head)

#在末尾处插入
newNode = Node(newItem)
if head is None:
	head = newNode
else:
	probe = head
	while probe.next != None:
		probe = probe.next
	probe.next = newNode

#从开始删除
removeditem = head.data
head = head.next
return removedItem

#从末尾删除
removeditem = head.data
if head.next is None:
	head = None
else:
	probe = head
	while probe.next.next != None:
		probe = probe.next
	removeditem = probe.next.data
	probe.next = None
return removeditem

#在任何位置插入
if head is None or index <= 0:
	head = Node(newItem,head)
else:
probe = head
while index > 1 and probe.next != None:
	probe = probe.next
	index -= 1
probe.next = Node(newItem,probe.next)

#从任意位置删除
if index < 1 or head.next is None:
	removeddata = head.data
	head = head.next
	return removeddata
else:
	probe = head
	while index > 1 and probe.next.next != None:
		probe = probe.next
		index -= 1
	removeddata = probe.next.data
	probe.next = probe.next.next
	return removeddata
