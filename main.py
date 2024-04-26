#Class to declare node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.freq = 0
    self.next = None

#Class to declare Linked List class and operations
class LinkedList:
  def __init__(self):
    self.tail = None
    self.head = None
    self.freq = 0
    self.count = 0

#Function to add data to the front of the linked list
  def pushFront(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
    self.count += 1
    newNode.freq += 1

#Function to ass data to the end of the linked list
  def pushEnd(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
      newNode.freq += 1
    self.count += 1

#Function to search for a value to see if it is already in the list
  def searchValue(self, index):
    temp = self.head
    found = 0
    if(temp != None):
      while (temp != None):
        if(temp.data==index):
          found += 1
          break
        temp = temp.next
      if(found == 1):
        temp.freq += 1
        print(f"\n{index} has a frequency of {temp.freq} in the linked list.")
        return True
      else:
        print(f"\n{index} is not found in the linked list.")
        return False
    else:
      print(f"\n{index} is not found in the linked list.")

  def search(self, index):
    temp = self.head
    found = 0
    if(temp != None):
      while (temp != None):
        if(temp.data==index):
          found += 1
          break
        temp = temp.next
      if(found == 1):
        print(f"\n{index} has a frequency of {temp.freq} in the linked list.")
        return True
      else:
        print(f"\n{index} is not found in the linked list.")
        return False
    else:
      print(f"\n{index} is not found in the linked list.")

#Remove the first value in the linked list 
  def removeFirst(self, data):
    if self.head != None:
      temp = self.head
      if self.head.data == data:
        self.head = self.head.next
        temp = None
      else:
        print("/nItem not found in linked list.")

#Remove specified value in linked list
  def removeData(self, data):
    temp = self.head
    prev = temp
    found = 0
    if(temp != None):
      while (temp != None):
        if(temp.data == data):
          found += 1
          break
        prev = temp
        temp = temp.next
      if(found == 1):
        if temp.freq <= 1:
          prev.next = temp.next
          temp = None
        else:
          temp.freq -= 1
      else:
        print("/nItem not found in linked list.") 

#Add a value to the linked list
  def append(self, data):
    if self.count == 0:
      self.pushFront(data)
    else:
      if self.searchValue(data) == False:
        self.pushEnd(data)

#Remove a value from the linked list
  def delete(self, data):
    if self.count == 0:
      print("\nLinked List empty. Can't delete.")
    elif self.count == 1:
      self.removeFirst(data)
    else:
      self.removeData(data)

#Print linked list
  def printLL(self):
    current = self.head
    while(current != None):
      print(f"{current.data}:{current.freq}")
      current = current.next 
        


def menu():
  print("\n[1] Search for a word. \n[2] Add a word. \n[3] Remove a word. \n[4] Print word frequencies. \n[5] Exit.")

menu()
choice = int(input("\nChoose an operation to perform on the linked list: "))
LL = LinkedList()

while choice != 5:
  
  #Check to see if user wants to search the frequency of a word
  if choice == 1:
    word = input("\nEnter a word you would like to find the frequency of in the list: ")
    LL.search(word)
  #Check to see if the user wants to add a word to the linked list or, if it already exists, increase it frequency without adding another node
  elif choice == 2:
    word = input("\nEnter a word to add to the end of the linked list: ")
    LL.append(word)

  #Check to see if the user wants to delete a word from the list. If the frequency is reduced to 0 then remove the word. Otherwise reduce frequency by 1.
  elif choice == 3:
    word = input("\nEnter a word to remove or reduce the frequency of in the linked list: ")
    LL.delete(word)

#Print the values in the linked list with their corresponding frequencies
  elif choice == 4:
    print("\n")
    LL.printLL()

#Break while loop for menu and exit program
  elif choice == 5:
    pass
  else:
    print("\nInvalid option. Please try again.\n")

  menu()
  choice = int(input("\nChoose an operation to perform on the linked list: "))

print("\nThank you for using the program. Goodbye.")
