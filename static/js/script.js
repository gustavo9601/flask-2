
const destruction = document.getElementById('destruction');

let timer = 10;
let counter = 1;

let interval = setInterval(() => {

    let text = 'This page will be destructed in: ' + (timer - counter);
    destruction.innerHTML = text;

    counter++;

    if(timer === counter ){
        clearInterval(interval);
        destruction.innerHTML = 'BOOM!!!!!';
    }

}, 1000)