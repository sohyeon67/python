const mysql = require('mysql');
const connection = mysql.createConnection({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

connection.connect();

connection.query('SELECT * from emp', (error, rows, fields) => {
	console.log(rows);
});

connection.end();