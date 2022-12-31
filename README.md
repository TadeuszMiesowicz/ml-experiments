# ml-experiments

## comparison of binary classification algorithms 

A *test of performance* of ML algorithms for *binary* classification.
The code associated with the training of each algorithm can be accessed in the algorithms folder.

Algorithm are trained on Census Income Data Set

[data set](https://archive-beta.ics.uci.edu/dataset/2/adult)

#### Data set description:

Predict whether income exceeds $50K/yr based on census data. Also known as "Census Income" dataset.


My ML training results are similar to Baseline Model Performance:
[data set](https://archive-beta.ics.uci.edu/dataset/2/adult)

also in my ML training *xgboost* has the best accuracy

#### SQL database & static site generation

Each time changes are added to the main branch of this repository github action: 
rebuilds a small postgres SQL database containing the training results.

Webpage `miesowicz.com` makes use of data from database for SSG (static site generation) with [SvelteKit](https://kit.svelte.dev/) .


#### www with comparison results

Charts and a summary of the training results also can be found on
[miesowicz.com/ml-performance](https://miesowicz.com/ml-performance)

---

### Start here

[start](./index.ipynb)
