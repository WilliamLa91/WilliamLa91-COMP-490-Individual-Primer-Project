#!/bin/bash

echo "X-COMP-490: ${USER}"
echo "Content-type: text/plain"
echo ""

if [ -n "${QUERY_STRING}" ] ; then
if [ "${QUERY_STRING}" != "simple.cgi" ] ; then
		echo "This application only support for a quick summary of all environment variables."
        exit 1;
fi
	cat  ./${QUERY_STRING}
		
fi
echo 'Environment Variables:'
/usr/bin/env



exit 0
