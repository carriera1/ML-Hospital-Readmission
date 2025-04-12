# Hospital Readmissions Project

## Project Overview 

This hypothetical project was commissioned by a hospital board seeking to reduce costs associated with patient readmissions. Using machine learning methods, I plan to find ways to save money. This file will be used to show each step in the project, instructions to run any code, and disclosure statements.

## Step 1: Find Resources
-Background information related to the data: https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps/hospital-readmissions-reduction-program-hrrp

-Offical paper on the characteristics of readmission https://hcup-us.ahrq.gov/reports/statbriefs/sb304-readmissions-2016-2020.jsp?_gl=1*cn2k9h*_ga*MTk4OTE4Mjc1NC4xNzQ0NDE4MjE5*_ga_1NPT56LE7J*MTc0NDQxODIxOC4xLjAuMTc0NDQxODIxOC4wLjAuMA..

## Step 2: Dataset Assessment
The data comes from https://data.cms.gov/provider-data/dataset/9n3s-kdb3, a government website relating to medicare and medicaid services. The dataset is read in the file step_3_assessment.py. We can see that the data includes 18510 rows of data, along with 12 variable columns. Other assessments can be found in code.

## Step 3: Variable Description
##### Facility Name: Strings containing the name of the facility
##### Facility ID: Unique integer values representing the facility
##### State: Strings containing the state abbreviation of the facility
##### Measure Name: 6 unique strings classifying heart attack (AMI), heart failure (HF), pneumonia (PN), chronic obstructive pulmonary disease (COPD), hip/knee replacement (THA/TKA), and coronary artery bypass graft surgery (CABG)
##### Number of Discharges: Float (with NaN values) containing the number of discharges in the facility
##### Footnote: Float (with NaN values) clarifying the data
##### Excess Readmission Ratio: Float (with NaN values) containing the ratio of readmission based on hospitals with similar patients. Calculated by next two vairables
##### Predicted Readmission Rate: Float (with NaN values) calculated readmission rate based on a precalculated statistical model for the facility
##### Expected Readmission Rate: Float (with NaN values) calculated readmission rate based on a precalculated statistical model using national data
##### Number of Readmissions: Float (with NaN values) containing the number of readmissions
##### Start Date: String in datetime format representing the start of the data collection period.
##### End Date: String in datetime format representing the end of the data collection period.

## Step 4: Research Question
Can we use decision trees to predict whether a hospital will have an above-average excess readmission ratio based on specific predictors?

## Step 5: Research Explanation
The excess readmission ratio determines if a facility is above or below average, based on if it's above 1 or not. Having a higher than 1 ratio means there are more patient readmissions than expected, costing the facility more money. This model will show the predictors that determine a specific facilities ratio, showing what may need to be adressed to save more money. 

## Step 6: Model Solution to Question
A decision tree will be used to handle both categorical and numeric data. This model can also have a high interpretability to the board. The code can be found in the file step_6_chosen-algo.py

## Step 7: Validation of Model
The validation of the model will also be found in step_6_chosen-algo.py

## Instructions to Run Model
To run this model, download the data set found in the repository and the python file "step_6_chosen-algo.py". If you want a visual, remove the # before lines 40-43 of code. Then, run the entire python file to see printed results.

## Conclusions, Predictions, and Recommendations
The already provided models of "Predicted Readmission Rate" and "Expected Readmission Rate" gave the best splits. This is likely because those are the values used to calculate the value we are predicting. I would recommend trying this model again, but with different predictors to see if we can keep the high accuracy without the correlated variables.

## Disclosures: Ethics Statements, Limitations, Generative AI use, and References used.
-Numerous hospitals provided NaN values, as well as reporting "Too Few to Report" in numeric data. The full count can be found in the step_3_assessment.py file

-The data provided includes no revealing data about any patient, and this may lead to limitations because to model doesn't use any data related to patient age and previous medical history. 

-For code, the ISLP labs were used as reference for decision trees and validation of the model.

-Generative AI use was also used for ideas relating to choosing a model and questions about the data
