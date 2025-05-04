// // java script default behvior is prototypical behaviuor 
// // java script wont give up util it find null

// function multiplyBy5(a){
//     return a * 5;
// }   
// multiplyBy5.power = 5; // adding a property to the function
// console.log(multiplyBy5(2));
// console.log(multiplyBy5.power);
// console.log(multiplyBy5.prototype);


function createUser(username , score){
    this.username = username;
    this.score = score;
    this.greetings = function(){
        console.log(`Welcome ${this.username}`)
    } 
}
createUser.prototype.greet = function(){
    this.score++;
}
createUser.prototype.scoree = function(){
    console.log(`Your score is ${this.score}`)
}
const chai = new createUser("chai" , 10)
const tea = new createUser("tea" , 20)
 
chai.scoree()
console.log(createUser)
console.log(createUser.prototype)