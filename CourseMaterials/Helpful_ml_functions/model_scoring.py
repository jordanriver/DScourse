import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def main():
    pass


def feature_selection_score(
    n_features, importance_frame, X_train_frame, y_train, X_test_frame, y_test, base_mse
):
    """A function that calculates MSE scores from models with number of features in the range of n_features.
    These scores are assigned to a MSE list. The function also calculates score differences from a score of a base model
    and assigns them to a second list. Both lists are returned as a dictionary with the following keys:
    'mse_list', 'mse_differences'.
    """
    mse_list = []
    mse_differences = []

    # Create a new RF model
    rf_enhanced_model = RandomForestRegressor(random_state=42)

    for n in n_features:
        # Choose the n most important features from feature_importance_sorted
        chosen_features = importance_frame.head(n).index

        # Define the new X_train to fit the model with the top n features
        X_train_new = X_train_frame[chosen_features]

        # Train the model
        rf_enhanced_model.fit(X_train_new, y_train)

        # Define the new X_test to predict the target with the top n features
        X_test_new = X_test_frame[chosen_features]

        # Predict via X_test_new
        y_pred_enhanced = rf_enhanced_model.predict(X_test_new)

        # Calculate score for model
        mse_enhanced = mean_squared_error(y_pred=y_pred_enhanced, y_true=y_test)
        mse_difference = base_mse - mse_enhanced
        mse_list.append(mse_enhanced)
        mse_differences.append(mse_difference)
    return {"mse_list": mse_list, "mse_differences": mse_differences}


if __name__ == "__main__":
    main()
