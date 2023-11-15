const mysql = require('sync-mysql');

const connection = new mysql({
	host: 'localhost',
	port: 3305,
	user: 'root',
	password: 'python',
	database: 'python'
});

var sql = `
	select * from emp
`;
var result = connection.query(sql);
console.log(result);
connection.dispose();