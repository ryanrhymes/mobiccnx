#!/usr/bin/env python
# 
# This script reads topology file as its input, and generate
# corresponding config files for each nodes in the experiment. The
# generated config files are supposed to help CCNx nodes construct
# the network topology needed in an experiment.
#
# Usage: appname TOPOLOGY_FILE
#
# Liang Wang @ Dept. of Computer Science, Univ. of Helsinki, Finland
# 2012.09.26 created
#

import re
import os
import sys
import time

class ConfigReader(object):
    """This class read the topology file, generate ccnd conf files."""

    def __init__(self, ifn, conf_dir):
        """
        ifn: topology file;
        conf_dir: directory to store generated config files;
        """
        self.topology = self.read_topology(ifn)
        self.conf_dir = conf_dir
        if not os.path.exists(conf_dir):
            os.mkdir(conf_dir)
        pass

    def read_topology(self, ifn):
        """Read in the topology file.
        ifn: topology file
        return: a dict contains router as key, and links as value
        """
        topology = {}
        # Get all the vrouters in the file, then filter
        for line in open(ifn, 'r').readlines():
            line = line.strip()
            if line.startswith('#') or len(line) == 0:
                continue

            m = re.search(r"(\S+)\s*->\s*(\S+)\s*", line).groups()
            vr1, vr2 = sorted(m)
            link = tuple([vr1,vr2])
            topology[vr1] = topology.get(vr1, set())
            topology[vr1].add(link)
            topology[vr2] = topology.get(vr2, set())
            topology[vr2].add(link)
        return topology

    def make_ccnd_conf(self):
        """Make ccnd config files for all the nodes in a network.
        return: None"""
        for router in sorted(self.topology.keys()):
            tstr = self.make_router_conf(router, self.topology)
            tfh = open(self.conf_dir + "/ccnd.conf." + router, "wb")
            tfh.write(tstr)
            tfh.close()
        pass

    def make_router_conf(self, router, topology):
        """Given a router and topology, generate config string.
        router: router name;
        return: config string;"""
        conf_str = "# ccnd.conf file in mobiccnx experiments\n" \
                 + "# host name: " + router + "\n" \
                 + "# created at " + time.ctime() + "\n\n"
        
        for nb in self.get_neighbors(router, topology):
            conf_str += "add ccnx:/greed/mobiccnx udp %s 9695\n" % nb

        conf_str += "\n\n" \
                  + "# The multicast address 224.0.23.170 is assigned by IANA for use with CCNx.\n" \
                  + "# We use this route to dispatch regular CCNx interest without greedy routing.\n\n" \
                  + "add ccnx:/mobiccnx udp 224.0.23.170 9695\n" \
                  + "\n"

        return conf_str

    def get_neighbors(self, router, topology):
        """Given a router and network topology, return all its
        neighbours.
        router: router name;
        topology: a dict contains network topology;
        return: a set contains router's neighbours;
        """
        r = set()
        for x, y in topology[router]:
            if router == x:
                r.add(y)
            elif router == y:
                r.add(x)
        return r

pass


if __name__=="__main__":
    config = ConfigReader(sys.argv[1], "tmp_confs")
    config.make_ccnd_conf()
    sys.exit(0)
