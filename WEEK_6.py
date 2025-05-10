import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array and calculate the mean
print("Task 1: NumPy Operations")
print("-" * 40)
numbers = np.array(range(1, 11))  # Create array of numbers 1-10
print(f"NumPy array: {numbers}")
mean_value = np.mean(numbers)
print(f"Mean value: {mean_value}")
print()

# Task 2: Load data into pandas DataFrame and display summary statistics
print("Task 2: Pandas DataFrame Operations")
print("-" * 40)
# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [72000, 68000, 54000, 85000, 76000],
    'Experience': [2, 5, 1, 8, 4]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print()

# Task 3: Fetch data from a public API
print("Task 3: API Request")
print("-" * 40)
try:
    response = requests.get('https://api.github.com/events')
    if response.status_code == 200:
        api_data = response.json()
        print(f"Random API Information: {api_data['entries'][0]['API']} - {api_data['entries'][0]['Description']}")
    else:
        print(f"API request failed with status code: {response.status_code}")
except Exception as e:
    print(f"Error fetching API data: {e}")
print()

# Task 4: Plot a simple line graph
print("Task 4: Matplotlib Visualization")
print("-" * 40)
x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', label='sin(x)')
plt.title('Simple Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()
plt.savefig('sine_wave.png')
print("Sine wave plot has been generated and saved as 'sine_wave.png'")