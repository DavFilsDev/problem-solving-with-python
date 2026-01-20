# Linear Regression from scratch using Gradient Descent
# This file is for learning ML fundamentals (no libraries)

import random

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = random.random()
        self.b = random.random()

    def predict(self, x):
        return self.w * x + self.b

    def train(self, X, y):
        n = len(X)

        for _ in range(self.epochs):
            dw = 0
            db = 0

            for xi, yi in zip(X, y):
                y_pred = self.predict(xi)
                error = y_pred - yi

                dw += error * xi
                db += error

            self.w -= self.lr * (dw / n)
            self.b -= self.lr * (db / n)

    def evaluate(self, X, y):
        mse = 0
        for xi, yi in zip(X, y):
            mse += (self.predict(xi) - yi) ** 2
        return mse / len(X)


# 🔍 Test the algorithm
if __name__ == "__main__":
    # Sample data (y = 2x + 1)
    X = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]

    model = LinearRegression()
    model.train(X, y)

    print("Weight:", model.w)
    print("Bias:", model.b)
    print("MSE:", model.evaluate(X, y))
