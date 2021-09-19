import datetime
from functools import wraps
import os, sys, logging


def create_log_file(log_file_name):
    cwd = os.getcwd()
    folder = 'Logs'
    CHECK_FOLDER = os.path.isdir(folder)
    newPath = os.path.join(cwd, folder)

    try:
        # If folder doesn't exist, then create it.
        if not CHECK_FOLDER:
            os.mkdir(newPath)
        logging.basicConfig(filename='{}/{}'.format(newPath, log_file_name), level=logging.DEBUG)
    except Exception as e:
        return "Error while creating log file"


def moniter(function):
    try:
        @wraps(function)
        def wrapper(*args, **kwargs):
            s = datetime.datetime.now()
            # ip_address = "{}".format(request.remote_addr)
            # user_agent = "{}".format(request.user_agent)
            called_fuction_name = "{}".format(function.__name__)
            _ = function(*args, **kwargs)

            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            called_arguments = ",\n".join(args_repr + kwargs_repr)

            # called_arguments = dict(kwargs.items())
            called_function_arguments = '{}'.format(called_arguments)
            e = datetime.datetime.now()
            exe_time = "{}".format((e - s))
            called_function_size = "{} Bytes".format(sys.getsizeof(function))

            logging.debug("Start time : {}".format(s))
            logging.debug("Called Fuction Name : {}".format(called_fuction_name))
            logging.debug("Called Function Arguments : {}".format(called_function_arguments))
            logging.debug("Memory : {}".format(called_function_size))
            logging.debug("Execution Time : {}".format(exe_time))
            logging.debug("End Time : {}\n".format(e))

            return _

        return wrapper

    except Exception as e:
        logging.error("ERROR : {}".format(str(e)))
