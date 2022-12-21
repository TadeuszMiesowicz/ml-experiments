
-- @block
CREATE TABLE income_algorithms(
    id INT NOT NULL,
    algorithm_name VARCHAR(255) NOT NULL,
    best_accuracy FLOAT NOT NULL,
    algorithm_precision FLOAT NOT NULL,
    recall FLOAT NOT NULL,
    roc_auc_score FLOAT NOT NULL,
    true_positives INT NOT NULL,
    false_positives INT NOT NULL,
    false_negatives INT NOT NULL,
    true_negatives INT NOT NULL,
    PRIMARY KEY (id)
);

-- @block
CREATE TABLE income_best_params(
    id UUID DEFAULT gen_random_uuid(),
    algorithm_id INT NOT NULL,
    hyperparameter_name VARCHAR(255) NOT NULL,
    best_value VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(algorithm_id) REFERENCES income_algorithms(id)
)

-- @block
CREATE TABLE income_cv_scores(
    id UUID DEFAULT gen_random_uuid(),
    algorithm_id INT NOT NULL,
    accuracy_score FLOAT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(algorithm_id) REFERENCES income_algorithms(id)
)

-- @block
DROP TABLE income_cv_scores
