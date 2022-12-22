const Pool = require("pg").Pool;
require("dotenv").config();
const fastcsv = require("fast-csv");
const fs = require("fs");

async function updateDb(csv_path, query, rebuildDb = false) {
  const stream = fs.createReadStream(csv_path);
  const csvData = [];
  let csvStream = fastcsv
    .parse()
    .on("data", function (data) {
      csvData.push(data);
    })
    .on("end", function () {
      // remove the first line: header
      csvData.shift();

      const pool = new Pool({
        host: process.env.POSTGRES_HOST,
        port: process.env.POSTGRES_PORT,
        user: process.env.POSTGRES_USER,
        password: process.env.POSTGRES_PASSWORD,
        database: process.env.DATABASE,
        connectionTimeoutMillis: 5000,
      });

      pool.connect(async (err, client, done) => {
        if (err) throw err;
        try {
          if (rebuildDb) {
            await client.query("DELETE FROM income_best_params");
            await client.query("DELETE FROM income_cv_scores;");
            await client.query("DELETE FROM income_algorithms;");
          }
          csvData.forEach((row) => {
            client.query(query, row, (err, res) => {
              if (err) {
                console.log(err);
              } else {
                console.log("inserted " + res.rowCount + " row:", row);
              }
            });
          });
        } finally {
          done();
        }
      });
    });

  stream.pipe(csvStream);
}

module.exports = updateDb;
