const mysql = require('mysql');
const connection = mysql.createConnection({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

connection.connect();
console.log("start");
var sql = `
	insert into emp
		(e_id, e_name, gen, addr)
	values
		('3', '3', '3', '3')
`;

connection.query(sql, (error, result) => {
	console.log(result.affectedRows);
	console.log("result");
});

connection.end();
console.log("end");