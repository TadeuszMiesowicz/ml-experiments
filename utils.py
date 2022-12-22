import seaborn as sns
import mplcyberpunk
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("cyberpunk")

cv_accuracy_df = pd.read_csv('./results/income_cv_scores.csv')
metrics_df = pd.read_csv('./results/income_algorithms.csv')
params_df = pd.read_csv('./results/income_best_params.csv')
algorithm_names = metrics_df["algorithm_name"].to_list()


def plot_accuracy():
    sns.set(font_scale=1.2)

    sns.boxplot(x=cv_accuracy_df["accuracy_score"], y=cv_accuracy_df["algorithm_id"].apply(
        lambda id: algorithm_names[id-1]), orient='h')

    plt.title('accuracy', fontsize=24, pad=40)
    plt.ylabel('algorithm name', fontsize=18, labelpad=40)
    plt.xlabel('accuracy score', fontsize=18, labelpad=40)

    sns.set(rc={'figure.figsize': (18, 10)})
    plt.show()


def plot_cm_metrics(algorithm_id):
    results = metrics_df[metrics_df["algorithm_id"] == algorithm_id].iloc[:, 2:]
    best_params = params_df[params_df["algorithm_id"] == algorithm_id].iloc[:, 1:]
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
