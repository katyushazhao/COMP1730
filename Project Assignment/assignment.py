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
    """ returns created array """
    return [1,0,0,0,0,0,0,0,0,1]

# Task 2
def simulate_1d_diffusion(array):
    """ argument: current array
        returns updated array """
    updated = array.copy()
    updated[0] = (array[0]+array[1])/2
    updated[-1] = (array[-1]+array[-2])/2
    for i in range(len(array)):
        n = 3
        if i == 0:
            updated[i]=(array[i]+array[i+1])
            n -= 1
        else:
            try:
                updated[i]=(array[i-1]+array[i]+array[i+1])
            except IndexError:
                n -= 1
        updated[i]/=n
    return updated


# Task 3

def plot_temperatures(initial, new, new2):
    """parameters: initial=original array, new=after 1 iteration, new2=after 2 iterations"""
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
    """ argument: grid division
    returns size x size 2D grid as list of list """
    empty = [[0]*size for i in range(size)]
    for x in range(size):
        empty[0][x] = 1
        empty[x][0] = 1
        empty[-1][x] = 1
        empty[x][-1] = 1
    return empty
        
# Task 5

def simulate_2d_diffusion(grid):
    """ argument: current 2D grid 
    returns updated grid after one iteration of simulation """
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
    for _ in range(num_iterations):
        plt.imshow(grid, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.show()
        grid = simulate_2d_diffusion(grid)

def simulate_large_scale(num_iterations,size=10):
    """ arguments: num_iterations=number of iterations to perform,
                   size=dimension of 2D grid 
        No return value.
        Use NumPy for efficient large-scale simulation and visualization, correctly handling edges."""
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
    """ arguments: edges=edge list defining graph, 
    temperatures=current temps of graph nodes
    returns updated temperatures list"""
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

    