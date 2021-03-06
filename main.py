# https://scikit-learn.org/stable/modules/neural_networks_supervised.html
from sklearn.neural_network import MLPClassifier

X = [[0., 0.], [1., 1.]]
y= [0, 1]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 6), random_state=1)
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 36), random_state=1)

clf.fit(X, y)
clf.predict([[2., 2.], [-1., -2.]])
