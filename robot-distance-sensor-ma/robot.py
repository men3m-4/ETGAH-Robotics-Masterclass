# Code Description
# This Code simulates a robot distance sensor 
# It reads a list of distance measurements, validates the data,and determines the appropriate robot movement (STOP, SLOW, MOVE FAST)

class Robot:

    def __init__(self,name,battery): # Initializes the robot with a name and battery level
        self.name = name
        self.battery = battery 

    def evaluate_distances(self, distances): # Evaluates a list of distance values and outputs corresponding movement commands
        results = []
        for distance in distances:
            try:
                distance = float(distance)
                if distance < 0:
                    results.append(f"INVALID ({distance})") # Collect results in a list to format and print all actions on a single line (matching example output)
                elif distance < 0.5:
                    results.append("STOP")
                elif distance <= 1.0:
                    results.append("SLOW")
                else:
                    results.append("MOVE FAST")
            except (ValueError, TypeError):
                results.append(f"INVALID ({distance})")

        print(", ".join(results))# Formats and prints all movement commands on a single line separated by commas (STOP, SLOW, MOVE FAST)

robot = Robot("Etgah", 44)
print(f"Robot: {robot.name} | Battery: {robot.battery}" )

# Test Case 1: Standard Example
print("Test 1 (Standard):")
robot.evaluate_distances([0.3, 1.5, 0.8, 2.0, 0.4])

# Test Case 2: Boundary Values
print("\nTest 2 (Boundaries):")
robot.evaluate_distances([0.0, 0.5, 1.0, 1.01])

# Test Case 3: Negative Values
print("\nTest 3 (Negative Values):")
robot.evaluate_distances([-0.5, -10, 0.2])

# Test Case 4: Invalid Types
print("\nTest 4 (Invalid Types):")
robot.evaluate_distances(["0.4", "ABC", None, 1.8])

# Test Case 5: Empty List
print("\nTest 5 (Empty List):")
robot.evaluate_distances([])