import scanpy as sc
import anndata2ri

adata = sc.datasets.blobs()

# basic pipeline
sc.pp.highly_variable_genes(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)
sc.tl.rank_genes_groups(adata, 'leiden')

sc.pl.umap(adata)

# anndata2ri
adata = sc.datasets.pbmc3k()
anndata2ri.py2rpy(adata)


sc.logging.print_versions()
