import heapq
import sys
class Person:
    def __init__(self, name, time, severity, k):
        self.name = name
        self.time = time
        self.severity = severity
        self.k = k
        self.priority = 0
    def calc(self, t):
       self.priority = self.k *(t -  self.time) + self.severity

    def __lt__(self, other):
        return self.priority > other.priority
def main():
   pq = []
   n, k = map(int, sys.stdin.readline().split())
   for i in range(n):
       query = sys.stdin.readline().split()
       if query[0] == "1":
           t, m, s = query[1:]
           pq.append(Person(m, int(t), int(s), k))
       elif query[0] == "2":
           for people in pq:
               people.calc(int(query[1]))
           heapq.heapify(pq)
           if pq:
               print(heapq.heappop(pq).name)
           else:
               print("doctor takes a break")
if __name__ == "__main__":
    main()
