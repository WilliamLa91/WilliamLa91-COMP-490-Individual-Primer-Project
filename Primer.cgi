#!/bin/bash

echo "X-COMP-490: ${USER}"
echo "Content-type: text/html"
echo ""

if [ -n "${QUERY_STRING}" ] ; then

	if [ "${QUERY_STRING}" = "Primer.cgi" ] ; then
	
		cat  ./${QUERY_STRING}
		
	else 
	
		echo "This application only support for a quick summary of all environment variables. QUERY is currently off. Use ?Primer.cgi to cat"
		exit 1
	fi
		
else
	
		echo 'This is just a fake copy of csun website. Environment Variables are at the bottom.'
		/usr/bin/curl -o /tmp/csun http://www.csun.edu
		cat /tmp/csun
		echo 'Available Environment Variables:'
		echo ''
		echo '<pre>'
		/usr/bin/env
		
fi

exit 0
