"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    # create a new node
    new_node = Node(value, None)
      
    # check if the list is empty. If the list is empty set the head and the tail to the newly created node
    if not self.head:
      self.head = new_node
      self.tail = new_node
    # if the list is not empty, set the pointer to the next node of the tail node to the newly created node. then set the tail to the newly created node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    if not self.head.get_next():
      head = self.head
      self.head = None
      self.tail = None
      return head.get_value()
    value =  self.head.get_value()
    self.head = self.head.get_next()
    return value


  def contains(self, value):
    if not self.head:
      return False
    if self.head.get_value() == value:
      return True
    current = self.head.get_next()
    while current:
      if current.get_value() == value:
        return True
      current = current.get_next()

    

  def get_max(self):
    if not self.head:
      return None
    maximum = self.head.get_value()
    current = self.head.get_next()
    while current:
      if current.get_value() > maximum:
        maximum = current.get_value()
      current = current.get_next()
    return maximum
