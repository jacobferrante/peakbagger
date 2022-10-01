
// HOMEPAGE // 
/*
document.getElementById('hikeList').addEventListener
('click', hikeList);

function hikeList(){
fetch('/',{
    method: 'GET',
})
.then(response => {
    window.location = response.url
    })
}
*/


// NEW POST // 
document.getElementById('newPost').addEventListener
('click', newPost);

function newPost(){
fetch('/hike',{
    method: 'GET',
})
.then(response => {
    window.location = response.url
    })
}

// DELETE POST // 
document.getElementById('deletePost').addEventListener
('click', deletePost);

function deletePost(){ 
    fetch("/post/3",{
    method: 'DELETE',
    })
    .then(response => {
    window.location = response.url
    })
}

// UPDATE POST //  
document.getElementById('updatePost').addEventListener
('click', updatePost);

function updatePost(event){
    let form = event.target.form;
    console.log(form.post_id.value);
    console.log("/post/" + form.post_id.value);
    event.preventDefault();    


}

/*
    fetch("/post/" + form.post_id.value,{
    method: 'GET',
    })
    .then(response => {
    window.location = response.url
    })
*/ 

// UPDATE POST //  
//document.getElementById('updatePost').addEventListener
//('click', updatePost);
//
//function updatePost(){
//    fetch("/hike/1",{
//    method: 'PUT',
//    })
//    .then(response => {
//    window.location = response.url
//    })
//}
