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
adata = sc.AnnData(X=sp.sparse.csr_matrix([[0, 1], [1, 0]]))
anndata2ri.py2rpy(adata)


sc.logging.print_versions()
