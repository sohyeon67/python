const mysql = require('mysql');
const connection = mysql.createConnection({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

var e_id = '3';
var e_name = '4';
var gen = '4';
var addr = '4';

connection.connect();
var sql = `
	update emp
		set e_name='${e_name}', 
			gen='${gen}',
			addr='${addr}'
		where e_id='${e_id}'
`;

connection.query(sql, (error, result) => {
	console.log(result.affectedRows);
});

connection.end();
