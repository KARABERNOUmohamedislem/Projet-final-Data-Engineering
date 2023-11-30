from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import numpy as np
import base64
from main import dim_red, clust
from clustering import other_clustering

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get user input
    dimension_reduction = request.form['dimension_reduction']
    clustering_algorithm = request.form['clustering_algorithm']
    n_components = int(request.form['n_components'])
    n_clusters = 20
    
    embedding = np.genfromtxt('embeddings.csv', delimiter=",", skip_header=1)
    mat = dim_red(embedding, n_components, dimension_reduction)

    # Cluster using the selected algorithm
    if clustering_algorithm == 'KMeans':
        pred = clust(mat, n_clusters)
    else:
        pred = other_clustering(mat,n_clusters,clustering_algorithm)

    print(mat.shape)
    labels = np.genfromtxt('labels.csv', delimiter=",", skip_header=1).astype(int)
    # Plot the DimRed result
    plt.switch_backend('agg')
    plt.scatter(mat[:,0], mat[:,1], c=labels)
    plt.title(f'{dimension_reduction}')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')

    # Save the DimRed plot to a BytesIO object
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Convert the plot to base64 for embedding in HTML
    dim_img_base64 = base64.b64encode(img_stream.read()).decode('utf-8')

    # Plot the Clustring result
    plt.scatter(mat[:,0], mat[:,1], c=pred)
    plt.title(f'{clustering_algorithm}')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')

    # Save the DimRed plot to a BytesIO object
    img_stream_cl = io.BytesIO()
    plt.savefig(img_stream_cl, format='png')
    img_stream_cl.seek(0)

    # Convert the plot to base64 for embedding in HTML
    cl_img_base64 = base64.b64encode(img_stream_cl.read()).decode('utf-8')

    return render_template('index.html', dim_image=dim_img_base64,clust_image= cl_img_base64)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
