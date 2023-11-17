var Mysql = require('sync-mysql');

class DaoEmp {
	
	constructor() {
		this.conn = new Mysql({
			host: 'localhost',
			port: 3305,
			user: 'root',
			password: 'python',
			database: 'python'
		});

	}
	
	selectList() {
		var sql = `
			select * from emp
		`;
		var result = this.conn.query(sql);
		return result;
	}
	
	select(e_id) {
		var sql = `
			select * 
				from emp
				where e_id = '${e_id}'
		`;
		var result = this.conn.query(sql);
		return result[0];
	}
	
	insert(e_id, e_name, gen, addr) {
		var sql = `
			insert into emp
				(e_id, e_name, gen, addr)
			values
				('${e_id}', '${e_name}', '${gen}', '${addr}')
		`;
		var result = this.conn.query(sql);
		return result.affectedRows;
	}
	
	update(e_id, e_name, gen, addr) {
		var sql = `
			update emp
				set e_name='${e_name}', 
					gen='${gen}',
					addr='${addr}'
				where e_id='${e_id}'
		`;
		var result = this.conn.query(sql);
		return result.affectedRows;
	}
	
	delete(e_id) {
		var sql = `
			delete from emp
				where e_id='${e_id}'
		`;
		var result = this.conn.query(sql);
		return result.affectedRows;
	}
}

module.exports = DaoEmp;

if (require.main === module) {
    var de = new DaoEmp();
	var list = de.selectList();
	var vo = de.select('1');
	var insertCnt = de.insert('3','3','3','3');
	var updateCnt = de.update('3','4','4','4');
	var deleteCnt = de.delete('3');
	console.log(list);
	console.log(vo);
	console.log(insertCnt);
	console.log(updateCnt);
	console.log(deleteCnt);
	
}
