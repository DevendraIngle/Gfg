#User function Template for python3

class Solution:
	def find_median(self, v):
        # Step 1: Sort the array
        v.sort()

        # Step 2: Find the median
        n = len(v)
        if n % 2 == 1:
            # If the number of elements is odd, return the middle element
            median = v[n // 2]
        else:
            # If the number of elements is even, return the floor of the average of the two middle elements
            mid1 = v[n // 2 - 1]
            mid2 = v[n // 2]
            median = (mid1 + mid2) // 2  # Use integer division to always return an integer

        return median
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends