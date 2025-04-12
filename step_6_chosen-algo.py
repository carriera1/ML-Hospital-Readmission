import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots
import sklearn.model_selection as skm
from ISLP import confusion_table
from ISLP.models import ModelSpec as MS
from sklearn.tree import (DecisionTreeClassifier as DTC,
                          DecisionTreeRegressor as DTR,
                          plot_tree,
                          export_text)
from sklearn.metrics import (accuracy_score,
                             log_loss)


data = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

data.replace("Too Few to Report", np.nan, inplace=True)

avg = np.where(data["Excess Readmission Ratio"] > 1, "Yes", "No")


model = MS(data.columns.drop(["Excess Readmission Ratio", "Facility Name", "Facility ID", "State","Measure Name", "Footnote", "Start Date", "End Date"]), intercept=False)
D = model.fit_transform(data)

feature_names = list(D.columns)
X = np.asarray(D)

clf = DTC(criterion='entropy', max_depth=3, random_state=0)
clf.fit(X, avg)
