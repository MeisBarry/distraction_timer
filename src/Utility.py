import sys

def print_flush(in_str):
    """ Uses the '\r' trick to re-write stdout

    Arguments:
        in_str (str): The string to pring

    """
    sys.stdout.write("\r{out_str}".format(out_str=in_str))
    sys.stdout.flush()
