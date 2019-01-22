import logging


def initDefaultLog(logFile, level=logging.DEBUG):
    #setup console.
    console=logging.StreamHandler()
    console.setLevel(level)
    formatterConsole = logging.Formatter('%(name)-20s: %(levelname)-8s %(message)s')
    console.setFormatter(formatterConsole)
    #setup default
    filehandler = logging.FileHandler(logFile,mode='w',encoding='utf8',delay=False)
    logging.basicConfig(level=level,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            handlers=[filehandler,console])

def addExtraLog(name,logFile,formatter=logging.Formatter('%(message)s'),level=logging.DEBUG):
    #assign different name other than "__name__"
    handler=logging.FileHandler(logFile,mode='w',encoding='utf8',delay=False)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers=[handler]
