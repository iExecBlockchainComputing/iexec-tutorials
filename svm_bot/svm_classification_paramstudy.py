
import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.metrics import classification_report
import csv

dir=sys.argv[1];
idx=sys.argv[2];

def extract_param(_idx):
      with open('parameters.csv', newline='') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=';')
          rows =list(spamreader)
          kernel, gamma = rows[_idx]
          return kernel, gamma

kernel,_gamma = extract_param(int(idx))

if kernel not in  "linear" "rbf" "poly":
    print ("error for kernel:", kernel )
    exit(1);

if ((int(_gamma) >= 15) or (int(_gamma) <= 5)):
    print ("error for gamma:", _gamma )
    exit(1);


print("running tasks " + idx + " of the bag of task")


iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 0, :2]
y = y[y != 0]

n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)

X_train = X[:int(.9 * n_sample)]
y_train = y[:int(.9 * n_sample)]
X_test = X[int(.9 * n_sample):]
y_test = y[int(.9 * n_sample):]

# fit the model
#for kernel in ('linear', 'rbf', 'poly'):

clf = svm.SVC(kernel=kernel, gamma=float(_gamma))
clf.fit(X_train, y_train)

plt.figure()
plt.clf()
plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired,
            edgecolor='k', s=20)

    # Circle out the test data
plt.scatter(X_test[:, 0], X_test[:, 1], s=80, facecolors='none',
            zorder=10, edgecolor='k')

plt.axis('tight')
x_min = X[:, 0].min()
x_max = X[:, 0].max()
y_min = X[:, 1].min()
y_max = X[:, 1].max()

XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
# Put the result into a color plot

Z = Z.reshape(XX.shape)
plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
             linestyles=['--', '-', '--'], levels=[-.5, 0, .5])


filename='image_kerneltype_' + kernel + '_gammavalue_' + str(_gamma)
plt.title(filename)
plt.savefig(dir + '/' + filename)

y_true, y_pred = y_test, clf.predict(X_test);
print('kernel: ' + kernel + ' gamma: '+ _gamma)
print(classification_report(y_true, y_pred))
