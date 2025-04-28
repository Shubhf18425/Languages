import pandas as pd 
import numpy as np

df = {"name" : ["shubh" , "Agarwal" , "Dinar"],
    "Age" : [18 , 20 , 19],
    "Income" : [1000 , 2000 , 3000],
    "City" : ["Delhi", "Mumbai", "Bangalore"],
}

f = pd.DataFrame(df)
print(f)

# print(f.ndim)  # number of dimensions

# print(f.shape) # dimension of the datagrame

# print(type(f["name"]))

# print(type(f.City))

# print(f.name.dtype)

# print(f["Age"])


# print(f["Age"])
# f["Age"] = f["Age"].astype("str")
# f["Age"] = f["Age"].astype(float)
# print(f["Age"])

# print(f["Income"][0])

# for i in range(len(f)):
#     f["Income"][i] = f["Income"][i] + 1000
# print(f)

# print(f.columns)

# print(f["Age"].max())
# print(f["Income"].min())
# print(f["Age"].mean())
# print(f["Income"].sum())
# print(f["Age"].median())
# print(f["Income"].std())
# print(f["Age"].var())
# print(f["Income"].count())
# print(f["Age"].describe())
# print(f["Income"].describe())

print(np.percentile(f["Age"], 50)) # 50th percentile
print(np.percentile(f["Income"], 50)) # 50th percentile


