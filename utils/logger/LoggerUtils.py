import logging
import logging.handlers
import os.path
import pathlib


def set_logger(name):
    """
    Method to set file and stream handler and generate log file.
    log file will generate at current folder with name "log-<YYMMDD_HHMMSS>.log"
    """
    filename_startswith = 'test_'
    _logger = logging.getLogger(name or __name__)
    _logger.setLevel(logging.INFO)

    # File handler to move stdout to log file
    # log_file_name = filename_startswith + datetime.now().strftime("%y%m%d_%H%M%S") + ".log"
    # res_dir_path = create_res_dir()
    # file = logging.handlers.RotatingFileHandler(filename=os.path.join(res_dir_path, log_file_name))
    # file_format = logging.Formatter("%(asctime)s [%(levelname)s]: %(name)s: %(message)s")
    # file.setLevel(logging.DEBUG)
    # file.setFormatter(file_format)

    # Stream handler to print debug logs in stdout
    stream = logging.StreamHandler()
    stream_format = logging.Formatter("%(asctime)s [%(levelname)s]: %(name)s: %(message)s")
    stream.setLevel(logging.DEBUG)
    stream.setFormatter(stream_format)

    # if (_logger.hasHandlers()):
    #     _logger.handlers.clear()
    # Adding all handlers to log file
    # _logger.addHandler(file)
    _logger.addHandler(stream)
    return _logger

def create_res_dir():
    root_path = pathlib.Path(__file__).parent.parent.parent
    res_path = os.path.join(root_path, "test_results")
    return res_path
