import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
data = pd.read_csv('winequality-red.csv', sep=';')
features = data.drop(columns=['quality'])

# Normalize the features
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# Initialize the SOM
som = MiniSom(x=10, y=10, input_len=features_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(features_scaled)

# Train the SOM
som.train_random(features_scaled, 100)

# Assign clusters to each sample
data['Cluster'] = [som.winner(x)[0] * 10 + som.winner(x)[1] for x in features_scaled]

# Create a mapping for cluster markers
marker_map = {
    0: 'o',  # Circle
    1: 's',  # Square
    2: 'D',  # Diamond
    3: '^',  # Triangle Up
    4: 'v',  # Triangle Down
    5: '<',  # Triangle Left
    6: '>',  # Triangle Right
    7: 'p',  # Pentagon
    8: '*',  # Star
    9: 'X'   # X Marker
}

# Create the plot
plt.figure(figsize=(10, 8))

# Get the weights and plot the heatmap
weights = som.get_weights().reshape(10, 10, -1)
mean_weights = np.mean(weights, axis=2)  # Average across all features for color intensity
plt.imshow(mean_weights, cmap='coolwarm', alpha=0.5)

# Plot the data points on top of the heatmap
for i, x in enumerate(features_scaled):
    w = som.winner(x)  # Getting the winner
    cluster_id = data['Cluster'][i] % 10  # Ensure it falls within the defined markers
    plt.scatter(w[0], w[1], marker=marker_map[cluster_id], edgecolor='black', s=100, 
                facecolor=plt.cm.tab10(cluster_id), alpha=0.7)

# Customize the plot
plt.title('SOM Clustering of Wine Quality Dataset', fontsize=15)
plt.xlabel('SOM X-axis', fontsize=12)
plt.ylabel('SOM Y-axis', fontsize=12)
plt.colorbar(label='Mean Weights')
plt.grid(False)
plt.tight_layout()
plt.show()
