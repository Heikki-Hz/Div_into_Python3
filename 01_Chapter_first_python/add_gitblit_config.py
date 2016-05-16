#/usr/bin/python

import os
import fnmatch

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

for filename in iterfindfiles(r".", "config"):
    print(filename)
    f = open(filename, "aw")
    p = f.tell()
    print(p)
    f.write(''' 
[gitblit]
    description = 
    originRepository =
    owner = admin
    acceptNewPatchsets = true
    acceptNewTickets = true
    mergeTo = master
    useIncrementalPushTags = false
    allowForks = true
    accessRestriction = VIEW
    authorizationControl = NAMED
    verifyCommitter = false
    showRemoteBranches = false
    isFrozen = false
    skipSizeCalculation = false
    skipSummaryMetrics = false
    federationStrategy = FEDERATE_THIS
    isFederated = false
    gcThreshold = 500k
    lastGC = 1970-01-01T08:00:00+0800
    ''')

    f.close()
