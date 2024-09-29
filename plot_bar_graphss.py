import pandas as pd
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv('winequality-red.csv', sep=';')
features = data.drop(columns=['quality'])

scaler = MinMaxScaler()
features_scaled = scaler.fit_transform(features)

som = MiniSom(x=10, y=10, input_len=features_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(features_scaled)

som.train_random(features_scaled, 100)


data['Cluster'] = [som.winner(x)[0] * 10 + som.winner(x)[1] for x in features_scaled]


avg_quality_by_cluster = data.groupby('Cluster')['quality'].mean()


plt.figure(figsize=(12, 6))
bars = plt.bar(avg_quality_by_cluster.index, avg_quality_by_cluster.values, width=0.5) 

plt.title('Average Wine Quality by Cluster', fontsize=16)
plt.ylabel('Average Quality', fontsize=12)
plt.xlabel('Cluster Number', fontsize=12)

plt.xticks(avg_quality_by_cluster.index, [f'Cluster {i}' for i in avg_quality_by_cluster.index], rotation=45, ha='right')

for bar in bars:
    bar.set_width(0.4)  
    bar.set_x(bar.get_x() + 0.1)  

plt.tight_layout()  
plt.show()
