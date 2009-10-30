day=20091028
hour=0;
minute=00;
while [ $hour -lt 24 ];
do
	while [ $minute -lt 60 ];
	do
		#wget http://archive.routeviews.org/bgpdata/2009.10/UPDATES/updates.$day.`printf  "%02d%02d\n" $hour $minute`.bz2;
		bunzip2 updates.$day.`printf  "%02d%02d\n" $hour $minute`.bz2;
		let minute=$minute+15;
	done
	let hour=$hour+1;
	minute=0;
done
