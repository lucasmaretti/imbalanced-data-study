import matplotlib.pyplot as plt

def analyze_target_distribution(df, target_variable):
    """
    Analyze the distribution of a target variable in a dataset.
    
    Parameters:
    df (pandas.DataFrame): The dataset.
    target_variable (str): The name of the target variable.
    """
    # Calculate the percentage of each category in the target variable
    target_counts = df[target_variable].value_counts()
    target_percentages = target_counts / len(df) * 100

    # Print the percentage of each category
    print(f"Percentage of each category in '{target_variable}':")
    for category, percentage in target_percentages.items():
        print(f"{category}: {percentage:.2f}%")

    # Generate a bar plot of the target variable
    plt.figure(figsize=(8, 6))
    target_counts.plot(kind='bar', color=['skyblue', 'salmon'])
    plt.title(f'{target_variable} Distribution')
    plt.xlabel(target_variable)
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()