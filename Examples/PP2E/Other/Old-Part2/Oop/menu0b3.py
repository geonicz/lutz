from security import allow                         # outside func, 'from'

def interact_dict(menu, logFlag=0, secFlag=0):     # menu + extension flags
    import os, logger                              # utility modules
    user = os.environ['USER']
    if secFlag:                                    # any allowed?
        for name in menu.keys():
            if allow(name, user):
                break
        else:
            print "You�re not authorized for any menu selections"
            return
    while 1:
        for name in menu.keys():                    # show legals
            if (not secFlag) or allow(name, user):
                print '\t' + name
        tool = raw_input('?')
        if logFlag:
            logger.record(user, tool)              # log it, validate it
        if secFlag and not allow(tool, user):
            print "You're not authorized for this selection - try again"
        else:
            try:
                menu[tool]()                       # run function
            except KeyError:              
                print 'what? - try again'          # key not found
