const myTitle = document.getElementById("myTitle");
const myImage = document.getElementById("myImage");
const myInput = document.getElementById("myInput");

const knopNoord = document.getElementById('knopNoord');
const knopOost = document.getElementById('knopOost');
const knopZuid = document.getElementById('knopZuid');
const knopWest = document.getElementById('knopWest');

let directionButtons = {
    "noord": document.getElementById('knopNoord'),
    "oost": document.getElementById('knopOost'),
    "zuid": document.getElementById('knopZuid'),
    "west": document.getElementById('knopWest')
}
let current_index = 0;

let lokaties = [
    {
        "titel":"plaats 0",
        "image":"img/ingang.jpg",
        "directions": {
            "zuid": 1,
            "oost": 2
        }
    },
    {
        "titel":"plaats 1",
        "image":"img/rondleiding1.jpg",
        "directions": {
            "noord": 0,
            "oost": 3
        }
    },
    {
        "titel":"plaats 2",
        "image":"img/plaatstwee.jpg",
        "directions": {
            "west": 0,
            "oost": 4
        }
    },
    {
        "titel":"plaats 3",
        "image":"img/images.jpeg",
        "directions": {
            "west": 1,
            "oost": 7
        }
    },
    {
        "titel":"plaats 4",
        "image":"img/plaats4interactieveroute.jpeg",
        "directions": {
            "west": 3,
            "oost": 5
        }

    },
    {
        "titel":"plaats 5",
        "image":"img/plaatsvijf.png",
        "directions": {
            "zuid": 6,
            "west": 4
        }
    },
    {
        "titel":"plaats 6",
        "image":"img/laatste.jpeg",
        "directions": {
            "noord": 5,
            "west": 7
        }
    },
    {
        "titel":"tussenstop",
        "image":"img/tussenstop.jpg",
        "directions": {
            "oost": 6,
            "west": 3
    }
    }
];

function show(index){
    myTitle.innerHTML = lokaties[index].titel;
    myImage.src = lokaties[index].image;
    current_index = index;

    updateDirections();
}

function updateDirections(){
    let possible = lokaties[current_index].directions;

    let possible_keys = Object.keys(possible);

    console.log(possible);
    console.log(possible_keys);

    let button_keys = Object.keys(directionButtons);
    console.log(button_keys);

    for (const key of possible_keys){

    }
}

function getInput(){
    show(myInput.value);
    myInput.value = "";
    myInput.focus();
}

function goDirection(richting){
    let punt_index = lokaties[current_index].directions[richting];
    show(punt_index);
}

show(0);