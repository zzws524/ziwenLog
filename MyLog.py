import time
import os
import logging

class Log(object):
    def __init__(self,logName='defaultlog1',writeLogToLocal = False):
        self.resultFolder = None
        self.logger = logging.getLogger(logName)
        if writeLogToLocal:
            self._createResultFolder()
            myfilename = os.path.abspath(self.resultFolder + r'/' + __name__ + r'.log')
            filehandler = logging.FileHandler(myfilename,mode='w',encoding='utf8',delay=False)
            logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    handlers=[filehandler])
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        if writeLogToLocal == False:
            logging.basicConfig(level=logging.INFO,handlers=[console])
        else:
            self.logger.addHandler(console)


    def _createResultFolder(self):
        self.resultFolder = r'./' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        if not os.path.exists(self.resultFolder):
            os.makedirs(self.resultFolder)