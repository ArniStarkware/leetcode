import math
class Solution:
    # #Returns a list of the values: n-1, n-4, n-9, n-16,...,n-k**2 >=0
    # def greedyListOfCandidets(self, n:int, bound: int):
    # we might want to hold a global variable.
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.ceil(math.sqrt(n))+1)]
        q, nq, d = [n], [], 1
        while q:
            for y in q:
                for x in squares:
                    if x == y:
                        return d
                    if x > y:
                        break
                    nq.append(y-x)
            d += 1
            if d == 4:
                return d
            q, nq = nq , []
        return d

output = Solution().numSquares(10**3)
print('the output is')
print(output)
