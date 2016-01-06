var colors = ['blue', 'cyan', 'gold', 'gray', 'green', 'magenta', 'orange',
    'red', 'white', 'yellow'];
var guesses = 0;
var finished = false;
var target;
var guess_input;

function do_game() {
    var pos = Math.floor(Math.random() * 10);
    target = colors[pos];
    
    while(!finished) {
        guess_input = prompt('I am thinking of one of these colors:\n\n' +
                             colors + '\n\n What color am I thinking of?');
        guesses += 1;
        finished = check_guess();
    }
}

function check_guess() {
    if (colors.indexOf(guess_input) == -1) {
        alert('Sorry, I don\'t recognize your color.');
        
        return false;
    }
    if (guess_input > target) {
        alert('Sorry, your guess is not correct!\n\n' +
              'Hint: your color is alphabetically higher than mine.\n\n' +
              'Please try again.');
        
        return false;
    }
    if (guess_input < target) {
        alert('Sorry, your guess is not correct!\n\n' +
              'Hint: your color is alphabetically lower than mine.\n\n' +
              'Please try again.');
        
        return false;
    }
    alert('Congratulations! You have guessed the color!\n\n' +
          'It took you ' + guesses + ' guesses to finish the game!\n\n' +
          'You can see the color in the background.');
    document.body.style.background = target;
    
    return true;
}