import logging
import time


class Loger:

    def __init__(self, logger, file_level=logging.INFO):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)


        curr_time=time.strftime('%Y-%m-%d-%H-%M')
        self.filename='..//logs//loger'+curr_time+'.log'
        fh=logging.FileHandler(self.filename, mode='w')
        fmt=logging.Formatter("%(asctime)s::%(levelname)s::%(name)s::%(message)s" )
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)