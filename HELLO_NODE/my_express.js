/*express : flask 같은 nodejs의 라이브러리*/
var express = require('express');
var app = express();
var port = 3000;

var bodyParser = require('body-parser');

//app.use(bodyParser.json());	// json 등록
app.use(bodyParser.urlencoded({ extended : false }));	// URL-encoded 등록

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
	res.send('forw');
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`);
})