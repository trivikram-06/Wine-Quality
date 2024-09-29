SOM Clustering on Wine Quality Dataset
Overview
This project uses Self-Organizing Maps (SOM) to cluster the Wine Quality Dataset based on chemical properties of red wines. The goal is to group wines into clusters and visualize them using different plots like the U-Matrix and average quality by cluster.

Dataset
The Wine Quality Dataset contains chemical data of red wines with a target quality variable (0–10 rating). Features include:

fixed acidity, volatile acidity, citric acid, residual sugar, etc.
You can download the dataset here.

Installation
Install the required Python packages:

bash
Copy code
pip install pandas matplotlib minisom scikit-learn
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/SOM-Wine-Clustering.git
cd SOM-Wine-Clustering
Place the dataset (winequality-red.csv) in the project folder.

Run the scripts:

Train SOM & save cluster data:

bash
Copy code
python wine_quality_segmentation.py
Generate U-Matrix:

bash
Copy code
python uplot_umatrix.py
Visualize clusters with markers:

bash
Copy code
python uplot_umatrix.py
Plot average wine quality by cluster:

bash
Copy code
python plot_bar_graphss.py
Visualizations
U-Matrix: Shows the distances between SOM neurons to reveal clusters.
Cluster Plot: Visualizes SOM clusters with different markers.
Average Quality: Bar chart showing average wine quality by cluster.
Conclusion
The project clusters wines based on their features and provides visual insights using SOM.
