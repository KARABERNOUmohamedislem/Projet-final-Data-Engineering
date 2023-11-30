# Data Engineering final project

Project website: [Link Text](https://data-engineering.onrender.com/)
P.S: The website might take long to render for the first time because it's deployed using a free instance. 

## Table of Contents

- [Branches](#branches)
  - [Main](#Main)
  - [feature_UMAP_Kmeans](#feature_UMAP_Kmeans)
  - [feature_TSNE_KMEANS](#feature_TSNE_KMEANS)
  - [feature_acp_kmeans](#feature_acp_kmeans)
  - [docker_backbone](#docker_backbone)
  - [tests_bonus](#tests_bonus)
  - [feature_light](#feature_light)
  - [Readme_update](#Readme_update)
- [Usage](#usage)

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


### Readme_update

This branch was used to update the Readme file.


## Usage

To use our docker image, pull it using this command :

```console
docker pull touaziaimenryad/projet_final_data_engineering
```

Then run it using :

```console
docker run -p 5000:5000 touaziaimenryad/projet_final_data_engineering:latest
```

To mirror the files/folder in the host inside the docker, use :

```console
docker run -p 5000:5000 -v $(pwd):/app touaziaimenryad/projet_final_data_engineering:latest
```