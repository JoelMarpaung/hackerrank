class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        
	# Add your code here
    def computeDifference(self):
        for x in range(0, len(self.__elements) - 1):
            for y in range(x+1, len(self.__elements)):
                self.maximumDifference = max(self.maximumDifference, abs(self.__elements[x] - self.__elements[y]))
                
        
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)