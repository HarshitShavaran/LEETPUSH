class Solution:
    def mergeKLists(self, l: list[ListNode | None]) -> ListNode | None:
        r = []
        for h in l:
            while h: r.append(h.val); h = h.next
        d = c = ListNode()
        for v in sorted(r): c.next = ListNode(v); c = c.next
        return d.next