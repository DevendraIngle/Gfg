#User function Template for python3

class Solution:
     def reverseWord(self, str: str) -> str:
        k = str[::-1]   #By slicing method
        return k


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