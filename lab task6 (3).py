import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ram", "Shyam", "Hari", "Sita"]
})

df2 = pd.DataFrame({
    "ID": [3, 4, 5, 6],
    "Marks": [75, 85, 90, 80]
})

print("Inner Join:")
print(pd.merge(df1, df2, on="ID", how="inner"))

print("Left Join:")
print(pd.merge(df1, df2, on="ID", how="left"))

print("Right Join:")
print(pd.merge(df1, df2, on="ID", how="right"))

print("Outer Join:")
print(pd.merge(df1, df2, on="ID", how="outer"))