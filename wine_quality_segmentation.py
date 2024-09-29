import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom

data = pd.read_csv('winequality-red.csv', sep=';')  

print("Loaded Data:")
print(data.head())

features = data.drop(columns=['quality'])


scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)


som = MiniSom(x=10, y=10, input_len=features_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(features_scaled)

som.train_random(features_scaled, 100)

win_map = som.win_map(features_scaled)

cluster_counts = {i: len(win_map[i]) for i in win_map.keys()}
pd.DataFrame(cluster_counts.items(), columns=['Cluster', 'Count']).to_csv('cluster_counts.csv', index=False)

print("SOM training complete and cluster data saved.")
