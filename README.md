# ml-experiments

## binary classification algorithms comparison

A *test of performance* of ML algorithms for *binary* classification.
The code associated with the training of each algorithm can be accessed in the algorithms folder.

Algorithm are trained on Census Income Data Set

[data set](https://archive-beta.ics.uci.edu/dataset/2/adult)

#### Data set description:

Predict whether income exceeds $50K/yr based on census data. Also known as "Census Income" dataset.


My test results are similar to Baseline Model Performance:
[data set](https://archive-beta.ics.uci.edu/dataset/2/adult)

*xgboost* also has the best accuracy in my tests

#### SQL database 

Each time changes are added to the main branch of this repository, github action: 
- rebuilds a small postgres SQL database containing the test results.

#### Static site generation SSG with comparison results

Page `miesowicz.com` is generated ([SvelteKit](https://kit.svelte.dev/) with SSG - static site generation) using data from created database.

Charts and a summary of the tests can be found:
[miesowicz.com/binary-test](https://miesowicz.com/binary-test)

---

### Start here

[start](./index.ipynb)
