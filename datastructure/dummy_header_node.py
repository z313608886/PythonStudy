#哑头节点

#空白链表
head = Node(None,None)
head.next = head

#在第i个位置插入
probe = head
while index > 0 and probe.next != head:
	probe = probe.next
	index -= 1
probe.next = Node(newItem,probe.next)
