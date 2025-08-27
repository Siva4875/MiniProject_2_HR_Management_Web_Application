import logging, os, sys

def get_logger(name: str = "orangehrm"):
    """
    Creates and returns a logger instance.
    
    Args:
        name (str): Logger name (default = "orangehrm").
    
    Returns:
        logging.Logger: Configured logger object.
    """
    # Get logger by name
    logger = logging.getLogger(name)

    # If logger already has handlers, just return it
    # (prevents duplicate logs if logger is called multiple times)
    if logger.handlers:
        return logger

    # Set default logging level
    logger.setLevel(logging.INFO)

    # Define log format: timestamp | log level | logger name | message
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # ---- Stream Handler (logs to console/stdout) ----
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)

    # ---- File Handler (logs to reports/run.log file) ----
    # Ensure "reports" directory exists
    log_path = os.path.join(os.getcwd(), "reports", "run.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    fh = logging.FileHandler(log_path)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger
