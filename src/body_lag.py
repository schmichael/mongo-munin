
name = "lagseconds"


def doData():
    try:
        status = getServerStatus(params={'repl':2})['repl']['sources'][0]['lagSeconds']
        print "%s.value %s" % (name, status)
    except KeyError, ex:
        print "Unable to find status key %s" % (str(ex),)
        sys.exit(-1)
    except IndexError:
        print "No replication sources found"
        sys.exit(-2)

def doConfig():

    print "graph_title MongoDB replication lag seconds"
    print "graph_args --base 1000 -l 0"
    print "graph_scale no"
    print "graph_vlabel connections"
    print "graph_category MongoDB"

    print name + ".label " + name





