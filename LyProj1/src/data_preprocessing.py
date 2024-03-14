from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd

# data = pd.read_csv('E:/LyProj1/data/processed/feature_engineered.csv')
# print(data)

def data_prepro(data):
    # Define the columns to include in the transformation
    columns_to_transform = ['SMA_20', 'EMA_30', 'RSI' , 'OBV' ,'Adj Close']  # Specify the column names you want to include

    # Group the data by 'company_name'
    grouped_data = data.groupby('company_name')

    # Define the pipeline steps as tuples
    steps = [
        ('imputer', IterativeImputer(max_iter=10, random_state=0)),
        ('scaler', StandardScaler())
    ]

    # Create the pipeline
    pipeline = Pipeline(steps)

    # Create an empty DataFrame to store the transformed data
    transformed_data = pd.DataFrame()

    # Iterate over groups and transform the data
    for group_name, group_data in grouped_data:
        # Select only the columns to include in the transformation
        group_data_subset = group_data[columns_to_transform]
        
        # Fit and transform the pipeline on the selected columns of the group
        transformed_group = pipeline.fit_transform(group_data_subset)
        
        # Convert the transformed data back to a DataFrame
        transformed_group_df = pd.DataFrame(transformed_group, columns=columns_to_transform, index=group_data_subset.index)
        
        # Add the non-transformed columns back to the transformed group
        for col in group_data.columns:
            if col not in columns_to_transform:
                transformed_group_df[col] = group_data[col]
        
        # Concatenate transformed group with the overall transformed data
        transformed_data = pd.concat([transformed_data, transformed_group_df])

    # Display the transformed data
    transformed_data.index = transformed_data['Date']
    transformed_data.drop(columns=['Date','buy_signal', 'sell_signal', 'EMA_10', 'EMA_50'],inplace = True,axis = 1)
    print(transformed_data)
    transformed_data = transformed_data.rename(columns = {'SMA_20':'SMA','EMA_30' :'EMA'})
    print(transformed_data.columns)
    
    # FINAL RETURN 
    return transformed_data

