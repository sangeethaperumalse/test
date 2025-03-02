import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Study hours (independent variable X)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Exam scores (dependent variable y)
y = np.array([60, 70, 75, 85, 90])

# Create a Linear Regression model
model = LinearRegression()

# Train (fit) the model using X and y
model.fit(X, y)

# Get the slope (m)
m = model.coef_[0]

# Get the intercept (b)
b = model.intercept_

print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")

# Predict the exam score for 6 hours of study
predicted_score = model.predict([[6]])
print(f"Predicted Score for 6 hours: {predicted_score[0]:.2f}")

# Plotting the data and the regression line
plt.scatter(X, y, color='blue', label='Data Points')  # Plot the original data
plt.plot(X, model.predict(X), color='red', label='Regression Line')  # Plot the regression line
plt.xlabel('Study Hours')  # X-axis label
plt.ylabel('Exam Score')  # Y-axis label
plt.title('Linear Regression: Study Hours vs Exam Score')  # Title of the plot
plt.legend()  # Display the legend
plt.show()  # Display the plot
