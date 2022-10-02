// NEW POST // 
document.getElementById('newPost').addEventListener
('click', newPost);

function newPost(){
fetch('/post',{
    method: 'GET',
})
.then(response => {
    window.location = response.url
    })
}

// GET UPDATE POST //  

for (let updatePostButton of document.getElementsByClassName('updatePost')) {
    updatePostButton.addEventListener('click', updatePost);
}

function updatePost(event){
    let form = event.target.form;
    event.preventDefault();    
    fetch("/post/" + form.post_id.value,{
    method: 'GET',
    })
    .then(response => {
    window.location = response.url
    })
}

// DELETE POST //  

for (let deletePostButton of document.getElementsByClassName('deletePost')) {
    deletePostButton.addEventListener('click', deletePost);
}

function deletePost(event){
    let form = event.target.form;
    event.preventDefault();    
    fetch("/post/" + form.post_id.value,{
    method: 'DELETE',
    })
    .then(response => {
    window.location = response.url
    })
}
