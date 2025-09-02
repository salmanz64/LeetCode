class RecentCounter:

    def __init__(self):
        self.queue = []


    def ping(self, t: int) -> int:
        ranges = t -3000
        if t > ranges:
            while self.queue and self.queue[0] <ranges:
                self.queue.pop(0)
            self.queue.append(t)
        return len(self.queue)
