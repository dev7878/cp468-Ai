import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('kmeans.csv')

# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Plot of the examples/observations')
plt.show()

def euclidean_distance(a, b):
    """
    Function to compute the Euclidean distance between two points a and b.
    """
    return np.sqrt(np.sum((a - b) ** 2))

def kmeans(data, k, epsilon=1e-9):
    """
    Function to perform k-means clustering.
    
    Parameters:
    data: DataFrame containing the data points.
    k: The number of clusters.
    epsilon: The threshold for the change in centroids below which we consider convergence.
    
    Returns:
    centroids: Array containing the final centroids.
    clusters: Array containing the final clusters.
    """
    # Number of examples
    n = len(data)
    
    # Initialize the centroids as the first k data points
    centroids = data[:k].to_numpy()

    # Run the K-means algorithm until convergence
    while True:
        # Assign each observation to the centroid to which it is closest
        clusters = [[] for _ in range(k)]
        for i in range(n):
            distances = [euclidean_distance(data.iloc[i].to_numpy(), centroid) for centroid in centroids]
            closest_centroid_index = np.argmin(distances)
            clusters[closest_centroid_index].append(data.iloc[i].to_numpy())

        # Compute new centroids for each cluster by averaging the data points in each cluster
        new_centroids = [np.mean(cluster, axis=0) for cluster in clusters]

        # Check if the centroids have stopped changing
        centroid_shifts = [euclidean_distance(old, new) for old, new in zip(centroids, new_centroids)]
        if max(centroid_shifts) < epsilon:
            break

        centroids = new_centroids
    
    # Convert clusters to numpy arrays for easier manipulation
    for i in range(k):
        clusters[i] = np.array(clusters[i])
    
    return centroids, clusters

# Apply K-means clustering for k = 2
centroids, clusters = kmeans(data, 2)

# Print the final cluster sizes
print("\nFinal Cluster Sizes:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1} size: {len(cluster)}")

# Print the final centroids
print("Final Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")

# Plot the final clusters and centroids
plt.figure(figsize=(8, 6))
colors = ['b', 'r']

for i, cluster in enumerate(clusters):
    plt.scatter(cluster[:, 0], cluster[:, 1], color=colors[i], alpha=0.6)

for i, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], color=colors[i], edgecolor='k', s=200)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Final Clusters (k=2)')
plt.show()
