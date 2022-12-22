const updateDb = require("./updatedDb");

updateDb(
  "./results/income_best_params.csv",
  `
            INSERT INTO income_best_params(
              algorithm_id,
              hyperparameter_name,
              best_value
            )
            VALUES(
              $1,
              $2,
              $3
            );
          `,
      10000,
      10000
);
