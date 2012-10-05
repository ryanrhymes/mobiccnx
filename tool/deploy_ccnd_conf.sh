#/usr/bin/env bash
# This script calls another python script to generate ccnd.conf for
# each node in the network first. Then it deploy the generated files
# to the proper folder in different nodes automatically.
# 
# Usage: appname TOPOLOGY_FILE
#
# Liang Wang @ Dept. of Computer Science, Univ. of Helsinki, Finland
# 2012.09.26 created
#

topology=$1
pyapp="./make_ccnd_conf.py"

echo "generating ccnd.conf for nodes ..."
$pyapp $topology

echo "deploying ccnd.conf on nodes ..."
arr=`cat $topology | sed '/^$/d' | grep -v "^#" | sed 's/ -> /\n/' | sort -n | uniq`

for x in $arr; do
    ssh -o BatchMode=yes -o StrictHostKeyChecking=no $x "if [ ! -d /var/tmp/ccnd ]; then mkdir /var/tmp/ccnd; fi; chgrp cone /var/tmp/ccnd; chmod 0770 /var/tmp/ccnd; exit;" &
    scp ./tmp_confs/ccnd.conf.$x $x:/var/tmp/ccnd/ccnd.conf.$x
done

echo "Done!"