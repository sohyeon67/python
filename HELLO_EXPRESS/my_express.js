/*express : flask 같은 nodejs의 라이브러리*/
var express = require('express');
var app = express();
var port = 3000;

var bodyParser = require('body-parser');

app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));	// URL-encoded 등록

app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => {
	res.send('Hello Express!');
})

app.get('/param', (req, res) => {
	var menu = req.query.menu;
	res.send('PARAM:'+menu);
})

app.post('/post', (req, res) => {
	const menu = req.body.menu
	res.send('Post:'+menu);
})

app.get('/forw', (req, res) => {
	var a = "홍길동";
	var b = ['유관순', '윤석렬'];
	var c = [
		{e_id:'1',e_name:'1',gen:'1',addr:'1'},
		{e_id:'2',e_name:'2',gen:'2',addr:'2'}
	];
	res.render('forw', { a:a, b:b, c:c });
})

/*app.get('/pug', (req, res) => {
	res.render('pug');
})*/

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
})