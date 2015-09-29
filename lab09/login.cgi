#!/usr/bin/perl -w

use CGI qw/:all/;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;

print header, start_html('Login Page');
warningsToBrowser(1);

$username = param('username') || '';
$password = param('password') || '';
# print "$username $password\n";
if ($username && $password) {
    if (open PASSWORD, "../accounts/$username/password"){
		$correct_password = <PASSWORD>;
		chomp $correct_password;
		if ($password eq $correct_password){
			print "$username authenticated.\n";
		} else {
			print "Incorrect password!\n";
		}
	} else {
		print "Unknown username!\n";
	}
} elsif ($username && !$password){
    print start_form, "\n";
    print "Password:\n", textfield('password'), "\n";
    print submit(value => Login), "\n";
    print hidden('username' => $username);
    print end_form, "\n";
} elsif (!$username && $password){	
    print start_form, "\n";
    print "Username:\n", textfield('username'), "\n";
    print submit(value => Login), "\n";
    print hidden('password' => $password);
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

