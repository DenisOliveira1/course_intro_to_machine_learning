#!/usr/bin/python


def mySort(val):
    return val[2]


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    outliers_amount = len(predictions)*0.1
    for i in range(len(predictions)):
        cleaned_data.append([ages[i],net_worths[i],predictions[i]-net_worths[i]])
    cleaned_data.sort(key = mySort)
    return cleaned_data[:int(len(predictions)-outliers_amount)]

