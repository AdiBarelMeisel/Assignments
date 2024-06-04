
The data we are going to analyze is from my rotation at Dr. Moshe Biton's lab.
The lab aims to uncover the connection between the immune system and the gut.
The data is a single cell RNA seq data that shows highly expressed genes in Paneth cells, one of the gut's cell type.
We are interested in the top five gene with the highest average of all the genes with a ratio of above 1, as they are considered "markers" of this cell type.

The file `single_cell_analysis.py` runs the above analysis using the `projenitor_markers.csv` file and outputs the top five genes to the csv file named `top5_genes.csv`
The file `test_single_cell_analysis.py` runs a test in order to compare the results to predetermined results from the `validate_top5_genes.csv` file.