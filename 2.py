def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def min_heapify(A,i):
    l = left_child(i)
    r = right_child(i)
    smallest = i
    if l<len(A) and A[l] < A[smallest]:
        smallest = l
    if r<len(A) and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A,smallest)

def heapify(A,i):
    if i == 0:
        return
    parent = int((i-1)/2)
    if A[i] < A[parent] :
        A[i],A[parent] = A[parent],A[i]
        heapify(A,parent)

def build_min_heap(A):
    n = int(len(A)/2-1)
    for i in range(n,-1,-1):
        min_heapify(A,i)


def heap_push(A,x):
    A.append(x)
    heapify(A,len(A)-1)

def top(A):
    return A[0]

def heap_pop(A):
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)
    min_heapify(A,0)

def empty_heap(A):
    return len(A) == 0

# Driver code
if __name__ == "__main__":
    flag = True
    arr = []
    # Menu Driven Driver Code :
    while True:
        print("\nChoose the operation to perform:")
        print("\t\t1. BUILD_HEAP() ")
        print("\t\t2. TOP() ")
        print("\t\t3. PUSH() ")
        print("\t\t4. POP() ")
        print("\t\t5. Exit ")
        choice = int(input("\nEnter your Choice: ")) # Inputting choice
        if choice != 1 and choice != 5 and flag : # display error if first choice is not '1'
            print("Build heap first!....")
        elif choice == 1 and flag:
            size = int(input("Enter no of elements : ")) # Taking input of elements
            if(size <= 0):
                print("size must be greater than '0' ")
            else:
                for i in range(0, size):
                    x = int(input(f"enter element {i+1} : "))
                    arr.append(x)
                build_min_heap(arr)
                print("prioity queue made using min heap is : ",end="")
                print(arr)
                flag = False
        elif choice == 1 and flag == False : # If second time choice '1' is entered
            print("Heap already created!...")
        elif choice == 2: 
            print("Top Element of the heap is : ",top(arr))
        elif choice == 3: # pushing new Element
            x = int(input("Enter the element you would like to insert : "))
            heap_push(arr, x)
            print("prioity queue after pushing element is : ",end="")
            print(arr)
        elif choice == 4: # Popping root element
            if(len(arr) == 0):
                print("No elements to pop from the heap")
            else:
                heap_pop(arr)
                print("prioity queue after popping element is : ",end="")
                print(arr)
        elif choice == 5: #exit from program
            break
        else: # inavlid input
            print("Invalid Input! Please, try again.")