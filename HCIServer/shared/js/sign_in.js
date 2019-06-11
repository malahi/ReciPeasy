$(document).ready(function () {
    $(document).on('click', '#log_button', function () {
        login();
    })
});

$(document).ready(function () {
    $(document).on('click', '#reg_button', function () {
        register();
    })
});

function register(){
    let username = document.getElementById('rusername').value;
    let password = document.getElementById('rpassword').value;
    let password2 = document.getElementById('rpassword2').value;
    if(username === '' || password === '' || password2 === ''){
        alert('Please fill all fields');
        return;
    }
    let email = document.getElementById('email').value;
    $.post('/register', JSON.stringify({username:username, password:password, email:email}), (res)=>{
        alert(res)
        window.location = '/';
    })
}

function login(){
    let username = document.getElementById('susername').value;
    let password = document.getElementById('spassword').value;
    if(username === '' || password === ''){
        alert('Please fill all fields');
        return;
    }

     $.post('/login', JSON.stringify({username:username, password:password}), (res)=>{
        if(res === 'False')
            alert('Wrong Login or password');
         else {
            document.cookie = res;
            window.location = '/';
         }
    })
}