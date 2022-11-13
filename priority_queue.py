class priority_queue:
    def __init__(self, key=lambda x: x):
        self.A = []
        self.key = key

    # Returns Left child's index of current element index i
    def left_child(self,i):
        return 2 * i + 1

    # Returns Right child's index of current element index i
    def right_child(self,i):
            return 2 * i + 2

    # Function to heapify elements from top to bottom
    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.A) and self.key(self.A[l]) < self.key(self.A[i]): # Checking if left child is less than parent
            smallest = l
        if r < len(self.A) and self.key(self.A[r]) < self.key(self.A[smallest]): # Checking if right child is less than parent
            smallest = r
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i] # placing the smallest element at the parent 
            self.min_heapify(smallest) # recursively heapify smallest node

    # Function to heapify elements from bottom to top after pushing a new element
    def heapify(self, i):
        if i == 0:
            return
        parent = int(((i-1)/2))
        if self.key(self.A[i]) < self.key(self.A[parent]): # Checking if current element is less than parent element
            self.A[i], self.A[parent] = self.A[parent], self.A[i] # swapping both parent and child
            self.heapify(parent) # Recursively heapify the parent element 
        
    # Function to build heap
    def build_min_heap(self):
        n = int((len(self.A)//2)-1)
        for i in range(n, -1, -1):
            self.min_heapify(i) # Calling min_heapify function for every parent starting from last parent level

    # Function to return the top element of min_heap
    def top(self):
        return self.A[0]
    
    
    def empty(self):
        return len(self.A)==0
        
    # Function to push an element into the heap
    def heap_push(self,x):
        self.A.append(x)
        self.heapify(len(self.A)-1)

    # Function to pop the root element of min_heap
    def heap_pop(self):
        self.A[0] = self.A[len(self.A)-1]
        self.A.pop(len(self.A)-1)
        self.min_heapify(0)

# Driver code
# if __name__ == "__main__":
#     flag = True
#     arr = []
#     # Menu Driven Driver Code :
#     while True:
#         print("\nChoose the operation to perform:")
#         print("\t\t1. BUILD_HEAP() ")
#         print("\t\t2. TOP() ")
#         print("\t\t3. PUSH() ")
#         print("\t\t4. POP() ")
#         print("\t\t5. Exit ")
#         choice = int(input("\nEnter your Choice: ")) # Inputting choice
#         if choice != 1 and choice != 5 and flag : # display error if first choice is not '1'
#             print("Build heap first!....")
#         elif choice == 1 and flag:
#             size = int(input("Enter no of elements : ")) # Taking input of elements
#             if(size <= 0):
#                 print("size must be greater than '0' ")
#             else:
#                 for i in range(0, size):
#                     x = int(input(f"enter element {i+1} : "))
#                     arr.append(x)
#                 build_min_heap(arr)
#                 print("prioity queue made using min heap is : ",end="")
#                 print(arr)
#                 flag = False
#         elif choice == 1 and flag == False : # If second time choice '1' is entered
#             print("Heap already created!...")
#         elif choice == 2: 
#             print("Top Element of the heap is : ",top(arr))
#         elif choice == 3: # pushing new Element
#             x = int(input("Enter the element you would like to insert : "))
#             heap_push(arr, x)
#             print("prioity queue after pushing element is : ",end="")
#             print(arr)
#         elif choice == 4: # Popping root element
#             if(len(arr) == 0):
#                 print("No elements to pop from the heap")
#             else:
#                 heap_pop(arr)
#                 print("prioity queue after popping element is : ",end="")
#                 print(arr)
#         elif choice == 5: #exit from program
#             break
#         else: # inavlid input
#             print("Invalid Input! Please, try again.")