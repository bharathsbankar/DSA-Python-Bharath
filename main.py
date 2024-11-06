# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load Wine dataset from UCI repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
columns = ['Alcohol', 'Malic_Acid', 'Ash', 'Alcalinity_of_Ash', 'Magnesium',
           'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols', 'Proanthocyanins',
           'Color_Intensity', 'Hue', 'OD280/OD315_of_Diluted_Wines', 'Proline', 'Class']
data = pd.read_csv(url, header=None, names=columns)

# Select features (ignoring the 'Class' label)
X = data.drop(columns=['Class'])

# Standardize the features for better performance of K-means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method for Optimal K')
plt.show()

# From the Elbow plot, let's assume 3 clusters is the optimal number (for Wine dataset)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Add the cluster labels to the dataset
data['Cluster'] = kmeans.labels_

# Plot the clusters in a scatter plot (using 'Alcohol' and 'Color Intensity' for visualization)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Alcohol', y='Color_Intensity', hue='Cluster', palette='viridis', style='Class')
plt.xlabel('Alcohol')
plt.ylabel('Color Intensity')
plt.title('K-means Clustering of Wine Dataset')
plt.show()

