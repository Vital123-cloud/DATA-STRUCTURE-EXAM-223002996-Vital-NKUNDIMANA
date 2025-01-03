print("Implementation of a tree to represent hierarchical data in the fitness app with real-time health monitoring.\n===========================================================================================================")
import time
class TreeNode:
    def __init__(self, name, data=None):
        """Initialize a node with a name, optional data, and children."""
        self.name = name  # The name of the node (e.g., Cardio, Running, Heart Rate)
        self.data = data  # Data associated with the node (e.g., heart rate, steps)
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        """Add a child node to this node (e.g., new activity or data point)."""
        self.children.append(child_node)

    def update_data(self, data):
        """Update the data of this node (e.g., update the step count or calories burned)."""
        self.data = data

    def display(self, level=0):
        """Display the node's data and recursively display all children."""
        indent = " " * (level * 2)
        print(f"{indent}{self.name}: {self.data if self.data else 'No Data'}")
        for child in self.children:
            child.display(level + 1)

class FitnessAppTree:
    def __init__(self):
        """Initialize the fitness app tree with a root node."""
        self.root = TreeNode("Fitness Data")

    def add_activity(self, activity_name, data=None, parent_name=None):
        """Add a new activity or data point to the tree under a specific parent node."""
        parent_node = self.find_node(self.root, parent_name) if parent_name else self.root
        new_node = TreeNode(activity_name, data)
        parent_node.add_child(new_node)

    def update_activity_data(self, activity_name, new_data):
        """Update the data of a specific activity."""
        node = self.find_node(self.root, activity_name)
        if node:
            node.update_data(new_data)
            print(f"Updated {activity_name} data to {new_data}")
        else:
            print(f"Activity '{activity_name}' not found.")

    def find_node(self, node, name):
        """Recursively search for a node by its name."""
        if node.name == name:
            return node
        for child in node.children:
            found_node = self.find_node(child, name)
            if found_node:
                return found_node
        return None

    def display_tree(self):
        """Display the entire hierarchical tree of fitness data."""
        self.root.display()

# Example usage of the FitnessAppTree with real-time data
def simulate_health_monitoring():
    fitness_tree = FitnessAppTree()

    # Adding top-level categories for fitness metrics
    fitness_tree.add_activity("Cardio")
    fitness_tree.add_activity("Strength Training")
    fitness_tree.add_activity("Nutrition")

    # Adding activities under "Cardio"
    fitness_tree.add_activity("Running", 5000, parent_name="Cardio")  # steps taken
    fitness_tree.add_activity("Cycling", 3000, parent_name="Cardio")  # steps taken

    # Adding activities under "Strength Training"
    fitness_tree.add_activity("Push-ups", 50, parent_name="Strength Training")  # reps
    fitness_tree.add_activity("Weight Lifting", 100, parent_name="Strength Training")  # weight lifted in kg

    # Adding activities under "Nutrition"
    fitness_tree.add_activity("Calories Consumed", 1800, parent_name="Nutrition")  # calories eaten
    fitness_tree.add_activity("Water Intake", 2, parent_name="Nutrition")  # liters of water consumed

    # Display the initial state of the tree
    print("Initial Fitness Data:")
    fitness_tree.display_tree()

    # Simulating real-time updates (e.g., after a workout or daily update)
    time.sleep(2)  # Simulate time passing
    fitness_tree.update_activity_data("Running", 5500)  # Update steps
    fitness_tree.update_activity_data("Push-ups", 60)  # Update reps

    # Display updated tree after real-time data changes
    print("\nUpdated Fitness Data (after real-time updates):")
    fitness_tree.display_tree()

# Run the simulation to test the fitness app tree
simulate_health_monitoring()
