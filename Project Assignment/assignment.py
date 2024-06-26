## COMP1730/6730 Project assignment

# Your ANU ID: u7650690
# Your NAME: Aria Zhao
# I declare that this submission is my own work
# [ref: https://www.anu.edu.au/students/academic-skills/academic-integrity ]

## You should implement the functions with pass as body.
## You can define new function(s) if it helps you decompose the problem
## into smaller subproblems.

import random
import matplotlib.pyplot as plt
import numpy as np
import random
from math import cos, sin, pi

# Task 1

def create_array():
    """ Returns a 1D zero indexed array of length 10 with leading and trailing 1s."""
    return [1,0,0,0,0,0,0,0,0,1]

# Task 2
def simulate_1d_diffusion(array):
    """
    Applies a nearest-neighbor averaging algorithm to a copy of the input array.
    Returns the averaged copy of the input array.
    Assumes the input array is 1D.
    """
    updated = array.copy()
    for i in range(len(array)):
        if i == 0:
            updated[i]=(array[i]+array[i+1])/2
        elif i == len(array) - 1:
            updated[i]=(array[i-1]+array[i])/2
        else:
            updated[i]=(array[i-1]+array[i]+array[i+1])/3
    return updated


# Task 3

def plot_temperatures(initial, new, new2):
    """
    Plots the 3 input arrays overlayed on eachother.
    Assumes input arrays are 1D and are the same length.
    """
    X = list(range(len(initial)))
    Y1, Y2, Y3 = initial, new, new2
    fig, ax = plt.subplots()
    ax.plot(X, Y1, label = "Initial")
    ax.plot(X, Y2, label = "After 1 Iteration")
    ax.plot(X, Y3, label = "After 2 Iterations")
    plt.legend() 
    plt.show()

# 1D diffusion exercise code:
def exercise_1D_diffusion():    
    initial_array = create_array()
    new_array1 = simulate_1d_diffusion(initial_array)
    new_array2 = simulate_1d_diffusion(new_array1)
    plot_temperatures(initial_array, new_array1, new_array2)

# Task 4

def create_grid(size=5):
    """ 
    Returns a square array of given side length.
    Defaults to side length 5 if no length given.
    Interior of returned array is all 0s and boundary cells are all 1s.
    Assumes size is an integer.
    """
    empty = [[0]*size for i in range(size)]
    for x in range(size):
        empty[0][x] = 1
        empty[x][0] = 1
        empty[-1][x] = 1
        empty[x][-1] = 1
    return empty
        
# Task 5

def simulate_2d_diffusion(grid):
    """
    Applies a nearest-neighbor averaging algorithm to a copy of the input array.
    Returns the averaged copy of the input array.
    Assumes the input array is 2D.
    """
    updated = [x[:] for x in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0: 
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i][j+1])/3
            elif i == 0 and j == len(grid[0])-1: 
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i][j-1])/3
            elif i == len(grid)-1 and j == 0: 
                updated[i][j] = (grid[i][j]+grid[i-1][j]+grid[i][j+1])/3
            elif i == len(grid)-1 and j == len(grid[0])-1: 
                updated[i][j] = (grid[i][j]+grid[i-1][j]+grid[i][j-1])/3
            elif i == 0: 
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i][j+1]+grid[i][j-1])/4
            elif j == 0: 
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i-1][j]+grid[i][j+1])/4
            elif i == len(grid)-1: 
                updated[i][j] = (grid[i][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
            elif j == len(grid[0])-1: 
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i-1][j]+grid[i][j-1])/4
            else:
                updated[i][j] = (grid[i][j]+grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/5
    return updated

# 2D diffusion exercise code:
def multiple_iterations(grid, num_iterations):
    for _ in range(num_iterations):
        for row in grid:
            print(' '.join(f'{temp:.2f}' for temp in row))
        print()
        grid = simulate_2d_diffusion(grid)

def exercise_2D_diffusion():    
    multiple_iterations(create_grid(),5)

# Task 6

def simulate_multiple_iterations(grid, num_iterations):
    """
    modified version multiple_iterations() which plots the grids instead of printing to console.
    requires an initial grid and number of iterations to plot as input.
    assumes grid is a 2x2 array and num_iterations is an integer.
    """
    for _ in range(num_iterations):
        plt.imshow(grid, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.show()
        grid = simulate_2d_diffusion(grid)

def simulate_large_scale(num_iterations,size=10):
    """
    Simulates and plots the temperature diffusion for a given number of iterations on a 2x2 array.
    The side length of the array defaults to 10 if no size is specified.
    Interior of initial array is all 0s and boundary cells are all 1s.
    Assumes size and num_iterations are integers.
    """
    simulate_multiple_iterations(create_grid(size), num_iterations)
    pass

# 2D diffusion (numpy implementation) exercise code:
def exercise_2D_diffusion_numpy():
    simulate_large_scale(5)

# Task 7:
    
def create_graph():
    """Generates a graph with nodes having initial random temperatures stored in a separate list."""
    num_nodes = 10
    # Initialize node temperatures
    temperatures = [random.randint(20, 30) for _ in range(num_nodes)]
    # Adjacency list to store edges
    edges = [[] for _ in range(num_nodes)]
    # Manually adding edges
    connections = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (0, 9),
                   (1, 3), (2, 4), (5, 7), (6, 8), (0, 5)]
    for start, end in connections:
        edges[start].append(end)
        edges[end].append(start)
    return edges, temperatures

def visualize_graph(edges, temperatures):
    """Visualizes the graph with node labels showing temperatures."""
    plt.figure(figsize=(10, 10))  # Increase figure size for better visibility
    num_nodes = len(temperatures)
    # Position nodes in a circle
    positions = {i: (cos(2 * pi * i / num_nodes), sin(2 * pi * i / num_nodes)) for i in range(num_nodes)}
    # Draw edges
    for i, neighbors in enumerate(edges):
        for neighbor in neighbors:
            plt.plot([positions[i][0], positions[neighbor][0]], 
                     [positions[i][1], positions[neighbor][1]], 'gray')
    # Draw nodes larger and with clear labels
    for i, pos in positions.items():
        plt.scatter(*pos, color='lightblue', s=1000)  # Increased node size
        plt.text(pos[0], pos[1], f'{temperatures[i]:.1f}°C', color='black', ha='center', va='center', fontweight='bold', fontsize=10)
    plt.axis('off')
    plt.show()

def simulate_diffusion(edges, temperatures):
    """
    Applies a nearest-neighbor averaging algorithm to a copy of the input temperatures array.
    Returns the averaged copy of the temperatures array.
    Assumes edges and temperatures are the same length.
    Assumes temperatures is a 1D array representing the temperature in each node.
    Assumes edges is a 2D array edges[i] where i is the list of nodes connected to node i
    """
    updated = temperatures.copy()
    for node in range(len(edges)):
        n = 1
        for connection in edges[node]:
            updated[node]+=temperatures[connection]
            n+=1
        updated[node]/=n
    return updated

# Graph diffusion exercise code:

def exercise_graph_diffusion():
    edges, temperatures = create_graph()
    print("Initial temperatures:", temperatures)
    visualize_graph(edges, temperatures)
    for _ in range(3):  # simulate multiple iterations
        temperatures = simulate_diffusion(edges, temperatures)
        visualize_graph(edges, temperatures)

    