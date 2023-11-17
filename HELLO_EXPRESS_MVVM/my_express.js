/*express : flask 같은 nodejs의 라이브러리*/
var DaoEmp = require('./daoemp.js');
var mysql = require('sync-mysql');
var express = require('express');
var app = express();
var port = 3000;

var bodyParser = require('body-parser');

app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));	// URL-encoded 등록

app.set('view engine', 'ejs');
app.set('views', './views');

app.use('/static', express.static('static'));

app.get('/', (req, res) => {
	res.redirect("static/emp.html");
})

// ajax.html 관련 ---------------------------------------------
app.post('/jquery.ajax', (req, res) => {
	var e_id = req.body.e_id;
	console.log("e_id", e_id);
	var myjson = {'msg':'ok'};
	res.json(myjson);
})

app.post('/axios.ajax', (req, res) => {
	var e_id = req.body.e_id;
	console.log("e_id", e_id);
	var myjson = {'msg':'ok2'};
	res.json(myjson);
})

app.post('/fetch.ajax', (req, res) => {
	var e_id = req.body.e_id;
	console.log("e_id", e_id);
	var myjson = {'msg':'ok3'};
	res.json(myjson);
})
// ajax.html 관련 END ---------------------------------------------


// emp.html 관련 --------------------------------------------------
app.post('/selectlist.ajax', (req, res) => {
	var de = new DaoEmp();
	var list = de.selectList();
	var myjson = {'list':list};
	res.json(myjson);
})


app.post('/select.ajax', (req, res) => {
	var e_id = req.body.e_id;
	var de = new DaoEmp();
	var vo = de.select(e_id);
	var myjson = {'vo':vo};
	res.json(myjson);
})

app.post('/insert.ajax', (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	
	var de = new DaoEmp();
	var cnt = de.insert(e_id,e_name,gen,addr);
	var myjson = {'cnt':cnt};
	res.json(myjson);
})

app.post('/update.ajax', (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	
	var de = new DaoEmp();
	var cnt = de.update(e_id,e_name,gen,addr);
	var myjson = {'cnt':cnt};
	res.json(myjson);
})

app.post('/delete.ajax', (req, res) => {
	var e_id = req.body.e_id;
	
	var de = new DaoEmp();
	var cnt = de.delete(e_id);
	var myjson = {'cnt':cnt};
	res.json(myjson);
})


// emp.html 관련 END ------------------------------------------------


app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
})