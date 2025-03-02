import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Study hours (X) and Exam scores (y) - Showing a non-linear trend
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([50, 55, 65, 75, 85, 90, 92, 93, 94, 94])  # Notice it slows down

# Convert X to polynomial features (degree=2 for quadratic curve)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Generate smooth curve points
X_test = np.linspace(1, 10, 100).reshape(-1, 1)
X_test_poly = poly.transform(X_test)
y_pred = model.predict(X_test_poly)

# Plot data points
plt.scatter(X, y, color='blue', label='Data Points')

# Plot polynomial regression curve
plt.plot(X_test, y_pred, color='red', label='Polynomial Regression Curve')

# Labels and title
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Polynomial Regression (Curved Line)')
plt.legend()
plt.show()
