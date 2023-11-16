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

app.get('/', (req, res) => {
	res.render('emp_list');
})

app.get('/emp_list', (req, res) => {
	var de = new DaoEmp();
	var list = de.selectList();
	res.render('emp_list', {list:list});
})

app.get('/emp_detail', (req, res) => {
	var e_id = req.query.e_id;
	var de = new DaoEmp();
	var vo = de.select(e_id);
	res.render('emp_detail', {vo:vo});
})

app.get('/emp_add', (req, res) => {
	res.render('emp_add');
})

app.post('/emp_add_act', (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	
	var de = new DaoEmp();
	var cnt = de.insert(e_id,e_name,gen,addr);
	res.render('emp_add_act', {cnt:cnt});
})

app.get('/emp_mod', (req, res) => {
	var e_id = req.query.e_id;
	var de = new DaoEmp();
	var vo = de.select(e_id);
	res.render('emp_mod', {vo:vo});
})

app.post('/emp_mod_act', (req, res) => {
	var e_id = req.body.e_id;
	var e_name = req.body.e_name;
	var gen = req.body.gen;
	var addr = req.body.addr;
	
	var de = new DaoEmp();
	var cnt = de.update(e_id,e_name,gen,addr);
	res.render('emp_mod_act', {cnt:cnt});
})

app.post('/emp_del_act', (req, res) => {
	var e_id = req.body.e_id;
	var de = new DaoEmp();
	var cnt = de.delete(e_id);
	res.render('emp_del_act', {cnt:cnt});
})


app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
})