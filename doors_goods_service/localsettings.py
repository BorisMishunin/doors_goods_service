# -*- coding: utf-8 -*-

import os
import json
import logging
from datetime import date

from .settings import *


DATABASES = json.load(open(os.environ['GOODS_DB_CONFIG']))

services = {
    'files_service': os.environ['DOORS_SERVICE_FILES'],
}

# Loggers
try:
    LOGGING = json.load(open(os.environ['GOODS_LOGGERS']))
except Exception, e:
    logging.exception(e)