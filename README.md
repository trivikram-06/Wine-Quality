# SOM Clustering on Wine Quality Dataset

## Overview
This project demonstrates how to use **Self-Organizing Maps (SOM)** to cluster wines from the **Wine Quality Dataset** based on their chemical features. The goal is to group wines into clusters and visualize their relationships.

## Dataset
The **Wine Quality Dataset** includes chemical properties of red wines with a target `quality` score between 0 and 10. The dataset contains features like:
- `fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, etc.

Dataset link: [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

## Prerequisites
Before running the code, ensure you have the following libraries installed:
```bash
pip install pandas matplotlib minisom scikit-learn
Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/SOM-Wine-Clustering.git
cd SOM-Wine-Clustering
2. Add the Dataset
Place the winequality-red.csv file in the project directory.

3. Run the Python Scripts
1. Train the SOM and Save Cluster Data
This script trains the SOM on the wine dataset and saves the cluster data in a CSV file.

bash
Copy code
python wine_quality_segmentation.py
Script: wine_quality_segmentation.py
Output: cluster_counts.csv
Description: The SOM is trained, and the wines are assigned to clusters based on their chemical properties.
2. Generate U-Matrix Heatmap
This script generates and saves the U-Matrix heatmap, which shows the distances between neurons.

bash
Copy code
python uplot_umatrix.py
Script: uplot_umatrix.py
Output: u_matrix.png
Description: Visualizes the distance map of the SOM, highlighting potential cluster boundaries.
3. Visualize Clusters with Markers
This script visualizes the SOM clusters with different markers based on the wine quality.

bash
Copy code
python uplot_umatrix.py
Script: uplot_umatrix.py
Output: Interactive plot
Description: The wines are plotted on the SOM grid with different markers representing different clusters.
4. Plot Average Wine Quality by Cluster
This script creates a bar chart of the average wine quality for each cluster.

bash
Copy code
python plot_bar_graphss.py
Script: plot_bar_graphss.py
Output: Interactive bar graph
Description: Shows the average quality of wine in each cluster, helping identify patterns across the clusters.
Visualizations
The project includes the following visualizations:

U-Matrix Heatmap: Displays a heatmap of distances between SOM neurons to visualize clusters.
Cluster Marker Plot: Shows the clusters with different markers on the SOM grid.
Bar Chart: Displays the average wine quality for each cluster.
Conclusion
The project demonstrates how Self-Organizing Maps (SOM) can be used to cluster wines based on their chemical features and visualize the clustering patterns using various plots.

css
Copy code

This `README.md` file provides a clear overview of your project, including installation instructions, scripts to run, and a summary of visualizations and conclusions. You can easily paste this content into your `README.md` file in your GitHub repository.





