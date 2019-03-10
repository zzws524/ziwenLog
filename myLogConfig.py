import logging
import os
import time


class ConfigMyLog():

    @property
    def logfile(self):
        return self._logFile

    @property
    def logfilepath(self):
        return self._logFilePath


    def __init__(self,logFileName='default',withFolder=True,consoleLevel=logging.DEBUG,logLevel=logging.DEBUG):
        if withFolder:
            self._logFilePath=r'./'+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            if not os.path.exists(self._logFilePath):
                os.makedirs(self._logFilePath)
            self._logFile=os.path.abspath(self._logFilePath+r'/'+logFileName+r'.log')
        else:
            self._logFilePath=r'./'
            self._logFile=os.path.abspath(r'./'+logFileName+r'.log')
        self.__setupDefaultLevel(consoleLevel,logLevel)


    def __setupDefaultLevel(self,consoleLevel,logLevel):
        #setup console.
        console=logging.StreamHandler()
        console.setLevel(consoleLevel)
        formatterConsole = logging.Formatter('%(name)-20s: %(levelname)-8s %(message)s')
        console.setFormatter(formatterConsole)
        #setup default
        filehandler = logging.FileHandler(self._logFile,mode='w',encoding='utf8',delay=False)
        logging.basicConfig(level=logLevel,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                handlers=[filehandler,console])

    def addExtraLog(self,loggerName,logFileName='extra',logLevel=logging.CRITICAL):
        #beside default log, add extra log. the loggerName can NOT be '__name__'
        extraFile=os.path.abspath(self._logFilePath+r'/'+logFileName+r'.log')
        filehandler = logging.FileHandler(extraFile,mode='w',encoding='utf8',delay=False)
        extraFormatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')
        filehandler.setFormatter(extraFormatter)
        logging.getLogger(loggerName).handlers=[filehandler]
