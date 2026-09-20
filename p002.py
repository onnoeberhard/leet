def add(l1, l2):
    if l1.val == l2.val == 0: return ListNode()
    return add_(l1, l2, 0)

def add_(l1, l2, c):
    n1, v1 = (None, 0) if l1 is None else (l1.next, l1.val)
    n2, v2 = (None, 0) if l2 is None else (l2.next, l2.val)
    x = v1 + v2 + c
    if x == 0: return None
    c = x // 10
    return ListNode(x % 10, add_(n1, n2, c))

def add2(l1, l2):
    res = new = ListNode()
    c = 0
    while l1 or l2 or c > 0:
        l1, v1 = (None, 0) if l1 is None else (l1.next, l1.val)
        l2, v2 = (None, 0) if l2 is None else (l2.next, l2.val)
        x = v1 + v2 + c
        c = x // 10
        new.next = ListNode(x % 10)
        new = new.next
    return res.next

def sol_old(l1, l2):
    carry = 0
    res = ListNode()
    y = res
    while l1 or l2 or carry:
        x = carry
        carry = 0
        if l1:
            x += l1.val
            l1 = l1.next
        if l2:
            x += l2.val
            l2 = l2.next
        if x >= 10:
            carry = 1
            x -= 10
        y.val = x
        if l1 or l2 or carry:
            y.next = ListNode()
            y = y.next
    return res

