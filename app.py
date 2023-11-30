from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import pandas as pd
import base64
from .main import dim_red, clust


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
    n_clusters = int(request.form['n_clusters'])
    
    embedding = np.genfromtxt('embeddings.csv', delimiter=",", skip_header=1)
    mat = dim_red(embedding, n_components, dimension_reduction)

    # Cluster using the selected algorithm
    if clustering_algorithm == 'KMeans':
        pred = clust(mat, n_clusters)
    else:
        # Handle other clustering algorithms
        pass

    # Plot the result
    # plt.scatter(df_reduced['Dim1'], df_reduced['Dim2'], c=clusters)
    # plt.title(f'{dimension_reduction} + {clustering_algorithm} Clustering')
    # plt.xlabel('Dimension 1')
    # plt.ylabel('Dimension 2')

    # Save the plot to a BytesIO object
    # img_stream = io.BytesIO()
    # plt.savefig(img_stream, format='png')
    # img_stream.seek(0)

    # Convert the plot to base64 for embedding in HTML
    # dim_img_base64 = base64.b64encode(img_stream.read()).decode('utf-8')

    return render_template('index.html', dim_image="")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
