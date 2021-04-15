document.addEventListener('DOMContentLoaded', function() {

    // All rows and columns as a variable
    cols = document.querySelectorAll('.col3');
        
    // When hovering over
    function on() {
        cols.forEach(col => {
            col.style.backgroundColor = 'rgba(190, 192, 189, 0.534)';
        })
    }

    // When not hovering over
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




