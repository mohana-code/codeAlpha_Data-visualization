import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Year': [2020, 2021, 2022, 2023],
    'Sales': [200, 300, 250, 400]
}

df = pd.DataFrame(data)

plt.plot(df['Year'], df['Sales'])
plt.title("Sales Data Visualization")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()