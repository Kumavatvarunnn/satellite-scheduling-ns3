from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Sample data: [latency in ms, packet size in bytes]
data = np.array([[100, 200], [150, 250], [200, 300], [250, 350], [300, 400]])

# Labels: actual latency
latency = np.array([100, 150, 200, 250, 300])

# Train a Linear Regression model
model = LinearRegression()
model.fit(data, latency)

# Predict latency for a new packet size
new_packet = np.array([[350, 450]])
predicted_latency = model.predict(new_packet)
print(f"Predicted latency: {predicted_latency[0]} ms")

# Visualize the data and prediction
plt.scatter(data[:, 0], latency, color='blue')
plt.plot(data[:, 0], model.predict(data), color='red')
plt.title("Latency Prediction")
plt.xlabel("Packet Size (bytes)")
plt.ylabel("Latency (ms)")
plt.show()
