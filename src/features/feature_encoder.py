from sklearn.preprocessing import LabelEncoder


class LabelEncoderWrapper:
    def __init__(self):
        self.label_encoders = {}

    def fit_transform(self, df, cols):
        # Encode categorical features and store encoders
        for column in cols:
            if column in df.columns:
                le = LabelEncoder()  # Initialize a LabelEncoder for the current column
                df[column] = le.fit_transform(df[column].astype(str))  # Fit and transform the column, updating the DataFrame
                self.label_encoders[column] = le  # Store the encoder in the dictionary with the column name as the key
            else:
                print(f"Warning: Column {column} not found in DataFrame.")
        return df

    def inverse_transform(self, df):
        # Reverse transform categorical features using stored encoders
        for column, le in self.label_encoders.items():
            if column in df.columns:
                df[column] = le.inverse_transform(df[column])
            else:
                print(f"Warning: Column {column} not found in DataFrame.")
        return df