import numpy as np
from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def generate_nand_data(num_samples):
    X = np.random.randint(0, 2, (num_samples, 5))
    y = np.array([int(not np.all(row)) for row in X])
    return X, y


# Implemente o KNN(com distancia euclidiana) para a porta NAND com 5 entradas fazendo a validação hold-out com 90% treinamento e 10% para testes?
# PS: Ache o melhor k possível para o KNN.

X, y = generate_nand_data(
1000
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
knn_and = KNeighborsClassifier(n_neighbors= 7, metric='euclidean')
knn_and.fit(X_train, y_train)


print(100 * "-")
print("Nand")
print(100 * "-")

y_pred = knn_and.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['class 0', 'class 1']))


#  Implemente o KNN( com a distancia de  manhattan)  para a porta XOR com 4 entradas fazendo a validação hold-out com 80%
# treinamento e 20% para testes?
# PS: Ache o melhor k possível para o KNN.

def generate_xor_data(num_samples):
    X = np.random.randint(0, 2, (num_samples, 4))
    y = np.array([int(np.sum(row) % 2) for row in X])
    return X, y

X_xor, y_xor = generate_xor_data(1000)


X_xor_train, X_xor_test, y_xor_train, y_xor_test, = train_test_split( X_xor, y_xor, test_size=0.2, random_state=42)

knn_xor = KNeighborsClassifier(n_neighbors=5, metric='manhattan')

knn_xor.fit(X_xor_train, y_xor_train)


print(100 * "-")
print("Xor")
print(100 * "-")
y_xor_predy_pred = knn_xor.predict(X_xor_test)
print(classification_report(y_xor_test, y_xor_predy_pred, target_names=['class 0', 'class 1']))