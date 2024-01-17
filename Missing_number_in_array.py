#Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
#
#Example 1:
#
#Input:
#N = 5
#A[] = {1,2,3,5}
#Output: 4
#Example 2:
#
#Input:
#N = 10
#A[] = {6,1,2,8,3,4,7,10,5}
#Output: 9
#
#Your Task :
#You don't need to read input or print anything. Complete the function MissingNumber() that takes array and N as input  parameters and #returns the value of the missing number.

# Solution


class Solution:
    def missingNumber(self,array,n):
        # code here
        expt_sum=n*(n+1)/2
        act_sum=sum(array)
        return int(expt_sum - act_sum)
