import pandas as pd 

def test_single_cell():
    user_output = pd.read_csv('top5_genes.csv')
    ground_truth = pd.read_csv("validate_top5_genes.csv")
    pd.testing.assert_frame_equal(user_output, ground_truth)

