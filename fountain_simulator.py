import threading
import random
import time
from datetime import datetime
from itertools import product

# Define a class for the fountains
class Fountain(threading.Thread):
    def __init__(self, name, color=None):
        super().__init__()
        self.name = name
        self.color = color
        self.cycles = random.randint(1, 3)  # Random number of cycles (1 to 3)
    
    def run(self):
        # Get the start time
        start_time = datetime.now().strftime("%H:%M:%S")
        if self.color:
            print(f"{self.name} started at: {start_time} with color {self.color}. Total cycles: {self.cycles}")
        else:
            print(f"{self.name} started at: {start_time}. Total cycles: {self.cycles}")
        
        # Perform each cycle with random ON and OFF times
        for cycle in range(1, self.cycles + 1):
            on_time = random.randint(1, 5)  # Random ON time (1 to 5 seconds)
            off_time = random.randint(1, 5)  # Random OFF time (1 to 5 seconds)
            
            # Start ON phase
            on_start_time = datetime.now().strftime("%H:%M:%S")
            time.sleep(on_time)  # Simulate ON time
            on_end_time = datetime.now().strftime("%H:%M:%S")
            
            # If this is not the last cycle, do the OFF phase
            if cycle < self.cycles:
                off_start_time = datetime.now().strftime("%H:%M:%S")
                time.sleep(off_time)  # Simulate OFF time
                off_end_time = datetime.now().strftime("%H:%M:%S")
                print(
                    f"{self.name} - Cycle {cycle}: "
                    f"ON for {on_time}s ({on_start_time} to {on_end_time}), "
                    f"OFF for {off_time}s ({off_start_time} to {off_end_time})"
                )
            else:
                print(
                    f"{self.name} - Cycle {cycle}: "
                    f"ON for {on_time}s ({on_start_time} to {on_end_time}), "
                    f"OFF phase skipped (last cycle)"
                )
        
        # Get the finish time
        finish_time = datetime.now().strftime("%H:%M:%S")
        if self.color:
            print(f"{self.name} finished at: {finish_time} with color {self.color}")
        else:
            print(f"{self.name} finished at: {finish_time}")


# Stage 1: Fountains run one after another (sequential)
def stage_1():
    print("\nStage 1: Sequential Execution")
    
    # Create fountains
    fountain1 = Fountain("Fountain 1")
    fountain2 = Fountain("Fountain 2")
    fountain3 = Fountain("Fountain 3")
    
    # Start fountains sequentially
    fountain1.start()
    fountain1.join()  # Wait for fountain1 to finish
    
    fountain2.start()
    fountain2.join()  # Wait for fountain2 to finish
    
    fountain3.start()
    fountain3.join()  # Wait for fountain3 to finish

# Stage 2: Fountains run in pairs
def stage_2():
    print("\nStage 2: Pairwise Execution")
    
    # Create fountains
    fountain1 = Fountain("Fountain 1")
    fountain2 = Fountain("Fountain 2")
    fountain3 = Fountain("Fountain 3")
    
    # Start Fountain 1 and 2 together
    fountain1.start()
    fountain2.start()
    fountain1.join()  # Wait for both fountains to finish
    fountain2.join()
    
    # Start Fountain 1 and 3 together
    fountain1 = Fountain("Fountain 1")  # Recreate fountains to restart them
    fountain3 = Fountain("Fountain 3")
    fountain1.start()
    fountain3.start()
    fountain1.join()
    fountain3.join()
    
    # Start Fountain 2 and 3 together
    fountain2 = Fountain("Fountain 2")
    fountain3 = Fountain("Fountain 3")
    fountain2.start()
    fountain3.start()
    fountain2.join()
    fountain3.join()

# Stage 3: All fountains run simultaneously with color combinations (with and without colors)
def stage_3():
    print("\nStage 3: Simultaneous Execution")

    # Define the colors for each fountain
    colors = ['Blue', 'Red', 'Green']

    # Generate all combinations of 3 colors for 3 fountains (3^3 = 27 combinations)
    color_combinations = list(product(colors, repeat=3))

    # Stage 3a: Execution without colors
    print("\nStage 3a: Running without Colors")
    # Create fountains without color (only one set of fountains)
    fountain1 = Fountain("Fountain 1")
    fountain2 = Fountain("Fountain 2")
    fountain3 = Fountain("Fountain 3")
    
    # Start all fountains simultaneously
    fountain1.start()
    fountain2.start()
    fountain3.start()
    
    # Wait for all fountains to finish
    fountain1.join()
    fountain2.join()
    fountain3.join()

    # Stage 3b: Execution with colors
    print("\nStage 3b: Running with Colors")
    for combo in color_combinations:
        print(f"\nExecuting combination: {combo}")
        
        # Create fountains with the corresponding colors
        fountain1 = Fountain("Fountain 1", combo[0])
        fountain2 = Fountain("Fountain 2", combo[1])
        fountain3 = Fountain("Fountain 3", combo[2])
        
        # Start all fountains simultaneously
        fountain1.start()
        fountain2.start()
        fountain3.start()
        
        # Wait for all fountains to finish
        fountain1.join()
        fountain2.join()
        fountain3.join()



# Main function to run all stages
def main():
    stage_1()  # Run stage 1
    stage_2()  # Run stage 2
    stage_3()  # Run stage 3

# Execute the program
if __name__ == "__main__":
    main()
