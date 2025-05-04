let myName = "Shubhh     "


// console.log(myName.truelength)

let myHeroes = ["Ironman" , "Thor" , "Hulk" , "Captain America"]

let heroPower = {
    thor : "Hammer",
    spiderman : "Web",
    getSpiderPower : function(){
        console.log(`spide power is  ${this.spiderman}`)
    }
}
Object.prototype.hitesh = function(){
    console.log("Hitesh is a good teacher");
}
// console.log(heroPower.hitesh())
// console.log(myHeroes.hitesh())

const User = {
    name: "Shubham",
    email: "shubham@gmail.com"
}
const Teacher={
    makeVideos: true
}
const TeachingSupport={
    isAvailable : true,
}
const TASupport = {
    fullTime : true,
    makeAssignment: "JS assignment",
    __proto__ : TeachingSupport
} 
Teacher.__proto__ = User

// modern syntax

Object.setPrototypeOf(Teacher , User)

let anotherUsername = "Shubham   "

String.prototype.truelength = function(){
    console.log(`${this}`)
    console.log(`${this.length}`)
    console.log(`True length is ${this.trim().length}`)    
}

anotherUsername.truelength()

"shubh  ".truelength()