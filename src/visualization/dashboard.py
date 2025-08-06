"""
Project Agora: Real-time Simulation Dashboard
Part of The Concordia Project v8.2

This module provides a real-time visualization of the simulation's
key metrics using matplotlib.
"""
import matplotlib.pyplot as plt

class Dashboard:
    """Creates a real-time plot of the simulation's world state."""
    def __init__(self):
        self.day_history = []
        self.wellbeing_history = []
        self.progress_history = []
        
        plt.ion() # Turn on interactive mode
        self.fig, self.ax1 = plt.subplots(figsize=(10, 6))
        
        # Setup for a second y-axis
        self.ax2 = self.ax1.twinx()
        
        self.fig.suptitle('Project Agora: A.D.A.M. Impact Simulation')

    def update(self, world_state: dict):
        """Updates and redraws the plot with the latest world state data."""
        self.day_history.append(world_state['day'])
        self.wellbeing_history.append(world_state['user_wellbeing'])
        self.progress_history.append(world_state['project_progress'])
        
        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()
        
        # Plot User Wellbeing on the left y-axis
        self.ax1.plot(self.day_history, self.wellbeing_history, 'g-', label='User Wellbeing (1-10)')
        self.ax1.set_xlabel('Simulation Day')
        self.ax1.set_ylabel('User Wellbeing', color='g')
        self.ax1.set_ylim(0, 10)
        self.ax1.tick_params(axis='y', labelcolor='g')

        # Plot Project Progress on the right y-axis
        self.ax2.plot(self.day_history, self.progress_history, 'b-', label='Project Progress (%)')
        self.ax2.set_ylabel('Project Progress (%)', color='b')
        self.ax2.set_ylim(0, 100)
        self.ax2.tick_params(axis='y', labelcolor='b')

        # Draw the plot
        plt.pause(0.01)
