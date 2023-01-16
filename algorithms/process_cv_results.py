from const import N_SPLITS
import pandas as pd
import numpy as np
import re
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, roc_auc_score


def remove_algorithm_name(algorithm_name, str):
    """remove algorithm name from string

    Args:
        algorithm_name (str):
        str (str):

    Returns:
        str
    """
    return re.sub(f"{algorithm_name}", "", str)


def process_cv_scores(cv, algorithm_id):
    scores = np.empty(0)

    for splitIndex in range(N_SPLITS):
        scores = np.append(
            scores,
            cv.cv_results_[f"split{splitIndex}_test_score"])

    scores_len = len(scores)

    algorithm_codes = [algorithm_id for x in range(scores_len)]

    return pd.DataFrame(list(zip(algorithm_codes, scores)),
                        columns=[
        "algorithm_id",
        "accuracy_score"
    ])


def process_best_params(cv, algorithm_id, algorithm_name):
    best_params = dict()

    for key, value in cv.best_params_.items():
        best_params[remove_algorithm_name(
            f"{algorithm_name}__", key)] = str(value)

    best_params_len = len(best_params.values())

    algorithm_codes = [algorithm_id for x in range(best_params_len)]

    return pd.DataFrame(zip(algorithm_codes, best_params.keys(), best_params.values()), columns=[
        "algorithm_id",
        "hyperparameter_name",
        "best_value"
    ])


def get_classification_metrics(y_test, y_pred, cv, algorithm_id, algorithm_name):
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print("\n---")
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred, output_dict=True)
    cr = pd.DataFrame(cr).transpose()
    cr.head()

    return pd.DataFrame({
        'algorithm_id': algorithm_id,
        'algorithm_name': algorithm_name,
        'best_accuracy': cv.best_score_,
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'roc_auc_score': roc_auc_score(y_test, y_pred),
        'true_positives': [cm[0, 0]],
        'false_positives': [cm[0, 1]],
        'false_negatives': [cm[1, 0]],
        'true_negatives': [cm[1, 1]]
    })


def save_results(dfs, algorithm_id):
    file_names = ['income_cv_scores.csv', 'income_best_params.csv',
                  'income_algorithms.csv']
    for index, file_name in enumerate(file_names):
        df = pd.read_csv(f'./{file_name}')
        df = df[df["algorithm_id"] != algorithm_id]
        df = pd.concat([df, dfs[index]])
        print(df.head())


def results_to_csv(dfs, algorithm_id):
    file_names = ['income_cv_scores.csv', 'income_best_params.csv',
                  'income_algorithms.csv']
    for index, file_name in enumerate(file_names):
        path = f'../results/{file_name}'
        df = pd.read_csv(path)
        df = df[df["algorithm_id"] != algorithm_id]
        df = pd.concat([df, dfs[index]], ignore_index=True)
        df = df.sort_values(by=["algorithm_id"])
        df.to_csv(path, index=False)
