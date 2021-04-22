document.addEventListener('DOMContentLoaded', function() {

    console.log(player_count);
    // All rows and columns as a variable
    let cols = document.querySelectorAll('.pool-table td');
        
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
    for (i = 1; i <= player_count; i++) {
        // Round 1
        var RWorth = document.querySelector(`#R1Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R1-games-won-${i}`).innerHTML;
        document.querySelector(`#R1-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
        // Round 2
        var RWorth = document.querySelector(`#R2Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R2-games-won-${i}`).innerHTML;
        document.querySelector(`#R2-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
        // Round 3
        var RWorth = document.querySelector(`#R3Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R3-games-won-${i}`).innerHTML;
        document.querySelector(`#R3-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
        // Round 4
        var RWorth = document.querySelector(`#R4Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R4-games-won-${i}`).innerHTML;
        document.querySelector(`#R4-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
        // Round 5
        var RWorth = document.querySelector(`#R5Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R5-games-won-${i}`).innerHTML;
        document.querySelector(`#R5-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
        // Round 6
        var RWorth = document.querySelector(`#R6Worth`).innerHTML;
        var R_Games_Won = document.querySelector(`#R6-games-won-${i}`).innerHTML;
        document.querySelector(`#R6-amount-won-${i}`).innerHTML = RWorth * R_Games_Won;
    }

})

