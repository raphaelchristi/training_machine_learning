from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
features = iris.data[:,[0,1,2,3]] #seleciona as colunas do dataset
target = iris.target
featuresAll = []

for observation in features:
    featuresAll.append(observation[0] + observation[1] + observation[2] + observation[3])

plt.scatter(featuresAll, target, c='blue', alpha=1.0)
plt.rcParams['figure.figsize'] = (10, 8)
plt.title('Iris Dataset')
plt.xlabel('Features')
plt.ylabel('Targets')
plt.show()

sepal_length = []
sepal_width = []
petal_length = []
petal_width = []
for feature in features:
    sepal_length.append(feature[0])
    sepal_width.append(feature[1])
for feature in features:
    petal_length.append(feature[2])
    petal_width.append(feature[3])

groups = ['setosa','versicolor', 'virginica']
colors = ['red', 'blue', 'green']
data = [(sepal_length[:50], sepal_width[:50]), (sepal_length[50:100], sepal_width[50:100]), (sepal_length[100:150] , sepal_width[100:150])]
data2 = [(petal_length[:50], petal_width[:50]), (petal_length[50:100], petal_width[50:100]), (petal_length[100:150] , petal_width[100:150])]

for item, color, group in zip(data, colors, groups):
    x0,y0 = item
    plt.scatter(x0, y0, c=color, alpha=1.0)
    plt.title('Iris Dataset')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

for item, color, group in zip(data2, colors, groups):
    x0,y0 = item
    plt.scatter(x0, y0, c=color, alpha=1.0)
    plt.title('Iris Dataset')

plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
