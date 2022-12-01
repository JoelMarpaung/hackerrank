import sys

class Solution:
    def __init__(self):
        self.words1 = []
        self.words2 = []
    # Write your code here
    def pushCharacter(self, char):
        self.words1.append(char)
        
    def enqueueCharacter(self, char):
        self.words2.append(char)
    
    def popCharacter(self):
        return self.words1.pop()
    
    def dequeueCharacter(self):
        return self.words1.pop(0)
        

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    