from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn import datasets
from pprint import PrettyPrinter
import numpy as np


def classify(x, y):
    clf = LogisticRegression(random_state=12)
    scores = []
    kf = KFold(len(y), n_folds=10)

    for train,test in kf:
      clf.fit(x[train], y[train])
      scores.append(clf.score(x[test], y[test]))
    PrettyPrinter().pprint(scores)
    print np.mean(scores)
    print

rain = np.load('rain.npy')
dates = np.load('doy.npy')

x = np.vstack((dates[:-1], rain[:-1]))
y = np.sign(rain[1:])
classify(x.T, y)

#iris example
iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target
classify(x, y)
