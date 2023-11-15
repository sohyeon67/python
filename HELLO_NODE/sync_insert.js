const mysql = require('sync-mysql');

const connection = new mysql({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

var e_id = '3';
var e_name = '3';
var gen = '3';
var addr = '3';

var sql = `
	insert into emp
		(e_id, e_name, gen, addr)
	values
		('${e_id}', '${e_name}', '${gen}', '${addr}')
`;
var result = connection.query(sql);
console.log(result.affectedRows);
connection.dispose();