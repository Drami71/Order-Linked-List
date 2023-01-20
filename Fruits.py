#Name: Daniel Ramirez
#Project 7
#This file imports the Project7 file to created an Ordered Linked List. It opens the supplied fruit file
#and processes it. It splits each line to access the action, i.e. insert and delete, and the fruit to access
#easier. It then checks to see if the first index, the action, is insert. If it is, it adds the second index, the fruit,
#to the list. If it is not insert, it proceeds to check if the action is delete. If it is, it checks if the fruit is in 
#the list at the moment and if it is, then it removes the fruit. This continues until each line is processed


import Project7

def main():

    create_list()

def create_list():

    fruit_file = open("fruit_file.txt", "r")        #Open text file to read
    my_list = Project7.OrderedList()                #Create list
    for line in fruit_file:                         #Process each line
        fruit_list = line.rsplit()                  #splits line to access info easier
        action = fruit_list[0]                      #places action and fruit into variables
        fruit = fruit_list[1]
        if action == "insert":                      #if action is equal to insert
            my_list.add(fruit)                      #add fruit to the list
        else: 
            if action == "delete":                  #if action is equal to delete
                value = my_list.search(fruit) 
                if value == True:                   #first check if that fruit is in the list and if so remove it
                    my_list.remove(fruit)
        
        my_list.printlist()                        #calls printlist method to display full list of fruits during this pass

    fruit_file.close()
            
main()