document.addEventListener('DOMContentLoaded', function() {

    // All rows and columns as a variable
    cols = document.querySelectorAll('.pool-table td');
        
    // When hovering over
    function on() {
        // Get class name of <td> that the user is hovering over
        var cn = this.className;
        // Select all <td>'s that have that class name (the entire column)
        var column = document.querySelectorAll(`.${cn}`);
        // Change background color of highlighted column
        column.forEach(col => {
            col.style.backgroundColor = 'rgba(190, 192, 189, 0.534)';
        })
    }

    // When not hovering over leave column with original background color
    function off() {
        cols.forEach(col => {
            col.style.backgroundColor = '';
        })
    }

    // For each cell in the row change the background color when hovered over
    cols.forEach(col => {
        col.addEventListener('mouseover', on)
        col.addEventListener('mouseout', off)
    })


    // Update the total amount won for each round per player
    R1Worth = document.querySelector('#R1Worth').innerHTML;
    R1Games = document.querySelector('#R1Games').innerHTML;
    R2Worth = document.querySelector('#R2Worth').innerHTML;
    R2Games = document.querySelector('#R2Games').innerHTML;
    R3Worth = document.querySelector('#R3Worth').innerHTML;
    R3Games = document.querySelector('#R3Games').innerHTML;
    R4Worth = document.querySelector('#R4Worth').innerHTML;
    R4Games = document.querySelector('#R4Games').innerHTML;
    R5Worth = document.querySelector('#R5Worth').innerHTML;
    R5Games = document.querySelector('#R5Games').innerHTML;
    R6Worth = document.querySelector('#R6Worth').innerHTML;
    R6Games = document.querySelector('#R6Games').innerHTML;

    document.querySelector('#R1Amount').innerHTML = R1Worth * R1Games;
    
})




