# GPX data to Maps of Intensity
JupyterHub [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsramo144/Thesis-Jupyter/HEAD)

Jupyter Notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1FHZmFP5zzuIhBWDRs0thnTZoyAMKdOce?usp=sharing)

:warning: the tool is under development, beta version.

## Extra Tools
### Web tool in Voilà [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsramo144/Thesis-Jupyter/HEAD?urlpath=%2Fvoila%2Frender%2Fgpx2intensity.ipynb)
Voilà is user-friendly way to present automation of Jupyer Notebooks. No coding skills required.
The launch of the virtual environment may take up to one minute generally.
### GPX Compression [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o9xJojiIB2Y-sI7mThGVwW5cIHah0OOV?usp=sharing)
The [python script](scripts/gpx_simplification.py) allows a user to compress the GPX data with a simplification option[^1] available. The final output consists of generalised geographic coordinates only.
Voilà tool allows the user upload max 10 MB, therefore, the tool may be used as an additional data preprocessing step. 

[^1]: Douglas, David; Peucker, Thomas (1973). "Algorithms for the reduction of the number of points required to represent a digitized line or its caricature". The Canadian Cartographer. 10 (2): 112–122. doi:10.3138/FM57-6770-U75U-7727
