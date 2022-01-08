const express = require("express")
const app = express()
const mysql = require("mysql")
const cors = require("cors")
const bodyParser = require("body-parser")

const PORT = process.env.PORT || 3001

app.use(cors())
app.use(bodyParser.json())

const dbConfig = {
    host: "localhost",
    user: "root",
    password: "test",
    database: "gelal_express_database"
}

db = mysql.createConnection(dbConfig);
db.connect();

app.get("/api", (req, res) => {
    res.send("WELCOME TO GELAL EXPRESS API")
})

app.get("/api/category", (req, res) => {
    const sqlQuery = `SELECT * from ${db.config.database}.category`
    db.query(sqlQuery, [req.params.uuid], (err, result) => {
        if (err) {
            console.log(err)
            res.send("An error occured.")
            return
        }
        res.send(result)
    })
})

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}.`)
})

// Cmd command to start the server --> npm run devStart