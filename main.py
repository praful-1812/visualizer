import os
import sys
import pandas as pd

sys.path.append(os.getcwd())

import config_file

# image_widget_url = pn.widgets.TextInput(value='static/images/assets/not_selected.jpg')

class EmbeddingPlot():
    def __init__(self, args):
        self.df_tsv = pd.read_csv(args.tsv_path, sep=args.COLUMN_SEPARATOR)

        embeddings = self.generate_embeddings()

        data = {}
        data['x'] = embeddings[:, 0]
        data['y'] = embeddings[:, 1]
        data['ground_truth'] = self.df_tsv['ground_truth']
        data['top_one_prediction'] = self.df_tsv['top_one_prediction']


    def generate_embeddings():
        pass

    
def main():
    args = object()
    args.__dict__.update(config_file.options)
    image_server_address = "http://" + str(args.image_server) + ":" + str(args.image_server_port) + "/"
    

if __name__ == '__main__':
    main()