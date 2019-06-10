let result = [];

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });

    return vars;
}

let params = getUrlVars();

$.get('/data/?_collection=recipes&_id=' + params['_id'], function (res) {
    // alert(JSON.stringify(res));
    result = res;
    document.getElementById('image').setAttribute('src', res[0]['image']);
    document.getElementById('author').innerText = res[0]['author'];
    document.getElementById('title').innerText = res[0]['name'];
    showDes();
});

function showDes() {
    document.getElementById('title_name').innerText = 'Description';
    document.getElementById('value').innerText = result[0]['description']
}


function showVideo() {
    document.getElementById('title_name').innerText = 'Video';
    document.getElementById('value').innerHTML =  '<iframe width="565" height="400"\n' +
        'src="' + result[0]['video'] + '">\n' +
        '</iframe>';
}

function showPrep() {
    document.getElementById('title_name').innerText = 'Preperation';
    document.getElementById('value').innerText = result[0]['preperation']
}

function showIngred() {
    document.getElementById('title_name').innerText = 'Preperation';
    document.getElementById('value').innerHTML = makeIngredients(result[0]['ingredients'])
}


function makeIngredients(ingr) {
    let ingr_arr = ingr.split('\n');

    let ans = '';
    for (let i = 0; i < ingr_arr.length; i++)
        ans += '<p>' + ingr_arr[i] + '</p>';
    return ans;
}

