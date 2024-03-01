#User function Template for python3

class Solution:
     def reverseWord(self, str: str) -> str:
        k = list(str)   #By function
        k.reverse()
        return "".join(k)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends