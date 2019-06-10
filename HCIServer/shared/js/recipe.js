function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });

    return vars;
}

let params = getUrlVars();

$(document).ready(function () {
        $.get('/data/?_collection=recipes&_id=' + params['_id'], function (res) {
        // alert(JSON.stringify(res));
        document.getElementById('recipe1').innerHTML += generatePage(res[0]);
    });
})

function generatePage(recipe){
    return '<div style="padding-left: 3%" class="row">\n' +
        '        <div  class="card">\n' +
        '            <div class="card-body" style=height: 100%;">\n' +
        '        <img class="card-img-top" style="width:600px;height:400px;" src="' + recipe['image'] + '" alt="Card image cap">\n' +
        '        <a href="#!">\n' +
        '      <div class="mask rgba-white-slight"></div>\n' +
        '    </a>\n' +
        '    <br>\n' +
        '    <h4 class="card-title"> ' + recipe['name'] + ' </h4>\n' +
        '    <p class="card-text"> ' + recipe['description'] + ' </p>\n' +
                     '    <br>\n' +
             '    <br>\n' +
         '    <h4 class="card-title"> Preparation </h4>\n' +

         '    <p class="card-text"> ' + recipe['preperation'] + ' </p>\n' +
        '  </div>\n' +
        '</div>\n' +
        '<div style="padding-left: 2%" >\n' +
        '\n' +
        '        <div  class="card" style="width:600px;height:100%;">\n' +
        '  <div class="card-body">\n' +
        ' \n' +
        '<iframe width="565" height="400"\n' +
        'src="' + recipe['video'] + '">\n' +
        '</iframe>' +
        ' <br>' +
        ' <br>' +
        '    <h4 class="card-title">Ingredients:</h4>\n' +
        '    <p class="card-text">' + makeIngredients(recipe['ingredients']) + '</p>\n' +
        '  </div>\n' +
        '</div>\n' +
        '</div>\n' +
        '  </div>\n';
}

function makeIngredients(ingr) {
    let ingr_arr = ingr.split('\n');

    let ans = '';
    for (let i = 0; i < ingr_arr.length; i++)
        ans += '<p>' + ingr_arr[i] + '</p>';
    return ans;
}

