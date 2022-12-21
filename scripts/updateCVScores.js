const updateDb = require("./updatedDb");

updateDb(
  "./results/income_cv_scores.csv",
  `
            INSERT INTO income_cv_scores(
              algorithm_id,
              accuracy_score
            )
            VALUES(
              $1,
              $2
            );
          `
);
