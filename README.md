![Build](https://github.com/dcgc-bfx/dcgc-single-cell/workflows/Build/badge.svg?branch=main)
[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/5095)

# dcgc-single-cell

DCGC singularity recipe for single cell analysis

Pull it from the singularity hub: https://singularity-hub.org/collections/5095

Start jupyter lab:

```bash
singularity run --writable-tmpfs --app jupyter shub://dcgc-bfx/dcgc-single-cell
```

Start rstudio server listening on port 8787:

```bash
singularity run --writable-tmpfs --app rserver shub://dcgc-bfx/dcgc-single-cell 8787
```
