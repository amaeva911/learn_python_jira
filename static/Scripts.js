function authent(){
    let login = document.getElementById('login').value;
    let password = document.getElementById('password').value;
    alert(login + ", " + password)
}

let JiraID;
let ActivationDate = 0;
function printResult(id){
    let Now = new Date();
    let time = Math.round((Now.getTime() - ActivationDate)/60000);
    if(ActivationDate != 0){
        alert(time);
    }
    JiraID = id;
    ActivationDate = Now.getTime();
}


