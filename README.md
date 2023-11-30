# Data Engineering final project

## Table of Contents

- [Branches](#branches)
  - [Main](#branch-1-name)
  - [feature_UMAP_Kmeans](#branch-2-name)
  - [feature_TSNE_KMEANS](#branch-3-name)
  - [feature_acp_kmeans](#branch-4-name)
  - [docker_backbone](#branch-5-name)
  - [tests_bonus](#branch-6-name)
  - [feature_light](#branch-7-name)

## Branches

Here we explain the purpose of each branch in the repository.

### Main

The main branch where we merge all of our approved and tested changes. This branch contains the last version of the project.

### feature_UMAP_Kmeans

The branch where we implemented and tested the UMAP algorithm followed by the KMeans algorithm.

### feature_TSNE_KMEANS

The branch where we implemented and tested the TSNE algorithm followed by the KMeans algorithm.

### feature_acp_kmeans

The branch where we implemented and tested the PCA algorithm followed by the KMeans algorithm.

### docker_backbone

The branch where we initialized docker and worked on the docker container.

### tests_bonus

In this branch we added some additional tests for hyper-parameter tunning, comparing between different dimensionality reduction algorithms and different clustering algorithms.

### feature_light

In this branch we tested removing SentenceTransformer and replacing the dataset with csv files that contains embeddings and labels for a lighter and more efficient docker image.