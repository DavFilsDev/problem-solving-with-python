# k-Nearest Neighbors (kNN) - very simple version
# No ML libraries, pure Python

def knn_predict(data, labels, x, k=3):
    # Calculer la distance (ici distance absolue)
    distances = []

    for xi, label in zip(data, labels):
        distance = abs(xi - x)
        distances.append((distance, label))

    # Trier par distance
    distances.sort(key=lambda item: item[0])

    # Prendre les k plus proches
    k_nearest = distances[:k]

    # Vote majoritaire
    votes = {}
    for _, label in k_nearest:
        votes[label] = votes.get(label, 0) + 1

    return max(votes, key=votes.get)


# 🔍 Test simple
if __name__ == "__main__":
    data = [1, 2, 4, 5]
    labels = [0, 0, 1, 1]

    x = 3
    prediction = knn_predict(data, labels, x, k=3)

    print(f"Prediction for {x}:", prediction)
