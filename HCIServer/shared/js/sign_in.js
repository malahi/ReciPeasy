function register(){
    let username = document.getElementById('rusername').value;
    let password = document.getElementById('rpassword').value;
    let email = document.getElementById('email').value;
    $.post('/register', JSON.stringify({username:username, password:password, email:email}), (res)=>{
        alert(res)
    })
}

function login(){
    let username = document.getElementById('susername').value;
    let password = document.getElementById('spassword').value;
     $.post('/login', JSON.stringify({username:username, password:password}), (res)=>{
        if(res === 'False')
            alert('Wrong Login or password');
         else {
            document.cookie = res;
            window.location = '/';
         }
    })
}