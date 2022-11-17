#Input: s = "is2 sentence4 This1 a3"
#Output: "This is a sentence"
#Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

#Constraints:

#2 <= s.length <= 200
#s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
#The number of words in s is between 1 and 9.
#The words in s are separated by a single space.
#s contains no leading or trailing spaces.


def sortSentence(s):
    x = s.split()
    a = len(s)
    check = [""] * a    
    for i in x:
        y = int(i[-1])
        check[y-1] = i[:-1]
    return " ".join (check)
s = "is2 sentence4 This1 a3"
print(sortSentence(s))
        
* second solutions
    
        
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([x[:-1] for x in sorted(s.split(), key=lambda y: y[-1])])
