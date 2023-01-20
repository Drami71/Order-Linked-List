#Name: Daniel Ramirez
#Project 7
#This file contains two classes that will be utilized to create an ordered list. 
#The Node class will be utilized alongside the Ordered List class
#to create an simple organized linked list from a text file containing
#actions and fruits. The two classes are largely the same as the ones presented 
#in the textbook with a method in the Ordered List class
#to print out the list after each pass

class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data              #Node class used to create nodes in the linked list
                                      #along with methods to access and modify data and the next reference
    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None             #Method to check if list is empty

    def add(self, item):
        current = self.head                  #Method to add an item to linked list
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def size(self):
        current = self.head                 #Method returns size of list
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):              #Method to search for an item to see if it is in list
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
            
    def remove(self, item):
        current = self.head              #Method to remove an item from linked list
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    
    def printlist(self):            #Method to print the linked list
       fruitlist = []               #Use a while loop to add each item to the list
       currentnode = self.head      #to display using the current node and
       while currentnode != None:   #each subsequent node
           fruitlist.append((currentnode.getData()))
           currentnode = currentnode.getNext()
       print(fruitlist)

