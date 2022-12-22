const updateDb = require("./updatedDb");
updateDb(
  "./results/income_algorithms.csv",
  `
    INSERT INTO income_algorithms(
        id,
        algorithm_name,
        best_accuracy,
        algorithm_precision,
        recall,
        roc_auc_score,
        true_positives,
        false_positives,
        false_negatives,
        true_negatives
      )
      VALUES(
        $1,
        $2,
        $3,
        $4,
        $5,
        $6,
        $7,
        $8,
        $9,
        $10
      );
    `,
    10000,
    10000,
    true
);
