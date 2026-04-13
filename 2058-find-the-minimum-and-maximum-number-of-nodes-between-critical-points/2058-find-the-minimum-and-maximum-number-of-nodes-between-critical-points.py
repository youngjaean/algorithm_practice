class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        previous = head
        current = head.next
        nex = current.next

        array = []
        minima = float("inf")
        index = 1

        while nex:
            if (current.val > previous.val and current.val > nex.val) or (
                current.val < previous.val and current.val < nex.val
            ):
                array.append(index)

                if len(array) >= 2:
                    minima = min(minima, array[-1] - array[-2])

            index += 1
            previous = current
            current = nex
            nex = nex.next

        if len(array) < 2:
            return [-1, -1]

        return [minima, array[-1] - array[0]]