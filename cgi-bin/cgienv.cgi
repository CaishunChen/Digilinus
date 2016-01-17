#!/bin/sh

echo Content-type: text/html
echo ""

/usr/bin/cat << EOM

<html>
<head><title>cgienv</title>
</HEAD>
<body>
<p>
<pre>
EOM

/usr/bin/env

cat << EOM
</pre>
</p>
<p>
<pre>
EOM

/usr/games/fortune

cat << EOM
</pre>
</p>
</body>
</html>
EOM
