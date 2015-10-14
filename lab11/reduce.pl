#!/usr/bin/perl -w

sub reduce (&@) {
    my $code = \&{shift @_};
    @list = @_;
    $a = shift @list;
    while (@list) {
        $b = shift @list;
        # print "$a $b\n";
        $a = $code->($a,$b);
    }
    return $a;
}

$sum = reduce { $a + $b } 1 .. 10;

print "$sum\n";
