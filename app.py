import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample student data
students = ["Aman", "Sara", "John", "Riya", "Ali"]

# Generate random marks using numpy
marks = np.random.randint(60, 100, size=5)

# Create DataFrame using pandas
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

# Print data
print(df)

# Plot graph using matplotlib
plt.bar(df["Student"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

# Save graph image
plt.savefig("marks_chart.png")

print("Chart saved as marks_chart.png")