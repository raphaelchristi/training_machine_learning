from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Carrega o conjunto de dados Iris
iris = datasets.load_iris()
irs = pd.DataFrame(iris.data, columns=iris.feature_names)

irs['class'] = iris.target

# Divide o conjunto de dados em features (x) e rótulos (y)
x = irs.iloc[:, :-1].values
y = irs.iloc[:, 4].values

# Divide os dados em conjuntos de treinamento e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Padroniza os dados
sc = StandardScaler()
sc.fit(x_train)

x_train = sc.transform(x_train)
x_test = sc.transform(x_test)

# Verifica se o modelo já foi treinado anteriormente
try:
    # Tenta carregar o modelo treinado
    classifier = joblib.load('knn_model.joblib')
    print("Modelo carregado com sucesso.")
except FileNotFoundError:
    # Se o modelo não existir, cria e treina um novo
    classifier = KNeighborsClassifier(n_neighbors=8)
    classifier.fit(x_train, y_train)
    joblib.dump(classifier, 'knn_model.joblib')
    print("Modelo treinado e salvo com sucesso.")

# Realiza a previsão no conjunto de teste
y_pred = classifier.predict(x_test)

# Avalia o desempenho do modelo
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print("Matriz de Confusão:\n", cm)
print('\n\nRelatório de Classificação:\n', cr)

# Solicita o input do usuário para classificação
print("\nDigite os valores do novo input:")
new_input = []
for i in range(4):
    value = float(input(f"Valor {i + 1}: "))
    new_input.append(value)

# Converte e padroniza o novo input
new_input = [new_input]
new_input_scaled = sc.transform(new_input)

# Realiza a previsão para o novo input
predicted_class = int(classifier.predict(new_input_scaled)[0])
class_name = iris.target_names[predicted_class]

# Exibe a classe prevista para o novo input
print("\nClasse prevista para o novo input:", class_name)
