import logging
from logging.handlers import RotatingFileHandler

# Constants
logging_format = logging.Formatter("%(message)s")

# Loggers and Logging Files
funnel_logger = logging.getLogger("FunnelLogger")
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler("audits.log", maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

creds_logger = logging.getLogger("CredsLogger")
creds_logger.setLevel(logging.INFO)
creds_handler = RotatingFileHandler("cmd_audits.log", maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(creds_handler)

# Emulated Shell

# SSH SERVER + Sockets

# Provision SSH-based client
