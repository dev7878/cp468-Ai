import csv
import math


def load_city_data(filename):
    city_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # Skip the header row
        for row in reader:
            city_data.append({
                'name': row[0],
                'description': row[1],
                'latitude': float(row[2]),
                'longitude': float(row[3])
            })
    # print(city_data)
    return city_data


def calculate_distance(city1, city2):
    lat1, lon1 = city1['latitude'], city1['longitude']
    lat2, lon2 = city2['latitude'], city2['longitude']
    radius = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula to calculate distance between two points
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * \
        math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    # print(distance)
    return distance


def create_distance_matrix(city_data):
    num_cities = len(city_data)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = calculate_distance(
                city_data[i], city_data[j])
    # print(distance_matrix)
    return distance_matrix


# Load city data
city_data = load_city_data('Assignment-1\city_data_50.csv')

# Create distance matrix
distance_matrix = create_distance_matrix(city_data)

# Solve TSP using depth-first search
dfs_distance, dfs_route = depth_first_search(city_data, distance_matrix)

# Solve TSP using breadth-first search
bfs_distance, bfs_route = breadth_first_search(city_data, distance_matrix)

# Print results
print(f"Depth-First Search:\nDistance: {dfs_distance}\nRoute: {dfs_route}\n")
print(f"Breadth-First Search:\nDistance: {bfs_distance}\nRoute: {bfs_route}\n")
