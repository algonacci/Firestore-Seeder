import pandas as pd
from datetime import datetime
import uuid

# Read the CSV file
df = pd.read_csv("terra_market.csv")

# Fill null values in 'createdAt' and 'updatedAt' columns with current timestamp
current_time = datetime.now()
df['createdAt'].fillna(current_time, inplace=True)
df['updatedAt'].fillna(current_time, inplace=True)

# Generate document IDs
df['id'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Print the updated DataFrame
print(df)

