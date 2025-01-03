print("Quick Sort to sort the fitness app with real-time health monitoring data based on priority.\n==========================================================================================")
import random
# Example Fitness Data with Name and Priority
fitness_data = [
    {"name": "Running", "priority": 3, "data": "5000 steps"},
    {"name": "Push-ups", "priority": 5, "data": "50 reps"},
    {"name": "Cycling", "priority": 2, "data": "3000 steps"},
    {"name": "Calories Consumed", "priority": 4, "data": "1800 kcal"},
    {"name": "Water Intake", "priority": 1, "data": "2 liters"}
]

def quick_sort(data, low, high):
    """Quick Sort function that sorts fitness data based on priority."""
    if low < high:
        # Partition the list and get the pivot index
        pi = partition(data, low, high)

        # Recursively apply the quick_sort on the left and right sublists
        quick_sort(data, low, pi - 1)
        quick_sort(data, pi + 1, high)

def partition(data, low, high):
    """Partition function that selects the pivot and rearranges the list."""
    pivot = data[high]["priority"]  # Choosing the last element's priority as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        # If current element's priority is less than or equal to the pivot
        if data[j]["priority"] <= pivot:
            i += 1
            # Swap the elements
            data[i], data[j] = data[j], data[i]
    
    # Swap the pivot element with the element at index i + 1
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def display_sorted_data(data):
    """Display the sorted fitness data."""
    for item in data:
        print(f"Activity: {item['name']}, Priority: {item['priority']}, Data: {item['data']}")

# Apply Quick Sort to the fitness data based on priority
quick_sort(fitness_data, 0, len(fitness_data) - 1)

# Display the sorted fitness data
print("Sorted Fitness Data (by Priority):")
display_sorted_data(fitness_data)
