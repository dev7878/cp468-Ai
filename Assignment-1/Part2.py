import csv
import math
from collections import deque

# Define the City class
class City:
    def __init__(self, name, latitude, longitude):
        # Constructor for City class, initializes city name, latitude and longitude
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

# Define the function to calculate distance between two cities
def distance(city1, city2):
    R = 6371  # Radius of earth in KM
    lat1, lon1 = math.radians(city1.latitude), math.radians(city1.longitude)  # Convert lat and long to radians
    lat2, lon2 = math.radians(city2.latitude), math.radians(city2.longitude)
    
    a = math.sin((lat2-lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2-lon1)/2)**2
    # Calculate the distance using the Haversine formula and return it
    return 2 * R * math.asin(math.sqrt(a))

# Define the function to load cities from CSV file
def load_cities(filename):
    cities = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, _, lat, lon = row
            cities.append(City(name, float(lat), float(lon)))  # Create a City object and add it to the list
    return cities

# Define the Depth-First Search (DFS) function
def dfs(cities):
    visited = set()
    stack = [0]  # Start from the first city
    path = []
    # Keep looping until the stack is empty
    while stack:
        city = stack.pop()
        # If the city is not visited, mark it as visited and add it to the path
        if city not in visited:
            visited.add(city)
            path.append(cities[city].name)
            # Add all unvisited neighbours to the stack
            stack.extend(neighbour for neighbour in range(len(cities)) if neighbour not in visited)
    return path

# Define the Breadth-First Search (BFS) function
def bfs(cities):
    visited = set()
    queue = deque([0])  # Start from the first city
    path = []
    # Keep looping until the queue is empty
    while queue:
        city = queue.popleft()
        # If the city is not visited, mark it as visited and add it to the path
        if city not in visited:
            visited.add(city)
            path.append(cities[city].name)
            # Add all unvisited neighbours to the queue
            queue.extend(neighbour for neighbour in range(len(cities)) if neighbour not in visited)
    return path

# Define the function to calculate the total distance of a path
def shortest_distance(path, cities):
    # Sum up the distances between consecutive cities in the path (cycle back to the first city in the end)
    return sum(distance(cities[i], cities[(i+1)%len(cities)]) for i in range(len(cities)))

# Load the cities from the CSV file
cities = load_cities('city_data_50.csv')

# Perform DFS and calculate the total distance of the path
dfs_path = dfs(cities)
print("DFS Shortest Distance: ", shortest_distance(dfs_path, cities))
print("DFS Path: ", ' -> '.join(dfs_path))

# Perform BFS and calculate the total distance of the path
bfs_path = bfs(cities)
print("BFS Shortest Distance: ", shortest_distance(bfs_path, cities))
print("BFS Path: ", ' -> '.join(bfs_path))