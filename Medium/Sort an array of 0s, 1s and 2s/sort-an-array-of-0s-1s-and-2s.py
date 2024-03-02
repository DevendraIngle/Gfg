#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        # Initialize counts for 0s, 1s, and 2s
        count_zeros = 0
        count_ones = 0
        count_twos = 0
        
        # Count occurrences of 0s, 1s, and 2s in the array
        for num in arr:
            if num == 0:
                count_zeros += 1
            elif num == 1:
                count_ones += 1
            else:
                count_twos += 1
        
        # Update the array with sorted elements
        arr.clear()  # Clear the original array
        
        # Append 0s, 1s, and 2s to the array based on counts
        arr.extend([0] * count_zeros)
        arr.extend([1] * count_ones)
        arr.extend([2] * count_twos)
        
        # Return the sorted array
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends