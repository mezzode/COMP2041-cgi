#!/usr/bin/perl -w

sub reduce (&@) {
    my $code = \&{shift @_};
    my @list = @_;
    $a = shift @list;
    while (@list) {
        $b = shift @list;
        # print "$a $b\n";
        $a = $code->($a,$b);
    }
    return $a;
}

$sum = reduce { $a + $b } 1 .. 10;
$min = reduce { $a < $b ? $a : $b } 5..10;
$maxstr = reduce { $a gt $b ? $a : $b } 'aa'..'ee';
$concat = reduce { $a . $b } 'J'..'P';
$sep = '-';
$join = reduce { "$a$sep$b" }  'A'..'E';
print "$sum $min $maxstr $concat $join\n";
