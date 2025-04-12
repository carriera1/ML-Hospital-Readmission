import pandas as pd
import numpy as np

data = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

data["Above_Average"] = (data["Excess Readmission Ratio"] > 1).astype(int)

x_df = data[["Number of Discharges", "Predicted Readmission Rate", "Number of Readmissions"]].copy()

y_df = data["Above_Average"]

