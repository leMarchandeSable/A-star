# A* Pathfinding and Maze Generation in Pygame

This project showcases A* pathfinding, a popular pathfinding algorithm, and allows you to generate mazes using Pygame. A* is used to find the shortest path from a start point to an end point while avoiding obstacles. You can also interactively create mazes and visualize the algorithm's operation.

![A_star4](https://user-images.githubusercontent.com/95425179/166672036-b9fe8992-de65-4973-8b07-900f8e8e8d0f.gif)

![A_star2](https://user-images.githubusercontent.com/95425179/166672119-38d6ffdd-f380-400c-982d-4c723002b252.gif)

![A* Pathfinding Screenshot](astar.png)

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Usage](#usage)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How it Works](#how-it-works)
- [Maze Generation](#maze-generation)

## Overview

This project combines A* pathfinding and maze generation in a Pygame-based environment. You can visualize how the A* algorithm calculates the shortest path from a start point to an end point, avoiding obstacles in the form of walls. Additionally, you can interactively create mazes and observe the algorithm's operation.

## Key Features

- A* Pathfinding: The project implements the A* pathfinding algorithm for finding the shortest path.
- Interactive Maze Creation: You can interactively generate mazes by adding walls to the grid.
- Maze Solving: Visualize how the A* algorithm efficiently finds the path from start to end, avoiding obstacles.
- Educational Tool: It can serve as an educational tool for understanding pathfinding algorithms and maze generation.

## Usage

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

2. **Install Dependencies**: Ensure you have Python and the Pygame library installed on your system.

3. **Run the A* Pathfinding**: Execute the `astar.py` script to see A* pathfinding in action.

```bash
python astar.py
```

4. **Run Maze Generation**: Execute the `maze_generation.py` script to interactively create mazes.

```bash
python maze_generation.py
```

## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites:

- Python 3
- Pygame library

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/astar-maze.git
cd astar-maze
```

2. Install the required dependencies, especially the Pygame library:

```bash
pip install pygame
```

## How it Works

The project combines A* pathfinding with maze generation. You can visualize how the A* algorithm efficiently finds the shortest path from the start point to the end point while avoiding obstacles represented as walls.

## Maze Generation

You can interactively create mazes by clicking on the grid to add walls. The algorithm will then calculate the shortest path around these walls.
