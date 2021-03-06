#
# Get CVE list:
# wget https://cve.mitre.org/data/downloads/allitems.csv
#
# Get Detectify modules list:
# 1/ login on Detectify
# 2/ Perform the following request:
# POST /ajax/application_load/50bdd32f114d2e889f29f31e3e79a1ac/
# with body: navigation[mode]=modules
# 3/ save the json returned in detectify-modules.json
#

import sys
import json
import csv
import re
import argparse
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("-s","--search",help="search a specific keyword")
parser.add_argument("-l","--limit",help="display only n first results")
parser.add_argument("-d","--detectify",help="display only when a Detectify module is available", action="store_true")
parser.parse_args()
args = parser.parse_args()

if args.search:
    search = args.search
else:
    search = ''

if args.limit:
    limit = int(args.limit)
else:
    limit = 0

if args.detectify:
    detectify = 1
else:
    detectify = 0

def search_module( cve, search, detectify ):
    if search is '' or search.lower() in cve[2].lower():
        for mod in t_modules:
            if cve[0] in mod['moduleName']:
                return [ mod['moduleName'], mod['userName'], mod['dateAdded'] ]
        return 1
    return 0

with open('detectify-modules.json') as json_file:
    j_detectify = json.load(json_file)
    t_modules = j_detectify['data']['widgets']['AllModulesList']['props']['changed']['modules']

with open('allitems.csv') as csv_file:
    i = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    for cve in reversed(list(csv_reader)):
        if "** RESERVED **" not in cve[2]:
            r = search_module( cve, search, detectify )
            if r != 0:
                if detectify == 0 or type(r) is list:
                    i = i + 1
                    #sys.stdout.write("https://cve.mitre.org/cgi-bin/cvename.cgi?name=%s - %s..." % (cve[0],cve[2][:150]))
                    sys.stdout.write("https://cve.mitre.org/cgi-bin/cvename.cgi?name=%s - %s..." % (cve[0],cve[2][:150]))
                if type(r) is list:
                    sys.stdout.write( colored(" -> %s - %s - %s" % (r[0],r[1],r[2]),"red") )
                if detectify == 0 or type(r) is list:
                    sys.stdout.write("\n")
            if limit and i >= limit:
                break
