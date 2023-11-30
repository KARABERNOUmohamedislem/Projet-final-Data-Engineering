from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np
import umap


def dim_red(mat, p, method):
    '''
    Perform dimensionality reduction

    Input:
    -----
        mat : NxM list 
        p : number of dimensions to keep 
    Output:
    ------
        red_mat : NxP list such that p<<m
    '''
    if method=='ACP':
        df_embeddings = pd.DataFrame(mat, columns=[f"feature_{i}" for i in range(len(mat[0]))])
        pca = PrincePCA(n_components=p)
        pca = pca.fit(df_embeddings)
        red_mat = pca.transform(df_embeddings).to_numpy()
        
    elif method=='TSNE':
        tsne = TSNE(n_components=p, random_state=42)
    	  mat = tsne.fit_transform(mat)
    	  red_mat = mat[:,:p]
        
    elif method=='UMAP':
        mat = umap.UMAP(n_components=p).fit_transform(mat)
        red_mat = mat[:,:p]
        
    else:
        raise Exception("Please select one of the three methods : APC, AFC, UMAP")
    
    return red_mat


def clust(mat, k):
    '''
    Perform clustering

    Input:
    -----
        mat : input list 
        k : number of cluster
    Output:
    ------
        pred : list of predicted labels
    '''
    
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(mat)
    pred =  kmeans.labels_
    
    return pred

# import data
ng20 = fetch_20newsgroups(subset='test')
corpus = ng20.data[:2000]
labels = ng20.target[:2000]
k = len(set(labels))

# embedding
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(corpus)

# Perform dimensionality reduction and clustering for each method
methods = ['ACP', 'TSNE', 'UMAP']
for method in methods:
    # Perform dimensionality reduction
    red_emb = dim_red(embeddings, 20, method)

    # Perform clustering
    pred = clust(red_emb, k)

    # Evaluate clustering results
    nmi_score = normalized_mutual_info_score(pred, labels)
    ari_score = adjusted_rand_score(pred, labels)

    # Print results
    print(f'Method: {method}\nNMI: {nmi_score:.2f} \nARI: {ari_score:.2f}\n')

