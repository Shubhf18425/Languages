// generate a random color

const randomColor = () => {
 const hex = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += hex[Math.floor(Math.random() * 16)];
    }
    return color; 
}
console.log(randomColor())

let intervalId;

const startChangingColor = () => {
    if(!intervalId) {
        intervalId = setInterval(() => {
            document.body.style.backgroundColor = randomColor();
        }, 1000);
    }
    
}

const stopChangingColor = () => {
    clearInterval(intervalId);
    intervalId = null; // reset intervalId to null
};
document.querySelector('#start').addEventListener('click', startChangingColor);
document.querySelector('#stop').addEventListener('click', stopChangingColor);

