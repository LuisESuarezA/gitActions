import pandas as pd

# Create a dictionary with the data
data = {
    'name': ['Lion', 'Tiger', 'Elephant', 'Giraffe'],
    'number_of_animals': [3, 2, 5, 4],
    'age': [10, 8, 15, 12]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
