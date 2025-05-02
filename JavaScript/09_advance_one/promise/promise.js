fetch('https://something').then().catch().finally()

const promiseone = new Promise((resolve, reject) => {
    // do an async task 
    // db calls , cryptograpgy network 
    setTimeout(() => {
        console.log('Asunc task is complete')
        resolve()
    } ,1000)
})

promiseone.then(() => {
    console.log('Promise resolved');
}).catch(() => {
    console.log('Promise rejected');
}).finally(() => {
    console.log('Promise completed');
})

new Promise((resolve, reject) => {
    setTimeout(()=>{
        console.log("Async task 2 is complete")
        resolve()
    } , 1000)
}).then(()=>{
    console.log("Async 2 resolved");
})

const promisethree = new Promise((resolve , reject)=>{
    setTimeout(()=>{
        console.log("Async task 3 is complete")
        resolve({
            name: 'John',
            age: 30,
            email: 'john@example.com'
        })
    } , 1000)
})

promisethree.then((user)=>{
    console.log(user)
    console.log(`User's email is: ${user.email}`);
    console.log(`User's name is: ${user.name}`);
    console.log(`User's age is: ${user.age}`);

}).catch((error)=>{
    console.log('Error:', error);

})

const promisefour = new Promise((resolve , reject)=>{
    setTimeout(()=>{
        let error = true;
        if (error) {
            reject('An error occurred in promisefour');
        } else {
            resolve({username: 'shubhagl' , password: '1234'});
        }
    } , 1000)
})
promisefour
.then((user)=>{
    console.log(user)
    // console.log(`User's username is: ${user.username}`);
    // console.log(`User's password is: ${user.password}`);
    return user.username
})
.then((username)=>{
    console.log(username); // This will log the username from the previous promise
})
.catch((error)=>{
    console.log('Error:', error); // Handle the error appropriately
    // You might want to add additional error handling logic here
})
.finally(()=>{
    console.log('Promise four completed'); // This will always run
})

const promisefive = new Promise((resolve , reject)=>{
    setTimeout(()=>{
        let error = true;
        if (error) {
            reject('An error occurred in promisefive');
        } else {
            resolve({username: 'primse5' , password: '1234'});
        }
    } , 1000)
})
// async function consumepromisefive(){
//     const response = await promisefive;
//     console.log(response);

//     console.log(`Username from promisefive is: ${response.username}`);
//     console.log(`Password from promisefive is: ${response.password}`);
// }
// consumepromisefive()    
async function consumepromisefive(){
    try{
        const response = await promisefive;
    console.log(response);

    console.log(`Username from promisefive is: ${response.username}`);
    console.log(`Password from promisefive is: ${response.password}`);
    } catch(error){
        console.log('Error:', error); // Handle the error appropriately
    }
    
}
consumepromisefive()    

async function fetchData() {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = response.json();
    console.log(data);
}
fetchData()

async function fetchData() {
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        console.log(data);
    }
    catch(error){
        console.log('Error:', error); // Handle the error appropriately
    } 
   
}
fetchData()

fetch('https://jsonplaceholder.typicode.com/users')
.then((res) =>{
return res.json();
})
.then((data) => {
console.log(data);
})
.catch((err) =>{
console.log(err);
})