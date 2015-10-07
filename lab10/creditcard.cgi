#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
# print "<h2>Credit Card Validation</h2>\n";
print h2("Credit Card Validation"),"\n";

$credit_card = param("credit_card");
$credit_card =~ s/\D//g;
param('credit_card',$credit_card);
$close = param("Close");
if (defined $close){
	print "Thank you for using the Credit Card Validator.\n";
	print end_html;
	exit 0;
} else {
	print "This page checks whether a potential credit card number satisfies the Luhn Formula.\n<p></p>\n";
}

if (defined $credit_card) {
    # print validate($credit_card);
	$code = validate($credit_card);
	if ($code == 0){ # valid
		param('credit_card','');
		print start_form, "\n";
		print "<p>$credit_card is valid</p>\n";
		print "Another card number:\n";
		print textfield(-name => 'credit_card'),"\n";
	} elsif ($code == 1) { # invalid
		print start_form, "\n";
		print span({-style => 'Color: red;'},"<p><b>$credit_card is invalid</b></p>"),"\n";
		print "Try again:\n";
		print textfield(-name => 'credit_card',-value => $credit_card),"\n";
	} elsif ($code == 2) {
		print start_form, "\n";
		print span({-style => 'Color: red;'},"<p><b>$credit_card is invalid - does not contain exactly 16 digits</b></p>"),"\n";
		print "Try again:\n";
		print textfield(-name => 'credit_card',-value => $credit_card),"\n";
	}
} else {
	print start_form,"\n";
	print "Enter credit card number:\n";
	print textfield('credit_card'),"\n";
}
print submit(value => Validate),"\n";
# print defaults('Reset'),"\n";
# print submit(value => Reset),"\n";
print reset();
print submit(-name => Close,-value => Close),"\n";
print end_html;
exit 0;

for $arg (@ARGV){
	# print "$arg\n";
	print validate($arg)."\n";
}

sub luhn_checksum {
	my ($number) = @_;
	my $checksum = 0;
	my @digits = split //, $number;
	@digits = reverse @digits;
	my $multiplier;
	my $d;
	for my $index (0..$#digits){
		$multiplier = 1 + $index % 2;
		$d = $digits[$index] * $multiplier;
		# print "$d = $digits[$index] * $multiplier\n";
		$d -= 9 if $d > 9;
		$checksum += $d;
	}
	# print "$number $checksum\n";
	return $checksum;
}

sub validate {
	my ($number) = @_;
	my $credit_card = $number;
	$number =~ s/\D//g; # works for numbers with random letters?
	# print "$number\n";
	if (length($number) != 16){
		# return "$credit_card is invalid - does not contain exactly 16 digits"
		return 2;
	} elsif (luhn_checksum($number) % 10 == 0){
		# return "$credit_card is valid";
		return 0;
	} else {
		# return "$credit_card is invalid";
		return 1;
	}
}
