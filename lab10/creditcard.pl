#!/usr/bin/perl -w

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
