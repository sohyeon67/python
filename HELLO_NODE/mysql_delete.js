const mysql = require('mysql');
const connection = mysql.createConnection({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

var e_id = '3';

connection.connect();
var sql = `
	delete from emp
		where e_id='${e_id}'
`;

connection.query(sql, (error, result) => {
	console.log(result.affectedRows);
});

connection.end();
