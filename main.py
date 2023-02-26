def firstOccurance (N, arr, X):
        # code here
        low=0
        high=N-1
        while low<=high:
            mid=(low+high)//2
            if X>arr[mid]:
                low=mid+1
            elif X<arr[mid]:
                 high=mid-1
            else:
                if mid==0 or arr[mid-1]!=arr[mid]:
                    return mid
                else:
                    high=mid-1
               
        return -1
  
N=int(input())
arr=input().split()
for i in range(N):
  arr[i]=int(arr[i])
X=int(input())
print(firstOccurance(N, arr, X))


  