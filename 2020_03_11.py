import pandas as pd

friend_dict_list = [
    {'name': 'John', 'age': 25, 'job': 'student'},
    {'name': 'Nate', 'age': 30, 'job': 'teacher'}
    ]
df = pd.DataFrame(friend_dict_list)
print(df.head())
