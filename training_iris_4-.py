import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df_iris = pd.DataFrame(np.column_stack((iris.data,iris.target)), columns=iris.feature_names+['target'])

df_iris.describe()