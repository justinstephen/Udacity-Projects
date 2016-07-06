from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy

def compute_fraction( poi_messages, all_messages ):
    if poi_messages == 'NaN':
        fraction = 0.
    elif all_messages == 'NaN':
        fraction = 0.
    else: 
        fraction = float(poi_messages) / float(all_messages)
    return fraction
	
def feature_selection(clf, features_list, data):
	data = featureFormat(data, features_list, sort_keys = True)
	labels, features = targetFeatureSplit(data)
	clf = clf.fit(features, labels)
	feature_importances = clf.feature_importances_
	pred = clf.predict(features)
	feature_weights = clf.feature_importances_
	feature_rank = dict(zip(features_list[1:], feature_weights))
	features_list = ['poi'] + {key:value for key, value in feature_rank.items() if value > 0.1}.keys()
	return features_list
	
def test_classifier(clf, dataset, feature_list, scaling = False, folds = 1000):
    score_all = []
    precision_all = []
    recall_all = []
    
    data = featureFormat(dataset, feature_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    
    if scaling == True:
        min_max_scaler = preprocessing.MinMaxScaler()
        features = min_max_scaler.fit_transform(features)
		
    cv = StratifiedShuffleSplit(labels, folds, random_state = 42)
    for train_indices, test_indices in cv: 
        features_train= [features[ii] for ii in train_indices]
        features_test= [features[ii] for ii in test_indices]
        labels_train=[labels[ii] for ii in train_indices]
        labels_test=[labels[ii] for ii in test_indices]
        
        clf.fit(features_train, labels_train)
        pred = clf.predict(features_test)
        score_all.append(clf.score(features_test,labels_test))
        precision_all.append(precision_score(labels_test,pred))
        recall_all.append(recall_score(labels_test,pred))

    precision = numpy.average(precision_all)
    recall = numpy.average(recall_all)
    score = numpy.average(score_all)
        
    print "Score: " + str(score)
    print "Recall: " + str(precision)
    print "Precision: " + str(recall)	
	
def test_features(clf, features_list, data, tests):
    count = 0
    while count < tests:
        count = count + 1
        features_list = feature_selection(clf, features_list, data)
        print features_list
    return features_list