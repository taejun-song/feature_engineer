from pathlib import Path

import pandas as pd
import numpy as np
from itertools import combinations
from minepy import MINE

from sklearn import tree
from sklearn.preprocessing import scale, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import (
    train_test_split,
    ParameterGrid,
    cross_val_score,
    GridSearchCV,
)
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.feature_selection import mutual_info_regression
from sklearn.neighbors import KernelDensity
from xgboost import XGBRegressor


import seaborn as sns
import matplotlib.pyplot as plt
import mpl_scatter_density  # adds projection='scatter_density'
from matplotlib.colors import LinearSegmentedColormap


def load_data(path: Path, index: str) -> pd.DataFrame:
    return pd.read_csv(path).set_index(index=index, inplace=True).dropna()
