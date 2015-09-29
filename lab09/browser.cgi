#!/bin/sh
echo Content-type: text/html
echo

host_address=`host $REMOTE_ADDR | sed 's/.* //' | sed 's/.$//'` # host command output is in different format
# host_address=`host $REMOTE_ADDR 2>&1|grep Name|sed 's/.*: *//'`

cat <<eof
<!DOCTYPE html>
<html lang="en">
<head>
<title>Webserver IP, Host and Software</title>

</head>
<body>
Your browser is running at IP address: <b>$REMOTE_ADDR</b>
<p>
Your browser is running on hostname: <b>$host_address</b>
<p>
Your browser identifies as: <b>$HTTP_USER_AGENT</b>

</body>
</html>
eof
