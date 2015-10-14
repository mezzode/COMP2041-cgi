#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print <<eof;
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="guess_number.css" rel="stylesheet">
    <title>A Guessing Game Player</title>
</head>
<body>
eof

warningsToBrowser(1);

$guess = param('guess');
$max = param('max');
$min = param('min');
$higher = param('higher');
$lower = param('lower');
$correct = param('correct');

$game_over = 0;

if (not defined $max){
    $max = 100;
}
if (not defined $min){
    $min = 1;
}

if (defined $higher){
    $min = $guess + 1;
} elsif (defined $lower){
    $max = $guess - 1;
} elsif (defined $correct){
    $game_over = 1;
}

if (0){# (defined $number_to_guess and defined $guess) {
    $guess =~ s/\D//g;
    $number_to_guess =~ s/\D//g;
    if ($guess == $number_to_guess) {
        print "You guessed right, it was $number_to_guess.\n";
        $game_over = 1;
    } elsif ($guess < $number_to_guess) {
        print "Its higher than $guess.\n";
    } else {
        print "Its lower than $guess.\n";
    }
} elsif (0) {
    $number_to_guess = 1 + int(rand $max_number_to_guess);
    print "I've  thought of number 0..$max_number_to_guess\n";
}

$guess = int(($min + $max)/2);

if ($game_over) {
print <<eof;
    <form method="POST" action="">
        I win!!!!
        <input type="submit" value="Play Again">
    </form>
eof
} else {
print <<eof;
    <form method="POST" action="">
        My guess is: $guess
        <input type="submit" value="Higher?" name="higher">
        <input type="submit" value="Correct?" name="correct">
        <input type="submit" value="Lower?" name="lower">
        <input type="hidden" name="guess" value="$guess">
        <input type="hidden" name="min" value="$min">
        <input type="hidden" name="max" value="$max">
    </form>
eof
}

print <<eof;
</body>
</html>
eof
