class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1
        for ele in range(len(arr)-1):
            if arr[ele+1]-arr[ele]<=1:
                pass
            else:
                arr[ele+1]=arr[ele]+1
        return max(arr)