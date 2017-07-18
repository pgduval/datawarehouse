import numpy as np
import pandas as pd

dim1_att = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
dim2_att = {1: "AA", 2: "BB", 3: "CC", 4: "DD", 5: "EE"}


dim1 = [dim1_att[i] for i in np.random.random_integers(low=1, high=5, size=100)]
dim2 = [dim2_att[i] for i in np.random.random_integers(low=1, high=5, size=100)]

metric1 = list(np.random.random_sample((100,)))

data = pd.DataFrame([dim1, dim2, metric1]).transpose()
data.columns = ['dim1', 'dim2', 'metric1']
data.to_csv("/home/elmaster/project/datawarehouse/source/data.csv", index=False)

