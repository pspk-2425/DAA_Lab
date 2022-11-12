def merge(arr,l,m,r):
    n1 = m-l+1
    n2 = r-m

    temp1 = [0]*n1
    temp2 = [0]*n2

    for i  in range(0,n1):
        temp1[i] = arr[l+i]

    for j  in range(0,n2):
        temp2[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if(temp1[i][1] <= temp2[j][1]):
            arr[k] = temp1[i]
            i+=1
        else:
            arr[k] = temp2[j]
            j+=1
        k+=1

    while(i<n1):
        arr[k] = temp1[i]
        i+=1
        k+=1

    while(j<n2):
        arr[k] = temp2[j]
        j+=1
        k+=1


def merge_sort(arr,l,r):
    if l<r:
        m = l+(r-l)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

def schedule_class(arr):
    finish = 0
    res = []
    for i in arr:
        if finish <= i[0]:
            finish = i[1]
            res.append(i)
    return res

if __name__ == "__main__":
    N = int(input("Enter the total no of classes : "))
    print()
    class_intervals = []
    print("---> Enter Timings in 24hr Format <---\n")
    for i in range(0,N):
        start = int(input(f"Enter the start time of class {i+1}: "))
        if(start <= 0 or start > 24):
            print("Error! Time must be in 24hr format")
            exit(0)
        end   = int(input(f"Enter the finish time of class {i+1}: "))
        if(end <= 0 or end > 24):
            print("Error! Time must be in 24hr format")
            exit(0)
        class_intervals.append((start,end))
        print()
    ans = []
    # class_intervals.sort(key=lambda x: x[1])
    merge_sort(class_intervals,0,len(class_intervals)-1)
    ans = schedule_class(class_intervals)
    print("Max no of classes that can be scheduled are : ",end=" ")
    print(len(ans))
    print(ans)