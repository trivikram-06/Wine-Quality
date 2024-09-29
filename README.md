# SOM Clustering on Wine Quality Dataset

## Overview
This project demonstrates how to use **Self-Organizing Maps (SOM)** to cluster wines from the **Wine Quality Dataset** based on their chemical features. The goal is to group wines into clusters and visualize their relationships.

## Dataset
The **Wine Quality Dataset** includes chemical properties of red wines with a target quality score between 0 and 10. The dataset contains features like:
- `fixed acidity`
- `volatile acidity`
- `citric acid`
- `residual sugar`, etc.

Dataset link: [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality)

## Prerequisites
Before running the code, ensure you have the following libraries installed:
```bash
pip install pandas matplotlib minisom scikit-learn

## 1. Clone the repository
```bash
git clone https://github.com/your-username/SOM-Wine-Clustering.git
cd SOM-Wine-Clustering

## 2. Run the Python Scripts
1. Train the SOM and Save Cluster Data
This script trains the SOM on the wine dataset and saves the cluster data in a CSV file.
```bash
python wine_quality_segmentation.py
