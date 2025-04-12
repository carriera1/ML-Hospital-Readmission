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

#Read in data
data = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

#Replace value with NaN
data.replace("Too Few to Report", np.nan, inplace=True)

#Create an if/else statement where above 1 is categorized as yes, no otherwise
avg = np.where(data["Excess Readmission Ratio"] > 1, "Yes", "No")

#Remove excess readmission ratio because it is the predicted, then other unnecessary predictors
model = MS(data.columns.drop(["Excess Readmission Ratio", "Facility Name", "Facility ID", "State","Measure Name", "Footnote", "Start Date", "End Date"]), intercept=False)
D = model.fit_transform(data)


feature_names = list(D.columns)
X = np.asarray(D)

#Fit the decision tree
clf = DTC(criterion='entropy', max_depth=3, random_state=0)
clf.fit(X, avg)

print("Accuracy Score:",accuracy_score(avg, clf.predict(X)))

print("Residual Deviation:",np.sum(log_loss(avg, clf.predict_proba(X))))

# Print the tree if you want a visual, but it's clustered on my end
#ax = subplots(figsize=(12, 12))[1]
#plot_tree(clf, feature_names=feature_names, ax=ax);
#plt.show()         


#Alternative to the visual, prints each branch
print(export_text(clf,
                  feature_names=feature_names,
                  show_weights=True))
