$.get('/data/?_collection=recipes', function (res) {

    for(let i = 0; i < res.length; i += 1 ){
        document.getElementById('popular-recent-table').innerHTML +=
            generateHTMLRow(res[i]['id'], res[i]['name'], res[i]['description'], res[i]['image'], res[i]['author']);
    }
});



function generateHTMLRow(popular_id, popular_title, popular_description, popular_image, popular_author){

    return generateOneColum(popular_id, popular_image, popular_title, popular_description, popular_author);
}


function generateOneColum(id, image, title, description, author) {
    return'           <div class="flip-card">\n' +
        '               <div class="flip-card-inner">\n' +
        '                   <div class="flip-card-front ">\n' +
        '                     <img style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 20px 20px 0 rgba(0, 0, 0, 0.19);"  src=' + image + ' width="100%" height="100%" >\n' +
        '                     </div>\n' +
        '                     <div class="flip-card-back">\n' +
        '                     <br><br><br> ' +
        '                     <h1><font face="Impact">Author</font></h1>\n' +
        '                     <h3><font face="Impact">' + author + '</font></h3>\n' +
        '                     </div>\n' +
        '               </div>\n' +
        '           </div>' +
        '          <br> ' +
        '          <div style="text-decoration: underline; font-size: 140%;" > <p><font face="Impact">' + title + '</font></p></div>\n' +
        '          <p class="mydescription"><font face="Arial Black">' + description + '</font> </p>\n' +
        '          <button type="button" class="btn btn-warning" onclick="chooseRecipe(' + id + ')">Read More</button>' +
     '<br><br>';/*+ ' <hr  width="96%" style="float: right" class="delimiter">\n'*/;
}

function chooseRecipe(id){
     window.location = '/recipe.html?_id=' + id;
}