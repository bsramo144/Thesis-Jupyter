# GPX data to Maps of Intensity
Jupyter Notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FHZmFP5zzuIhBWDRs0thnTZoyAMKdOce?usp=sharing)

JupyterHub (supporting Voilà) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsramo144/Thesis-Jupyter/HEAD)

:warning: the tool is under development, beta version.

## Supporting Tools
### Web Application in Voilà [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsramo144/Thesis-Jupyter/HEAD?urlpath=%2Fvoila%2Frender%2Fgpx2intensity.ipynb)
Voilà is user-friendly way to present Jupyer Notebooks workflow. No coding skills required.
The launch of the virtual environment may take up to one minute generally.
### GPX Compression [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o9xJojiIB2Y-sI7mThGVwW5cIHah0OOV?usp=sharing)
The [python script](scripts/gpx_simplification.py) allows a user to compress the GPX data with a simplification option[^1] available. The final output consists of generalised geographic coordinates only.
Voilà tool allows the user upload max 10 MB, therefore, the tool may be used as an additional data preprocessing step. 

## Workflow Documentation
![Workflow Diagram](https://user-images.githubusercontent.com/47752920/234070295-6493a543-8fe1-4754-b331-a9a5a3bd54b9.png)

### Pre-Processing
The parametrization and data upload parts are the only parts expecting a direct user interaction of the workflow. The user sets 11 parameters that have a direct impact on the final product. The parameters consist of (2) directories for data input and output, (1) parameter for street network download, (9) map matching parameters such as level of generalization, GNSS measurement noise, thresholds etc. The detailed explanation of parametrization is explained in script comentaries or explanatory table. The data upload refers to the link of GPX data either to the local file or to the given sample data web repository. The access to the set of GPX files is mandatory for the automation process to execute.

### Data Mining: Map Matching
Map Matching follows the structure of a Python package responsible for matching the GNSS measurements to the street network[^2]. The matching is enriched with spatial filtering and generalization. The core part starts with the download of the street network from OSM[^3], the extent is defined by the input data and the parameter for buffering. 

The MM works on the probabilistic calculation of possible paths, therefore, the parametrization is crucial for the result. The output of the analysis is a sequence of passed nodes on the street network. The nodes construct matched routes to the network. In the same step, the traces of mobility are concatenated into so-called tracks that serve as a reference to the matched result.

### Post-Processing: Outputs
Post-processing has two main goals for automation. Firstly, the matched routes are overlayed with a blank street network on which are calculated frequencies i.e., the number of matched passages through the street. Secondly, the variables are transformed into data structures ready for data geospatial visualization and storage.

The result visualization and storage part serves the user as a preview of the result. The asset supports the user with a simple visualization in form of an interactive web map[^4]. Based on the visualization one can readjust the parametrization that would fit the characteristics of the study area or the input data. The results can be stored as the web map (HTML format) or as geodata (GeoJSON, GeoPackage formats). More sophisticated and accurate maps should be made in GIS integrating the output geodata.


[^1]: Douglas, David; Peucker, Thomas (1973). "Algorithms for the reduction of the number of points required to represent a digitized line or its caricature". The Canadian Cartographer. 10 (2): 112–122. doi:10.3138/FM57-6770-U75U-7727
[^2]: Meert, W., & Verbeke, M. (2018). HMM with non-emitting states for Map Matching. In European Conference on Data Analysis (ECDA), Date: 2018/07/04-2018/07/06, Location: Paderborn, Germany. Python package 
<a href="https://leuvenmapmatching.readthedocs.io/en/latest/" target="_blank"> documentation</a>.
[^3]: Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. Computers, Environment and Urban Systems, 65, 126-139.
[^4]: Wu, Q. (2021). Leafmap: A Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment. Journal of Open Source Software, 6(63), 3414. https://doi.org/10.21105/joss.03414
