let row_id = 0

function findRecipes(all_rec){
    document.getElementById('search').innerHTML = '';
    row_id = 0

    let e = document.getElementById("categories");
    let category = e.options[e.selectedIndex].value;
    let title = document.getElementById('search_value').value

    let get_request = '/data/?_collection=recipes&_category=' + category;
    get_request += all_rec? '&_title=' + title : '';
    $.get(get_request, function (res) {
        let num_of_rec = res.length - 1;
        for (let i = 0; i < res.length/3; i++)
            document.getElementById('search').innerHTML += generateRow();
        row_id = 3;
        let col_i = 0;
        while(num_of_rec >= 0) {
            document.getElementById(row_id + col_i).innerHTML = generateCard(res[num_of_rec--]);
            col_i = (col_i + 1) % 3;
            if (col_i == 0)
                row_id += 3;
        }
    });
}


function generateRow(){
    row_id += 3;
    return '<div class="row">\n' +
        '    <div class="col-lg-1"></div>\n' +
        '    <div class="col-lg-3" id="' + row_id + '"></div>\n' +
        '    <div class="col-lg-3" id="' + (row_id + 1) + '"></div>\n' +
        '    <div class="col-lg-3" id="' + (row_id + 2) + '"></div>\n' +
        '   </div>' +
        '   <br>' +
        '   <br>';
}

function generateCard(recipe){
    return '<!-- Card Narrower -->\n' +
        '<div class="card card-cascade narrower">\n' +
        '  <div class="view view-cascade overlay">\n' +
        '    <img  class="card-img-top"  style="height: 250px;" src="' + recipe['image'] + '" alt="Card image cap">\n' +
        '    <a>\n' +
        '      <div class="mask rgba-white-slight"></div>\n' +
        '    </a>\n' +
        '  </div>\n' +
        '  <div class="card-body card-body-cascade">\n' +
        '    <h5 class="pink-text pb-2 pt-1"><i class="fas fa-utensils"></i> ' + recipe['author'] + '</h5>\n' +
        '    <h4 class="font-weight-bold card-title">' + recipe['name'] + '</h4>\n' +
        '    <p class="card-text">' + recipe['description'] + '</p>\n' +
        '    <a class="btn btn-warning" onclick="chooseRecipe('+ recipe['id'] + ');">Read More</a>\n' +
        '  </div>';
}

function chooseRecipe(id){
     window.location = '/recipe.html?_id=' + id;
}