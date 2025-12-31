from collections import Counter
class Recovery:
    def __init__(self,log,pattern):
        self.log=log
        self.pattern=pattern
    def window_recovery(self):
        self.need=Counter(self.pattern)
        self.missing=len(self.pattern)
        self.left = 0
        self.start = 0
        self.maxLength = float("inf")
        for right, i in enumerate(self.log):
            if self.need[i] > 0:
                self.missing -= 1
            self.need[i] -= 1
            while self.missing==0:
                if right - self.left+1<self.maxLength:
                    self.maxLength=right-self.left+1
                    self.start=self.left
                self.need[self.log[self.left]] += 1
                if self.need[self.log[self.left]] > 0:
                    self.missing += 1
                self.left += 1
        if self.maxLength == float("inf"):
            return ""
        self.log[self.start:self.start + self.maxLength]

        # for right in  range(len(self.log)):
        #     while self.log[right] in self.set:
        #         self.set.remove(self.log[self.left])
        #         self.left += 1
                # print(self.set)
        #     self.set.add(self.log[right])
        # print(self.set)
        # self.maxLength = max(self.maxLength, right - self.left + 1)
        # print(self.maxLength)
r=Recovery('ADOBECODEBANC','ABC')
r.window_recovery()
