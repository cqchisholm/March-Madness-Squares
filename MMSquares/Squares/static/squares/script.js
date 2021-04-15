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
    
})




