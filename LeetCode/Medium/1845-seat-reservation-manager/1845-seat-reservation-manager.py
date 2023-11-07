from heapq import heappush, heappop, heapify


class SeatManager:
    def __init__(self, n: int):
        self.candidate = list(range(1, n + 1))
        heapify(self.candidate)

    def reserve(self) -> int:
        value = heappop(self.candidate)
        return value

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.candidate, seatNumber)