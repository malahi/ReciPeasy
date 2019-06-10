$.get('/data/?_collection=recipes', function (res) {
    for(let i = 0; i < res.length; i += 2)
        document.getElementById('popular-recent-table').innerHTML +=
                                        generateHTMLRow(res[i]['id'], res[i]['name'],   res[i]['description'],   res[i]['image'],   res[i]['author'],
                                                        res[i+1]['id'], res[i+1]['name'], res[i+1]['description'], res[i+1]['image'], res[i+1]['author']);
});



function generateHTMLRow(popular_id, popular_title, popular_description, popular_image, popular_author,
                         recent_id, recet_title, recet_description, recent_image, recent_author){

    return '<td  width="650">\n' +
                generateOneColum(popular_id, popular_image, popular_title, popular_description, popular_author) +
        '  </td>\n' +
        '  <td class="mytd"></td>\n' +
        '<td  width="650">\n' +
                generateOneColum(recent_id, recent_image, recet_title, recet_description, recent_author) +
        '</td>';
}


function generateOneColum(id, image, title, description, author) {
    return  '    <div class="row">\n' +
        '        <div class="col-lg-1"></div>\n' +
        '        <div class="col-lg-10" align="center">\n' +
        // '          <img style=" box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 20px 20px 0 rgba(0, 0, 0, 0.19);"  src=' + popular_image + ' width="400" height="300"  class="rounded-circle">\n' +
        '           <div style="padding-right: 360px" class="flip-card rounded-circle">\n' +
        '               <div class="flip-card-inner rounded-circle">\n' +
        '                   <div class="flip-card-front">\n' +
        '                     <img style="box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 20px 20px 0 rgba(0, 0, 0, 0.19);"  src=' + image + ' width="400" height="300"  class="rounded-circle">\n' +
        '                     </div>\n' +
        '                     <div class="flip-card-back rounded-circle">\n' +
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
        '        </div>\n' +
        '        <div class="col-lg-1"></div>\n' +
        '    </div>\n' +
        '     <hr  width="96%" style="float: right" class="delimiter">\n';
}

function chooseRecipe(id){
     window.location = '/recipe.html?_id=' + id;
}