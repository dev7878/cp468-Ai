import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv('boston.csv')

# a) How many rows and columns are in this data set? What do the rows and columns represent?
num_rows = data.shape[0]
num_cols = data.shape[1]
print(f"The data set has {num_rows} rows and {num_cols} columns.")
print("Each row represents a census tract in Boston, and each column represents a predictor.")

# b) Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.
pd.plotting.scatter_matrix(data, figsize=(12, 12))
plt.show()
print("The scatterplots show the relationships between pairs of predictors.")
print("The diagonal plots show the distribution of each predictor, and the off-diagonal plots show the relationships between pairs of predictors.")

# c) Are any of the predictors associated with per capita crime rate? If so, explain the relationship.
crime_corr = data.corr()['crim'].drop('crim')
predictors_with_correlation = crime_corr[crime_corr.abs() > 0.3]
print("The following predictors have a correlation coefficient of at least 0.3 with per capita crime rate:")
print(predictors_with_correlation)
print("A positive correlation indicates that as the predictor increases, the per capita crime rate tends to increase as well.")

# d) Do any of the census tracts of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.
high_crime_tracts = data[data['crim'] > data['crim'].mean() + 2 * data['crim'].std()]
high_tax_tracts = data[data['tax'] > data['tax'].mean() + 2 * data['tax'].std()]
high_ptratio_tracts = data[data['ptratio'] > data['ptratio'].mean() + 2 * data['ptratio'].std()]
print(f"There are {len(high_crime_tracts)} census tracts with particularly high crime rates.")
print(f"There are {len(high_tax_tracts)} census tracts with particularly high tax rates.")
print(f"There are {len(high_ptratio_tracts)} census tracts with particularly high pupil-teacher ratios.")
print("The range of each predictor can be examined using the describe() method:")
print(data[['crim', 'tax', 'ptratio']].describe())

# e) How many of the census tracts in this data set bound the Charles River?
charles_river_tracts = data[data['chas'] == 1]
num_charles_river_tracts = len(charles_river_tracts)
print(f"{num_charles_river_tracts} census tracts in this data set bound the Charles River.")

# f) What is the median pupil-teacher ratio among the towns in this data set?
median_ptratio = data['ptratio'].median()
print(f"The median pupil-teacher ratio among the towns in this data set is {median_ptratio}.")

# g) Which census tract of Boston has the lowest median value of owner-occupied homes?
lowest_medv_tract = data[data['medv'] == data['medv'].min()]
print("The census tract with the lowest median value of owner-occupied homes:")
print(lowest_medv_tract)
print("The values of the other predictors for that census tract:")
print(lowest_medv_tract.drop('medv', axis=1))
print("Comparing the values to the overall ranges for those predictors can be done using the describe() method.")

# h) In this data set, how many of the census tracts average more than seven rooms per dwelling? More than eight rooms per dwelling?
num_tracts_seven_rooms = len(data[data['rm'] > 7])
num_tracts_eight_rooms = len(data[data['rm'] > 8])
print(f"There are {num_tracts_seven_rooms} census tracts that average more than seven rooms per dwelling.")
print(f"There are {num_tracts_eight_rooms} census tracts that average more than eight rooms per dwelling.")
print("Additional insights on the census tracts can be obtained by examining the specific rows of data.")
