// const user = {
//     username : "JohnDoe",
//     loginCount : 8,
//     signedIn : true,

//     getUserDetails : function(){
//         console.log(`Got user details from ${this.username}`)
//         console.log(this)
//     }
// }



// // console.log(user)
// console.log(user.getUserDetails())

// console.log(this) // {} but in brower it will be window object




// const promiseOne = new Promise((resolve, reject) => {

// })

// const date = new Date()

function User(username, loginCount, signedIn){
     
    this.username = username;
    this.loginCount = loginCount;
    this.signedIn = signedIn;
    this.greetings = function(){
        console.log(`Welcome ${this.username}`)
    }
    return this;
}

// const userOne = User("hitesh" , 12, true)
// const userTwo = User("JaneDoe" , 13, true)

// console.log(userOne);// override the default return value of the function   

const userOne = new User("hitesh" , 12, true)
const userTwo = new User("JaneDoe" , 13, true)

console.log(userOne.constructor);

