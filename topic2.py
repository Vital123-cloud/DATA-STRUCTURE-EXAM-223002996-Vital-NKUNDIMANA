print("\tDouble Linked liste to manage data in the fitness app with real-time health monitoring.\n\t======================================================================================")
class Node:
    def __init__(self, data):
        self.data = data  # Store the data (e.g., health data point)
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The start of the list
        self.tail = None  # The end of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Example usage
fitness_data = DoublyLinkedList()
fitness_data.append("\t<- Step count: 3000 ->")
fitness_data.append("\t<- Calories burned: 200 ->")
fitness_data.prepend("\tHeart rate: 80 bpm->")
fitness_data.display()


print("\n\tDeque to manage data in the fitness app with real-time health monitoring. \n\t========================================================================")


from collections import deque

class FitnessAppDeque:
    def __init__(self, max_size=5):
        self.data = deque(maxlen=max_size)  # max_size determines the limit of the deque

    def add_data(self, data):
        """ Add a new health data point to the deque. """
        self.data.append(data)

    def remove_data(self):
        """ Remove the oldest data point. """
        return self.data.popleft()

    def get_latest_data(self):
        """ Get the most recent data entry. """
        return self.data[-1] if self.data else None

    def display(self):
        """ Display the contents of the deque. """
        for entry in self.data:
            print(entry)

# Example usage
real_time_health_data = FitnessAppDeque(max_size=5)
real_time_health_data.add_data("\tStep count: 3000")
real_time_health_data.add_data("\tCalories burned: 150")
real_time_health_data.add_data("\tHeart rate: 85 bpm")
real_time_health_data.add_data("\tSteps today: 4000")
real_time_health_data.add_data("\tCalories burned: 250")

# Display the latest health data
real_time_health_data.display()

# Add another data point, the oldest data will be removed due to max_size
real_time_health_data.add_data("\tHeart rate: 90 bpm")
real_time_health_data.display()

