from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_regression(y_true, preds):
    rmse = np.sqrt(mean_squared_error(y_true, preds))
    r2 = r2_score(y_true, preds)

    return {
        "RMSE": rmse,
        "R2": r2
    }