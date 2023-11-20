const express = require('express');
const app = express();
const mysql = require('mysql');
const cors = require('cors');
const bodyParser = require('body-parser');
const { urlencoded } = require('body-parser');
const PORT = process.env.port || 8000;

const db = mysql.createPool({
    host: "localhost",
    user: "root",
	port: 3305,
    password: "python",
    database: "python"
});

app.use(cors());
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/api/get", (req, res)=>{
	console.log("/api/get");
    const sqlQuery = "SELECT * FROM simpleboard;";
    db.query(sqlQuery, (err, result)=>{
		console.log("err",err);
		console.log("result",result);
        res.send(result);
    })
})

app.post("/api/insert", (req, res) => {
	console.log("/api/insert");
    const title = req.body.title;
    const content = req.body.content;
    const sqlQuery = "INSERT INTO simpleboard (title, content) VALUES (?,?)";
    db.query(sqlQuery, [title, content], (err, result) => {
		console.log("result",result);
        res.send('success!');
    });
});



// emp ---------------------------------------

app.get("/emp/select_list", (req, res)=>{
	console.log("/emp/select_list");
    const sqlQuery = "SELECT * FROM emp";
    db.query(sqlQuery, (err, result)=>{
		console.log("err",err);
		console.log("result",result);
        res.send(result);
    })
})

app.post("/emp/select_one", (req, res)=>{
	console.log("/emp/select_one");
	const e_id = req.body.e_id;
    const sqlQuery = `
		SELECT * FROM emp
		where
			e_id = '${e_id}'
	`;
    db.query(sqlQuery, (err, result)=>{
		console.log("result",result);
        res.send(result[0]);
    })
})

app.post("/emp/insert", (req, res)=>{
	console.log("/emp/insert");
	const e_id = req.body.e_id;
	const e_name = req.body.e_name;
	const gen = req.body.gen;
	const addr = req.body.addr;
    const sqlQuery = `
		insert into emp
			(e_id, e_name, gen, addr)
		values
			('${e_id}', '${e_name}', '${gen}', '${addr}')
	`;
    db.query(sqlQuery, (err, result)=>{
		var cnt = result.affectedRows;
		console.log(cnt);
        res.send(cnt+"");
    })
})



app.listen(PORT, () => {
    console.log(`running on port ${PORT}`);
});