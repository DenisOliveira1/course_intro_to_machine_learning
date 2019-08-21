#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "The dataset has:", len(enron_data), "pessoas"
print "Cada pessoa contem:", len(enron_data["SKILLING JEFFREY K"]), "atributos"

poi = 0
for i in enron_data:
    if enron_data[i]["poi"] == 1:   
        poi = poi + 1
print "There are:",poi,"poi's"

print "James Pretice total_stock_value",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Wesley from_this_person_to_poi:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Jeffrey K Skilling exercised_stock_options:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Kenneth L Lay total_payments:",enron_data["LAY KENNETH L"]["total_payments"]
print "Jeffrey K Skilling total_payments:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Andrw S Fastow total_payments:", enron_data["FASTOW ANDREW S"]["total_payments"]

known_salary = 0
known_email = 0
for i in enron_data:
    if enron_data[i]["email_address"] != "NaN":
        known_email = known_email + 1
    if enron_data[i]["salary"] != "NaN":
        known_salary = known_salary + 1
print "known_salary:", known_salary
print "known_email:", known_email

unknown_total_payments = 0
for i in enron_data:
    if enron_data[i]["total_payments"] == "NaN":
        unknown_total_payments = unknown_total_payments + 1
print "unknown_total_payments porcentage:", 100*unknown_total_payments/len(enron_data),"%"

poi_unknown_total_payments = 0
for i in enron_data:
    if enron_data[i]["poi"]:
        if enron_data[i]["total_payments"] == "NaN":
            poi_unknown_total_payments = poi_unknown_total_payments + 1
print "poi_unknown_total_payments porcentage:", 100*poi_unknown_total_payments/poi,"%"

print "new dataset size:", len(enron_data)+10
print "new unknown_total_payments:", unknown_total_payments+10

print "new poi size:", poi+10
print "new poi_unknown_total_payments:", poi_unknown_total_payments+10

print "new poi_unknown_total_payments porcentage:", 100*(poi_unknown_total_payments+10)/(poi+10),"%"


        
