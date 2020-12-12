import pytest
import logging

log = logging.getLogger()

def test_logger():
    log.info("info massage!")
    log.debug("debug massage!")
    log.error("error message!")
    log.critical("critical message!")
    log.warning("warning message!")
    print("print message!")

def test_2():
    logging.debug('debug 信息')
    logging.info('info 信息')
    logging.warning('warning 信息')
    logging.error('error 信息')
    logging.critical('critial 信息')