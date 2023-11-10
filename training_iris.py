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
plt.xlabel('features')
plt.ylabel('target')
plt.show()