import pandas as pd
import cudf
from sklearn.model_selection import train_test_split

train_data = pd.read_csv("train_data_GPU.csv")
train_data.drop(columns=['UserId', 'ProductId', 'Time', 'Likes', 'Dislikes'], inplace=True)

                                  
print("done")

train_data.head()