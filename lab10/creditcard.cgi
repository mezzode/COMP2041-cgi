#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html("Credit Card Validation"), "\n";
warningsToBrowser(1);
$credit_card = param("credit_card");
if (defined $credit_card) {
    print validate($credit_card);
}
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
		return "$credit_card is invalid - does not contain exactly 16 digits"
	} elsif (luhn_checksum($number) % 10 == 0){
		return "$credit_card is valid";
	} else {
		return "$credit_card is invalid";
	}
}
