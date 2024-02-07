import numpy as np


X = np.array([[1, 2], [3, 4], [5, 6]])  
y = np.array([3, 4, 5])  
theta = np.array([0.1, 0.2])  
lambda_ = 0.1  


def compute_cost(X, y, theta, lambda_):
    m = len(y)
    h_theta = np.dot(X, theta)
    error = h_theta - y
    cost = (1/(2*m)) * (np.sum(np.square(error)) + lambda_ * np.sum(np.square(theta)))
    return cost


cost = compute_cost(X, y, theta, lambda_)
print("Cost:", cost)
