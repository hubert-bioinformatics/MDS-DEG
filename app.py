from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances
from sklearn.manifold import MDS
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        data = pd.read_csv(file, sep='\t', comment='#')
        data_transposed = data.drop(columns=['gene_id']).T
        data_log = np.log2(data_transposed + 1)
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data_log)
        distance_matrix = pairwise_distances(data_scaled, metric='euclidean')
        mds_3d = MDS(n_components=3, dissimilarity='precomputed', random_state=42)
        mds_results_3d = mds_3d.fit_transform(distance_matrix)
        mds_df_3d = pd.DataFrame(mds_results_3d, columns=['MDS1', 'MDS2', 'MDS3'])
        mds_df_3d['Sample'] = data_transposed.index
        fig = px.scatter_3d(mds_df_3d, x='MDS1', y='MDS2', z='MDS3', color='Sample', title='Interactive 3D MDS Plot of RNA-seq Data')
        plot_html = pio.to_html(fig, full_html=False)
        return render_template('plot.html', plot_html=plot_html)
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)