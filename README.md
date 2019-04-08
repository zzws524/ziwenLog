# myLogConfig
Configured logging for python script.

Loggers are never instantiated directly, but always through the module-level function logging.getLogger(name). Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.

Even though, I prefer to wrap the config into a class.


#how to use:
import logging
from ziwenLog import myLogConfig

class A:
    def __init__(self):
        self.logger=logging.getLogger(__name__)
        self.logger.debug('class a init')

if __name__=='__main__':
    myLogConfig=myLogConfig.ConfigMyLog(logFileName='test')
    logger=logging.getLogger(__name__)
    logger.info('start main')
    tmpA=A()

