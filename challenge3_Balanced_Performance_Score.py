
#from collections import Counter
#from logging import currentframe


class median:
    def __init__(self,scoreA,scoreB):
        self.scoreA=scoreA
        self.scoreB=scoreB

    def is_sorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def median_calculation(self):
        if not self.is_sorted(self.scoreA):
            self.scoreA.sort()
        if not self.is_sorted(self.scoreB):
            self.scoreB.sort()
        total= len(self.scoreA)+len(self.scoreB)
        mid2=total//2
        mid1=(total-1)//2
        i=j=0
        count=0
        self.prev=self.current=0
        while count <= mid2:
            self.prev = self.current
            if i < len(self.scoreA) and (j >= len(self.scoreB) or self.scoreA[i] <= self.scoreB[j]):
                self.current = self.scoreA[i]
                i += 1

            else:
                self.current = self.scoreB[j]
                j += 1
            count += 1

        if total % 2 == 1:
            return self.current
        else:
            return (self.prev + self.current) / 2

m=median([1,2],[3,4])
print(m.median_calculation())
