from node import Node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
#   Function to get the head node
  def get_head_node(self):
    return self.head_node

#  To place the new Value at the beginning 
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

    # to print out our various nodes 
  def stringify_list(self):

    string_list = ""
    current_node = self.get_head_node()

    while current_node:

      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"

      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):

    current_node = self.get_head_node()

    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()

    else:
      while current_node:
        next_node = current_node.get_next_node()
        
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node