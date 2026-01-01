'''Use **two-pointer traversal** approach:

- Start with one pointer at the beginning of each array
- Move the pointer with the smaller current value
- Keep a count of how many elements have been seen
- Stop when you reach the median position

You do **not** need to store the merged array.
You may simulate merging using indices, but must not create a merged array.
Input:  scoresA = [1, 2], scoresB = [3, 4]
Output: 2.5
'''
from collections import Counter
class median:
    def __init__(self,scoreA,scoreB):
        self.scoreA=scoreA
        self.scoreB=scoreB
    def is_sorted(self,arr):
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return False
            return True
    def median_calculation(self):
        if self.scoreA is not self.is_sorted():
            self.scoreA.sort()
        if self.scoreB is not self.is_sorted():
            self.scoreB.sort()
        self.left1=0 #at self.scoreA[0]
        self.left2=0 #at self.scoreB[0]
        for i in range(len(self.scoreA)):
            # if len(self.scoreA)//2:
            #     self.mid1=
            while self.scoreA[i] is not None:
                self.left1+=1
                return self.left1
            if self.left1 % 2 != 0:
                self.mid1 = self.scoreA[(i+1)/2]
            else:
                self.mid1 = self.scoreA[(i+2)/2]

        for i in range(len(self.scoreB)):
            while self.scoreB[i] is not None:
                self.left2+=1
                return self.left2
            if self.left2 % 2 != 0:
                self.mid2 = self.scoreB[(i+1)/2]
            else:
                self.mid2 = self.scoreB[(i+2)/2]
        if (int(self.left1) + int(self.left2))%2 != 0:
            self.mid=float(self.mid2-self.mid1)
        return self.mid
        # self.count=Counter()
m=median([1,2],[3,4])
m.is_sorted()
print(m.median_calculation())
