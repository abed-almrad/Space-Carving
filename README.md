# Space-Carving
Implementation of the space carving algorithm to create 3D shapes from a collection of 2D images taken from multiple points of view.

# Instructions

## Data

The [Multiview Datasets](https://vision.in.tum.de/data/datasets/3dreconstruction) provided by Technical University of Munich are used for this project.

**P.S.** Before implementing the algorithms, make sure to download the datasets and place them in a folder called "DataSets" in your Downloads directory.

## Algorithms

Six different versions of the space carving algorithm were developped. Each version can be implemented by simple and direct execution. 

Only the name of the dataset object needs to be specified in the algorithm's code, the silhouette_extract.py and projection.py files before running anything.

## Visualizer

Any IDE that is able to interpret .pro files, can be used to run the viewer and visualize the algorithms resulting 3D meshes.

At the end of each algorithm version, the resulting mesh is stored as a .txt file, the name of this generated file needs to be specified in Qt Creator's execution parameters before visualizing the results of this aglorithm.
