import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

cv_accuracy_df = pd.read_csv('./results/income_cv_scores.csv')
metrics_df = pd.read_csv('./results/income_algorithms.csv')
params_df = pd.read_csv('./results/income_best_params.csv')
algorithm_names = metrics_df["algorithm_name"].to_list()
cv_accuracy_df["algorithm_id"] = cv_accuracy_df["algorithm_id"].apply(
    lambda id: algorithm_names[id-1])
cv_accuracy_df = cv_accuracy_df.drop(len(cv_accuracy_df)-1)


def plot_accuracy():
    """Plot box plot for accuracy
    """    
    sns.set(font_scale=1.2)
    sns.boxplot(x="accuracy_score", y="algorithm_id", data=cv_accuracy_df, orient='h')

    plt.title('accuracy', fontsize=24, pad=40)
    plt.ylabel('algorithm name', fontsize=18, labelpad=40)
    plt.xlabel('accuracy score', fontsize=18, labelpad=40)

    sns.set(rc={'figure.figsize': (100, 200)})
    plt.show()


def plot_cm_metrics(algorithm_id):
    """
       Display confusion matrix and
       get DataFrame with best params for specific algorithm

    Args:
        algorithm_id (str):

    Returns:
        DataFrame: best params for analyzed algorithm
    """    
    results = metrics_df[metrics_df["algorithm_id"]
                         == algorithm_id].iloc[:, 2:]
    best_params = params_df[params_df["algorithm_id"]
                            == algorithm_id].iloc[:, 1:]
    sns.set(rc={'figure.figsize': (8, 6)})
    sns.heatmap([[
        results.iloc[0, -4],
        results.iloc[0, -3]
    ], [
        results.iloc[0, -2],
        results.iloc[0, -1]
    ]], cmap="crest")
    plt.title('confusion matrix', fontsize=24, pad=40)
    return best_params
