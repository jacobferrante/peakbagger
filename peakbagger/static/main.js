
// HOMEPAGE // 
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

// NEW HIKE // 
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

document.getElementById('deletePost').addEventListener
('click', deletePost);

function deletePost(){ 
    fetch("/hike/3",{
    method: 'DELETE',
    })
    .then(response => {
    window.location = response.url
    })
}

// UPDATE HIKE //  
document.getElementById('updatePost').addEventListener
('click', updatePost);

function updatePost(){
    fetch("/hike/3",{
    method: 'PUT',
    })
    .then(response => {
    window.location = response.url
    })
}
