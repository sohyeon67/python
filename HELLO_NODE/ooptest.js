/*const Animal = require('./Animal');

var ani = new Animal();
console.log("ani.full :",ani.full);
ani.eat(9);
console.log("ani.full :",ani.full);*/

const Human = require('./Human');

var hum = new Human();
console.log("full:", hum.full);
console.log("flag_tool:", hum.flag_tool);
hum.eat(9);
hum.momstouch();
console.log("full:", hum.full);
console.log("flag_tool:", hum.flag_tool);