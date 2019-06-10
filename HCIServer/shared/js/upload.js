function addRecipe(){
    let ingr = document.getElementById('ingr').value;
    let desc = document.getElementById('desc').value;
    let prep = document.getElementById('prep').value;
    let rec_name = document.getElementById('rec_name').value;
    let author_name = document.getElementById('author_name').value;
    let image_url = document.getElementById('image_url').value;
    let video_url = document.getElementById('video_url').value;

    let e = document.getElementById("categories");
    let category = e.options[e.selectedIndex].value;


    $.post('/addRec', JSON.stringify({ name:rec_name, description:desc, preperation:prep, ingredients:ingr, image:image_url, video:video_url, category:category, author:author_name}), (res)=>{
        alert('aa   ' + res);
    })
}