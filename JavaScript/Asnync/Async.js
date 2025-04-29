// interval is a function that takes a callback and a delay in milliseconds
// and returns a function that will call the callback at the specified interval 



// ..................................settimeout
// setTimeout(function(){
//     console.log("Hello World")
// } , 2000)

// const Shubh = function(){
//     console.log("HELLO WORLD");
// }
// setTimeout(Shubh , 2000)



// const changeText = function(){
//     document.querySelector('h1').innerHTML = "Hello Cutie"
// }
// const changeMe = setTimeout(changeText , 2000)

// // ..................................cleartimeout

// document.querySelector('#stop').addEventListener('click', function() {
//     clearTimeout(changeMe);
//     console.log("Timeout Cleared");
// });


// .......................................setInterval

// setInterval(function(str){
//     console.log(str , Date.now())
// } , 1000)


const date = function(str){
    console.log(str , Date.now())
}
let sayDate;
document.querySelector('#start').addEventListener('click', function() {
     sayDate = setInterval(date , 1000 , "Paramenter")
})


// .................................clearInterval


document.querySelector('#stop').addEventListener('click', function() {
    clearInterval(sayDate);
    console.log("Interval Cleared");
});
