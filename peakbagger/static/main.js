

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


// update 
document.getElementById('updateHike').addEventListener
('click', updateHike);

function updateHike(){
    fetch('hike/{{ hike.id }}',{
    method: 'GET',
    })
    .then(response => {
    window.location = response.url
    })
}


// delete
document.getElementById('deleteHike').addEventListener
('click', deleteHike);

function deleteHike(){
    fetch('hike/{{ hike.id }}',{
    method: 'delete',
    })
    .then(response => {
    window.location = response.url
    })
}

