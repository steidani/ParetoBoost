# ParetoBoost: Predicting weather extremes

by Jonathan Koh and Daniel Steinfeld  
*Oeschger Centre for Climate Change Research, University of Bern  

This repository contains all code for downloading and processing ERA5 data, and for training and testing a ParetoBoost model.

## Set up

Set up the conda environment:

```bash
conda env create -f environment.yml
conda activate paretoboost
```

download the data:

```bash
python3 scripts/download_era5.py
```

## Quick start

You can follow the tutorial in `notebooks/01_predict_t2m_europe.ipynb` to get started.  
Using geopotential at 500 hPa (z500) as the input variable, we can predict the 2m surface temperature (target variable) of the next day. Three different models are trained and tested:

- baseline: climatoloy and persistence
- linear regression using sklearn
- Convolutional neural network (CNN) using Keras

## Notebooks

- `00_preprocess_era5.ipynb`: preprocessing the predictor (z500) and target variables (t2m), including regridding and calculating standardised anomalies
- `01_predict_t2m_europe.ipynb`: Testing three different models to see if z500 is a good predictor of t2m
