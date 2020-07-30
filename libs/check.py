from urllib import request

from libs.logger import logger
from config import domain_check_api

def is_available(domain):
    """Check if the domain name is registered"""

    api = domain_check_api.format(domain)
    result = request.urlopen(api.format(domain)).read().decode('utf-8')
    logger.debug(result)
    if '<original>210' in result:
        # domain is available
        return True
    elif '<original>211' in result:
        # domain is not available
        return False
    else:
        logger.warning('api Forbidden')
        return False
