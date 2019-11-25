import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import mean_absolute_error

heart = pd.read_csv('framingham.csv', sep=',', header=0)

def datapreprocessing(heart):
    heart = heart.rename(index=str, columns={'male': 'Gender', 'age': 'Age', 'BPMeds': 'Blood_Pressure_Medication'})

    # Cleaning the data which having NA values by removing the null valued rows
    heart = heart.dropna()
    # Remove duplicate values from the database
    heart = heart.drop_duplicates(subset=['Gender', 'Age', 'currentSmoker', 'cigsPerDay',
                                          'Blood_Pressure_Medication', 'prevalentStroke', 'prevalentHyp',
                                          'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose',
                                          'TenYearCHD'], keep='first')
    # Drop the values which doesn't affect the results
    heart = heart.drop(['education', 'Blood_Pressure_Medication', 'prevalentStroke', 'diabetes', ], axis=1)

    # Normalize the data which in betwenn 0 & 1
    heart['Age'] = (heart['Age'] - heart['Age'].min()) / (heart['Age'].max() - heart['Age'].min())
    heart['cigsPerDay'] = (heart['cigsPerDay'] - heart['cigsPerDay'].min()) / (
                heart['cigsPerDay'].max() - heart['cigsPerDay'].min())
    heart['totChol'] = (heart['totChol'] - heart['totChol'].min()) / (heart['totChol'].max() - heart['totChol'].min())
    heart['sysBP'] = (heart['sysBP'] - heart['sysBP'].min()) / (heart['sysBP'].max() - heart['sysBP'].min())
    heart['diaBP'] = (heart['diaBP'] - heart['diaBP'].min()) / (heart['diaBP'].max() - heart['diaBP'].min())
    heart['BMI'] = (heart['BMI'] - heart['BMI'].min()) / (heart['BMI'].max() - heart['BMI'].min())
    heart['heartRate'] = (heart['heartRate'] - heart['heartRate'].min()) / (
                heart['heartRate'].max() - heart['heartRate'].min())
    heart['glucose'] = (heart['glucose'] - heart['glucose'].min()) / (heart['glucose'].max() - heart['glucose'].min())


heart = datapreprocessing(heart)
input("Enter to continue...!")
