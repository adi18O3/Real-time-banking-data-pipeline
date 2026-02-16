
# Bank Customer Segmentation and Visualization Using Big Data Technologies

## Overview

This project, **Bank Customer Segmentation and Visualization Using Big Data Technologies**, leverages big data tools and techniques to segment and visualize bank customers based on their transactional behaviors and demographic attributes. By analyzing a comprehensive dataset containing various customer details and transaction records, the project identifies distinct customer segments using advanced data analytics and machine learning algorithms.

## Project Goals

The key goals of this project include:
- Segmenting bank customers based on patterns in their demographic data and transaction behaviors.
- Visualizing the identified customer segments.
- Providing insights that can help banks enhance customer relationship management (CRM), optimize marketing strategies, and improve overall customer satisfaction through personalized services.

  
  
## Features
- **Data Processing**: Uses big data technologies to efficiently process and manage large volumes of customer and transaction data.
- **Segmentation**: Employs machine learning algorithms like KMeans and Hierarchical Clustering to identify customer segments.
- **Visualization**: Generates visualizations to interpret the customer segments and insights from the data analysis.

  

## Files and Notebooks:

- **Abstract.txt**: Provides an overview of the project and its objectives.
  
- **Bank_Customer_Segmentation_ETL.ipynb**:
- Contains the code for the ETL (Extract, Transform, Load) processes, data preprocessing, and initial analysis.
- Apply different aggregation form geting some insight.
- Extract feature to existing feature.
- Load data into Parquet and csv format.
  
- **DataFatch_From_Hive.ipynb**:
- Fetch data from Hive tables and read Parquet files.
- Extract and describe the schema of Parquet files.
- Integrate Spark with Hive to perform SQL queries on Hive tables.
  
- **Hierarchical_Clustering.ipynb**:
- Includes the implementation of hierarchical clustering to segment customers.
- Use silhouette score to finnd best cluster.
- very less effective on this data.
  
- **KMeans_K6.ipynb**:
- Setting up and training the K-Means model with range of clusters.
- Evaluating the clustering performance using the Silhouette score.
- Analyzing the cluster centers and the distribution of data points across clusters.
- Performing detailed analysis of clusters, including the range of key features within each cluster.
  
- **Model.ipynb**:
- We select best cluster with good silhouette score in which we use k=6 cluster.
- Perform prediction on this model.
  
- **Bank_Segmentation_data_Dashboards.pdf**:
- Content the dashboard we create for visualize the data in tableau.
- it consist 4 dashbaord with diffrent graphs.
  


## Technologies Used
- **Python**: Programming language used for data analysis and machine learning.
- **Big Data Technologies**: Technologies such as Apache Spark and Hadoop were utilized for managing and analyzing large datasets.
- **Jupyter Notebooks**: Used for interactive development and documentation of the project.
- **Machine Learning Libraries**: Includes libraries such as Scikit-learn for implementing KMeans and Hierarchical Clustering.
- **Tableau**: For visualizing the data and differentiate between customers.

## Conclusion
By implementing this project, banks can utilize customer segmentation to personalize their services and optimize their business strategies. The integration of big data technologies ensures the scalability and efficiency required to handle large datasets in the banking sector.

