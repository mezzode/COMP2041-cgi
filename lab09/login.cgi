#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html('Login Page');
warningsToBrowser(1);

$username = param('username') || '';
$password = param('password') || '';

if ($username && $password) {
    print "$username authenticated.\n";
} elsif ($username && !$password){
    print start_form, "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
} elsif (!$username && $password){	
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
} else {
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print end_form, "\n";
}
print end_html;
exit(0);

