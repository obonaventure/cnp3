# Special filter to sort announce by originating AS.
# It use version of route_bto that has filter capabilities
# and then reconvert the messages in to binary to inject
# it in Xorp, See the route_btoa patch.

day=20091028
hour=0;
minute=00;
AS=31500
while [ $hour -lt 24 ];
do
	while [ $minute -lt 60 ];
	do
		#wget http://archive.routeviews.org/bgpdata/2009.10/UPDATES/updates.$day.`printf  "%02d%02d\n" $hour $minute`.bz2;
		/usr/local/sbin/route_btoa updates.$day.`printf  "%02d%02d\n" $hour $minute` -a $AS | /usr/local/sbin/route_atob > updates.$day.`printf  "%02d%02d\n" $hour $minute`.AS$AS;
		let minute=$minute+15;
	done
	let hour=$hour+1;
	minute=0;
done
