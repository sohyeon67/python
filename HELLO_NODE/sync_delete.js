const mysql = require('sync-mysql');

const connection = new mysql({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

var e_id = '3';

var sql = `
	delete from emp
		where e_id='${e_id}'
`;

var result = connection.query(sql);
console.log(result.affectedRows);
connection.dispose();