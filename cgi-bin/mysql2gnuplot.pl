#!/usr/bin/perl -W

# DigiTemp MySQL plott script
# 2004 by Tomas Wredendal <tomwre@netscape.net>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# -------------------------[ HISTORY ]-------------------------------------
# 2006-03-17 twl - Modified to fetch data 2 gnuplot...
# 2004-09-22 twl - Plott script to suite my needs...
#
# -------------------------------------------------------------------------
# CREATE table digitemp (
#   dtKey int(11) NOT NULL auto_increment,
#   time timestamp NOT NULL,
#   temp1 decimal(3,1) NOT NULL,
#   temp2 decimal(3,1) NOT NULL,
#   PRIMARY KEY (dtKey),
#   KEY time_key (time)
# );
#
# GRANT SELECT,INSERT ON digitemp.* TO digitemp@localhost
# IDENTIFIED BY 'password';
#
# -------------------------------------------------------------------------

use strict;
use DBI();


# Database info
my $db_name     = "digitemp:192.168.0.8";
my $db_user     = "digitemp";
my $db_pass     = "digitemp";

# # of temperatures per sample (number of sensors)
my $sensors = 2;
my $samples_per_hour = 2;

# How many days to track (back).
my $days = 7;


# No need to change anything below this line
# -----------------------------------------------------------



# --------------------------------[ MAIN CODE ]----------------------------


my ($matrix_ref); # reference to array of references

# Connect to the database
my $dbh = DBI->connect("dbi:mysql:$db_name", "$db_user", "$db_pass")
          or die "I cannot connect to dbi:mysql:$db_name as $db_user - $DBI::errstr\n";

#my $sql="SELECT * FROM digitemp WHERE (time > DATE_SUB(NOW(),INTERVAL '$days' DAY)) ORDER #BY time DESC";
my $sql="SELECT time, temp1, temp2 FROM digitemp WHERE (time > DATE_SUB(NOW(),INTERVAL '$days' DAY)) ORDER BY time DESC";
# Now retrieve data from the table.
$matrix_ref = $dbh->selectall_arrayref($sql);

# Disconnect from the database.
$dbh->disconnect();

# determine dimension of matrix
my ($rows) = (!defined ($matrix_ref) ? 0 : scalar (@{$matrix_ref}));
my ($cols) = ($rows == 0 ? 0 : scalar (@{$matrix_ref->[0]}));

# test print 
for (my $i = 0; $i < $rows; $i++)
{
    my ($delim) = " ";
    for (my $j = 0; $j < $cols; $j++)
    {
		print $delim . $matrix_ref->[$i][$j];
		$delim = " ";
    }
    print "\n";
}
   



