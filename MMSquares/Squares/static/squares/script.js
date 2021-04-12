document.addEventListener('DOMContentLoaded', function() {

    let cells = document.querySelectorAll('.col1');

    // When hovering over
    function on() {
        cells.forEach(cell => {
            cell.style.backgroundColor = 'rgba(190, 192, 189, 0.534)';
        })
    }

    // When not hovering over
    function off() {
        cells.forEach(cell => {
            cell.style.backgroundColor = 'white';
        })
    }


    // For each cell in the row change the background color when hovered over
    cells.forEach(cell => {
        cell.addEventListener('mouseenter', on)
        cell.addEventListener('mouseleave', off)
    })



})




