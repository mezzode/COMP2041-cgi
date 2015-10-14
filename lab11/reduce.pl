#!/usr/bin/perl -w


sub reduce (&@) {
    my $code = \&{shift @_};
    @list = @_;
    for $i (1..$#list) {
        $a = $list[$i-1];
        $b = $list[$i];
        print "$a $b\n";
        $code->($a,$b);
    }
}
$sum = reduce { $a + $b } 1 .. 10;
print $sum;
