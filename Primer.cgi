#!/bin/bash

echo "X-COMP-490: ${USER}"
echo "Content-type: text/plain"
echo ""

if [ -n "${QUERY_STRING}" ] ; then

	if [ "${QUERY_STRING}" = "simple.cgi" ] ; then
	
		cat  ./${QUERY_STRING}
		
	else 
	
		echo "This application only support for a quick summary of all environment variables. QUERY is currently off."
		exit 1
	fi
		
else
	
		echo 'Available Environment Variables:'
		
		/usr/bin/env

fi

exit 0
