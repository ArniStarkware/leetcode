import sys
class Solution:
    # #Returns a list of the values: n-1, n-4, n-9, n-16,...,n-k**2 >=0
    # def greedyListOfCandidets(self, n:int, bound: int):
    # we might want to hold a global variable.
    def numSquares(self, n: int) -> int:
        MAX_INT = sys.maxsize
        arr = [MAX_INT]*n
        for i in range(n):
            cur = i + 1
            for j in range(1,cur+1):
                if cur - j**2 == 0:
                    arr[i] = 1
                elif cur - j**2 > 0:
                    arr[i] = min( arr[i], 1+ arr[i-j**2])
                else:
                    break
        print(max(arr))
        return arr[n-1]

output = Solution().numSquares(10**5)
print('the output is')
print(output)
