import pandas as pd 

def find_top_genes():
    single_cell_df = pd.read_csv("projenitor_markers.csv")
    single_cell_df = single_cell_df.loc[single_cell_df['ratio']>1]
    top5_genes = single_cell_df.loc[single_cell_df['avg_log2FC'].nlargest(5).reset_index(0).index]['gene']
    top5_genes.to_csv('top5_genes.csv')


if __name__=='__main__':
    find_top_genes()