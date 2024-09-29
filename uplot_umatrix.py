# plot_umatrix.py
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
import pandas as pd

# Load the dataset
data = pd.read_csv('winequality-red.csv', sep=';')
features = data.drop(columns=['quality'])

# Normalize the features
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

# Initialize the SOM
som = MiniSom(x=10, y=10, input_len=features_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(features_scaled)

# Train the SOM
som.train_random(features_scaled, 100)

# Create a U-Matrix
u_matrix = som.distance_map().T

# Plot the U-Matrix
plt.figure(figsize=(10, 7))
plt.pcolor(u_matrix, cmap='coolwarm')
plt.colorbar(label='Distance')
plt.title('U-Matrix of the SOM')
plt.xlabel('SOM X-axis')
plt.ylabel('SOM Y-axis')
plt.savefig('u_matrix.png')  # Save the plot as an image
plt.tight_layout()  # Adjust layout for better spacing
plt.show()

