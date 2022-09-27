

// homepage 
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

// search 
document.getElementById('searchHike').addEventListener
('click', searchHike);

function searchHike(){
fetch('/',{
    method: 'GET',
})
.then(response => {
    window.location = response.url
    })
}

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

// delete hike
let itemID = document.getElementById('deleteHike').value
itemID = `/hike/${itemID}`

document.getElementById('deleteHike').addEventListener
('click', deleteHike);

function deleteHike(){ 
    fetch(itemID,{
    method: 'DELETE',
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
    method: 'PUT',
    })
    .then(response => {
    window.location = response.url
    })
}
