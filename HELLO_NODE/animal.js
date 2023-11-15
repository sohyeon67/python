class Animal {
	constructor() {
		this.full = 1;
	}
	
	eat(amount) {
		this.full += amount;
	}
}

module.exports = Animal;

if (require.main === module) {
    var ani = new Animal();
	console.log("ani.full1 :",ani.full);
	ani.eat(9);
	console.log("ani.full1 :",ani.full);
}
