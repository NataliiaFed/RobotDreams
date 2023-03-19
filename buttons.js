// create a new div and append it to the body
const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.textAlign = 'center';
document.getElementsByTagName('body')[0].appendChild(myDiv);

// add h2 to the div
const myDivHeading = document.createElement('h2');
myDivHeading.innerText = 'Get in touch';
myDiv.appendChild(myDivHeading);

// add buttons to the div
['Connect', 'Message', 'Offer a job'].map(buttonName => {
    let button = document.createElement('button');
    button.innerText = `${buttonName}`;
    button.style.background = 'lightgrey';
    button.style.marginLeft = '10px';
    button.style.marginBottom = '10px';
    button.style.fontSize = '16px';
    myDiv.appendChild(button)
});

// add paragraphe with random number of friend to the div
let i = Math.floor(Math.random() * 100);

let friendsNumber = document.createElement('p');
friendsNumber.innerText = `Friends: ${i}`;
myDiv.appendChild(friendsNumber);

// event for button Connect
const btnConnect = document.getElementsByTagName('button')[0];
btnConnect.onclick = (event) => {
    friendsNumber.innerText = `Friends: ${++i}`;
    event.target.disabled = true;
    event.target.innerText = 'Requested';
};

// event for button Message
let btnMessage = document.getElementsByTagName('button')[1];
btnMessage.onclick = (event) => {
    if(event.target.style.background == "lightgrey"){
        event.target.style.background = "grey";
    } else {
        event.target.style.background = "lightgrey";
    }
};

// event for button Offer a job
let btnJobOffer = document.getElementsByTagName('button')[2];
btnJobOffer.onclick = (event) => {
    if(btnConnect.style.visibility == "hidden"){
        btnConnect.style.visibility = "visible";
    } else {
        btnConnect.style.visibility = "hidden";
    }
};