function displaytext(letter){

    var output = document.getElementById(letter).innerHTML;
    // console.log(output);

    document.getElementById("lettercombo").value += output;
}

function logtext(values){
    var list_values = [];

    
}

function log_test(values){
    console.log(values);
}


const alphabet = document.getElementsByClassName('alphabet');

// for(i = 0; i< alphabet.length; i++){
//     console.log(alphabet[i].innerHTML);
//     // console.log("hello")
// }


// for(i=0; i<5; i++){
//     console.log(i);
// }

console.log(alphabet)
console.log(alphabet[0])