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

echo "Done!"