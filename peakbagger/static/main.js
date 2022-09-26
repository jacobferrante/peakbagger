
// new hike
document.getElementById('newHike').addEventListener
('click', newHike);

function newHike(){
fetch('/hike',{
    method: 'GET',
})
.then(response => {
    window.location = response.url
    })
}


// get ID numbers from buttons on jinja loop
let itemID = document.getElementById('deleteHike').value
itemID = `/hike/${itemID}`

// delete
document.getElementById('deleteHike').addEventListener
('click', deleteHike);

function deleteHike(){
    fetch(itemID,{
    method: 'delete',
    })
    .then(response => {
    window.location = response.url
    })
}

// update 
document.getElementById('updateHike').addEventListener
('click', updateHike);

function updateHike(){
    fetch(itemID,{
    method: 'GET',
    })
    .then(response => {
    window.location = response.url
    })
}
