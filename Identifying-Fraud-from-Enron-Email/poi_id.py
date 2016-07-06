#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from enron_functions import compute_fraction, feature_selection, test_classifier, test_features
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn.cross_validation import StratifiedShuffleSplit
import numpy


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
### features_list = ['poi','salary'] # You will need to use more features

financial_features = 	['salary', 
						'deferral_payments', 
						'total_payments', 
						'loan_advances', 'bonus', 
						'restricted_stock_deferred', 
						'deferred_income', 
						'total_stock_value', 
						'expenses', 
						'exercised_stock_options', 
						'long_term_incentive', 
						'restricted_stock', 
						'director_fees']
						
email_features = 		['to_messages',
						'from_poi_to_this_person', 
						'from_messages', 
						'from_this_person_to_poi', 
						'shared_receipt_with_poi']

poi_label = ['poi']

features_list = poi_label + financial_features + email_features

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )
my_dataset = data_dict

print len(my_dataset.keys())
print len(my_dataset.values()[0])

### Task 2: Remove outliers
outliers = ['THE TRAVEL AGENCY IN THE PARK', 'TOTAL']

for key in outliers:
    my_dataset.pop(key, None)
	
	
### Testing different classifiers
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#Decision Tree
from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=6)
print "Decision Tree Classifier:"
print test_classifier(clf, my_dataset, features_list, scaling = True)

#GaussianNB 
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
print "Naive Bayes: "
print test_classifier(clf, my_dataset, features_list, scaling = True)

#SVC
from sklearn.svm import SVC

clf = SVC(kernel="rbf", C=10)
print "SVC: "
print test_classifier(clf, my_dataset, features_list, scaling = True)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
new_features = ['fraction_from_poi', 'fraction_to_poi']
features_list = features_list + new_features

for name in data_dict:
    data_point = my_dataset[name]
    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = compute_fraction( from_poi_to_this_person, to_messages )
    data_point["fraction_from_poi"] = fraction_from_poi
    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = compute_fraction( from_this_person_to_poi, from_messages )
    data_point["fraction_to_poi"] = fraction_to_poi

###Test DecisionTreeClassifier again with new features:
clf = tree.DecisionTreeClassifier(min_samples_split=6)
print "Decision Tree Classifier with new features:"
print test_classifier(clf, my_dataset, features_list)


### Using feature selection in a decision tree model
features_list = poi_label + financial_features + email_features + ['fraction_from_poi', 'fraction_to_poi']
clf = tree.DecisionTreeClassifier(min_samples_split=6)
features_list = test_features(clf, features_list, my_dataset, 10)

#Testing Decision Tree with reduced features:
clf = tree.DecisionTreeClassifier(min_samples_split=6)
print "Decision Tree Classifier with reduced features:"
print test_classifier(clf, my_dataset, features_list)

### Optimizing parameters
from time import time
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation
from sklearn.metrics import classification_report

print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'max_features': ['auto', 'sqrt', 'log2'],
              'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10],
              'max_depth' : [None, 2, 4, 6, 8, 10]}
cv = cross_validation.StratifiedShuffleSplit(labels,n_iter = 50,random_state = 42)			  
clf = GridSearchCV(tree.DecisionTreeClassifier(), param_grid, cv = cv, scoring='recall')
clf = clf.fit(features, labels)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
	
#Decision Tree with new parameters:	
clf = clf.best_estimator_
print test_classifier(clf, my_dataset, features_list, scaling = True)
print clf

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)