import random

def Main():
    lili = LinkedList()
    lst = [1,3,9,4,2,9,5,6,7,8,10, 9]
    for i in lst:
        lili.add(i)
    
    print(f'size: {lili.getSize()}')
    print(f'Get element at index 7: {lili.get(7)}') #Get element at index 7
    print(f'Set element at index 7 to value 2 with set method: {lili.set(7, 2)}') #Set element at index 7 to 2
    print(f'Get element at index 7: {lili.get(7)}') #Get element at index 7
    print(f'Get element at index 15, should print index out of range and return False: {lili.get(15)}')
    print(f'Get index of first element with value 9 with indexOf method: {lili.indexOf(9)}')
    print(f'Get index of first element with value 16 with indexOf method, should return -1: {lili.indexOf(16)}')
    print(f'Get index of last element with value 9 with lastIndexOf method: {lili.lastIndexOf(9)}')
    print(f'Get index of last element with value 16 with lastIndexOf method, should return -1: {lili.lastIndexOf(16)}')
    print(f'Check if list contains element 5 with contains: {lili.contains(5)}')
    print(f'Check if list contains element 15 with contains, should return False: {lili.contains(17)}')
    print(f'Remove 8 from list with remove method: {lili.remove(8)}')
    print(f'size: {lili.getSize()}')
    print(f'Check if 8 is removed with contains, should return False: {lili.contains(8)}')
    print(f'Test clear method: {lili.clear()}')
    print(f'size: {lili.getSize()}')
    print(f'Get element at index 7: {lili.get(7)}') #Check that values are gone
    
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0
        return f'Linked List cleared'

    # Return true if this list contains the element o 
    def contains(self, e):
        current = self.__head
        while current != None:
            if current.element == e:
                return True
            current = current.next
        return False
            

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        current = self.__head
        parent = None
        
        if not self.__head: #Tom liste
            return False
        if self.__head.element == e:
            self.__head = self.__head.next
            self.__size -= 1
            return True
        
        while current != None:
            parent = current
            current = current.next
            if current.element == e:
                parent.next = current.next
                self.__size -= 1
                return True
                
            
        return False

    # Return the element from this list at the specified index 
    def get(self, index):
        current = self.__head
        if index == 0:
            return self.__head.element
        else:
            for i in range(0, index):
                try:
                    current = current.next
                except AttributeError:
                    print("Index out of range")
                    break
        if current == None:
            return False
                
        return current.element

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        index = 0
        current = self.__head
        while current.element != e:
            current = current.next
            index += 1
            if current == None:
                return -1
        return  index

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        index = 0
        idxlist = []
        current = self.__head
        while current != None:
            if current.element == e:
                idxlist.append(index)
            current = current.next
            index += 1
            
        if len(idxlist) == 0:
            return -1
        else: 
            return idxlist[-1]
           

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        current = self.__head
        if index == 0:
            self.__head.element = e
        for i in range(0, index):
            try:
                current = current.next
            except AttributeError:
                print("Index does not exist")
                break
        if current == None:
            return False
        current.element = e
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    

Main()