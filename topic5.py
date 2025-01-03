print("Deque to track data dynamically in fitness app with real-time health monitoring\n===============================================================================")
from collections import deque
import time

class FitnessAppDeque:
    def __init__(self, max_size=5):
        """Initialize a deque to store real-time fitness data with a fixed max size."""
        self.data_queue = deque(maxlen=max_size)

    def add_data(self, data):
        """Add new health data to the deque."""
        self.data_queue.append(data)

    def remove_oldest_data(self):
        """Remove and return the oldest health data from the deque (FIFO)."""
        if self.data_queue:
            oldest_data = self.data_queue.popleft()
            return oldest_data
        else:
            return None

    def get_latest_data(self):
        """Get the latest health data without removing it from the deque."""
        if self.data_queue:
            return self.data_queue[-1]
        else:
            return None

    def display_data(self):
        """Display the current contents of the deque."""
        if self.data_queue:
            print("Current Health Data:")
            for entry in self.data_queue:
                print(entry)
        else:
            print("No health data available.")

# Example usage to simulate real-time health data tracking
def simulate_health_data_tracking():
    # Initialize the deque with a max size of 5
    health_data = FitnessAppDeque(max_size=5)

    # Simulate real-time health data updates (e.g., every 2 seconds)
    data_points = [
        "Step count: 3000",
        "Calories burned: 200 kcal",
        "Heart rate: 80 bpm",
        "Step count: 3500",
        "Calories burned: 220 kcal",
        "Heart rate: 82 bpm",
        "Step count: 4000",
        "Calories burned: 250 kcal",
        "Heart rate: 85 bpm",
        "Step count: 4500"
    ]

    # Simulate adding real-time health data to the deque
    for data in data_points:
        print(f"Adding data: {data}")
        health_data.add_data(data)
        health_data.display_data()
        time.sleep(2)  # Simulate waiting for 2 seconds before the next data point

    # Display the latest health data
    print("\nLatest Health Data:", health_data.get_latest_data())

    # Remove and display the oldest health data
    print("\nRemoving the oldest data:")
    health_data.remove_oldest_data()
    health_data.display_data()

# Run the simulation
simulate_health_data_tracking()
