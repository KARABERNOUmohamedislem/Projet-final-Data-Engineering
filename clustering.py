from sklearn.cluster import AgglomerativeClustering, SpectralClustering, Birch, MiniBatchKMeans
from sklearn.mixture import GaussianMixture

models = {
    'AR' : lambda k : AgglomerativeClustering(n_clusters=k),
    'GM' :  lambda k : GaussianMixture(n_components=k),
    'SC' :  lambda k : SpectralClustering(n_clusters=k),
    'Birch' :  lambda k : Birch(n_clusters=k),
    'MiniBatchKMeans' :  lambda k : MiniBatchKMeans(n_clusters=k),
}

def other_clustering(data, k, method) :
    model = models[method](k)
    pred = model.fit_predict(data)
    return pred