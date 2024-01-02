import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor


def main():
    pass


def plot_top_n_importance(DataFrame, model, top_n):
    """
    Display the top N feature importances of a model.

    Arguments:
    DataFrame (pd.DataFrame): The dataframe used to train the model.
    model: The trained model with feature importance attribute.
    top_n (int): Number of top features to display.

    Returns:
    None. Displays a plot of top N feature importances.
    """
    # Extract feature importances
    feature_importances = model.feature_importances_

    # Create a series with feature importances
    feature_importances = pd.Series(feature_importances, index=DataFrame.columns)

    # Sort and select the top N importances
    importances_sorted = feature_importances.sort_values(ascending=False)[:top_n]

    # Plot the top N feature importances
    plt.figure(figsize=(10, top_n * 0.5))  # Adjust the size based on number of features
    importances_sorted.plot(kind="barh", color="skyblue")
    plt.title(f"Top {top_n} Feature Importances")
    plt.show()


if __name__ == "__main__":
    main()
