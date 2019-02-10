#linear search
def ls(arr,l,r,x):
	if r>=l:
		if(arr[l]==x):
			return l
                 if r<l:
                 	return -1	 
                 l=l+1
                 return ls(arr,l,r,x)
arr=[0,2,6,3]
x=6
# Function call
result = ls(arr, 0, len(arr)-1, x)
 
if result != -1:
    print( "Element is present at index %d" % result)
else:
    print ("Element is not present in array")		  


