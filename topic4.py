print("\tDeque to manage a fixed number of orders in the fitness app with real-time health monitoring.\n\t============================================================================================")
from collections import deque

class FitnessAppDeque:
    def __init__(self, max_size=5):
        """Initialize a deque to manage fitness orders with a fixed size."""
        self.order_queue = deque(maxlen=max_size)

    def add_order(self, order):
        """Add a new health order (data point) to the deque."""
        self.order_queue.append(order)

    def process_order(self):
        """Process (remove) the oldest health order in the deque."""
        if self.order_queue:
            oldest_order = self.order_queue.popleft()  # FIFO: Removes the front element
            print("\t"+f"Processed Order:\n{oldest_order}")
            return oldest_order
        else:
            print("No orders to process.")
            return None

    def get_latest_order(self):
        """Retrieve the most recent health order without removing it."""
        return self.order_queue[-1] if self.order_queue else None

    def display_orders(self):
        """Display all the current orders in the deque."""
        print("\tCurrent Health Orders:")
        for order in self.order_queue:
            print(order)

# Example usage
fitness_orders = FitnessAppDeque(max_size=5)

# Add fitness orders to the deque (e.g., real-time health data points)
fitness_orders.add_order("\tStep count: 3000 steps")
fitness_orders.add_order("\tCalories burned: 200 kcal")
fitness_orders.add_order("\tHeart rate: 80 bpm")
fitness_orders.add_order("\tDistance walked: 2 km")
fitness_orders.add_order("\tActive minutes: 45 minutes")

# Display current fitness orders
fitness_orders.display_orders()

# Adding a new order will remove the oldest one because the deque is full
fitness_orders.add_order("\tHeart rate: 85 bpm")
fitness_orders.display_orders()

# Process (remove) the oldest fitness order
fitness_orders.process_order()

# Display the deque after processing the oldest order
fitness_orders.display_orders()

# Get the latest order (without removing it)
latest_order = fitness_orders.get_latest_order()
print("\t"+f"Latest Order:\n{latest_order}")
