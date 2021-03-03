# dcgc-single-cell

![Build](https://github.com/dcgc-bfx/dcgc-single-cell/workflows/Build/badge.svg?branch=main)

DCGC singularity recipe for single cell analysis

Pull it from the cloud library: https://cloud.sylabs.io/library/fabianrost84/dcgc/single-cell.sif#

Start jupyter lab:

```bash
singularity run --writable-tmpfs --app jupyter library://fabianrost84/dcgc/single-cell.sif
```

Start rstudio server:

```bash
singularity run --writable-tmpfs --app rstudio-server library://fabianrost84/dcgc/single-cell.sif 8787
```
