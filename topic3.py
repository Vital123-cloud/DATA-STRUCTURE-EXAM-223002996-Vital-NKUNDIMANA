print("\t Implementation of Queue for fitness app with real-time health monitoring processing.\n\t====================================================================================")
import queue

class FitnessAppQueue:
    def __init__(self, max_size=5):
        """ Initialize the queue with a specified max size """
        self.data_queue = queue.Queue(maxsize=max_size)

    def add_data(self, data):
        """ Add new health data to the queue. """
        if self.data_queue.full():
            print("\tQueue is full. Oldest data will be removed.")
            self.data_queue.get()  # Remove the oldest data to make space for the new one
        self.data_queue.put(data)  # Add the new health data point

    def process_data(self):
        """ Process (retrieve) and remove the oldest data point from the queue. """
        if not self.data_queue.empty():
            oldest_data = self.data_queue.get()  # FIFO: Remove the front element
            print("\t"+f"Processed Data:\n{oldest_data}")
            return oldest_data
        else:
            print("Queue is empty. No data to process.")
            return None

    def display(self):
        """ Display the current contents of the queue. """
        print("\tCurrent Health Data in Queue:")
        for item in list(self.data_queue.queue):  # Convert to list for easier display
            print(item)

# Example usage
real_time_health_data_queue = FitnessAppQueue(max_size=5)

# Add real-time health data to the queue
real_time_health_data_queue.add_data("\tStep count: 3000")
real_time_health_data_queue.add_data("\tCalories burned: 150")
real_time_health_data_queue.add_data("\tHeart rate: 85 bpm")
real_time_health_data_queue.add_data("\tSteps today: 4000")
real_time_health_data_queue.add_data("\tCalories burned: 250")

# Display the current queue contents
real_time_health_data_queue.display()

# Adding more data after the queue has reached its max size
real_time_health_data_queue.add_data("\tHeart rate: 90 bpm")
real_time_health_data_queue.display()

# Process (retrieve) the oldest data (FIFO)
real_time_health_data_queue.process_data()

# Display the queue after processing
real_time_health_data_queue.display()
