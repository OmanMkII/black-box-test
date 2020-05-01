""" A collection of assertion statements that return True or False based on the
TestCase conditions. These are expected to be used external to the TestCase object
to allow for it to be executed and then assertions made based on if certain parts
of it are indeed relevant.
"""

FILE_CMP = "cmp {} {}\n"
GET_ERRNO = "echo $?"

@strict_types
def assert_equal_stdout(test: TestCase, expected: str):
    """ Asserts the output from a test case exactly matches the file at the given
    path.
    """
    exec = FILE_CMP.format(test.getStdout(), expected)
    output = subprocess.run(exec.split(), shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = output.stdout.decode('utf-8'), output.stderr.decode('utf-8')
    if len(stdout) == 0 and len(stderr) == 0:
        return True
    else:
        return False

@strict_types
def assert_equal_stderr(test: TestCase, expected: str):
    """ Asserts the error log from a test case exactly matches the file at the
    given path.
    """
    exec = FILE_CMP.format(test.getStderr(), expected)
    output = subprocess.run(exec.split(), shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    stdout, stderr = output.stdout.decode('utf-8'), output.stderr.decode('utf-8')
    if len(stdout) == 0 and len(stderr) == 0:
        return True
    else:
        return False

@strict_types
def retrieve_errno(test: TestCase):
    """ Retrieves the error number output from the last run command. """
    subprocess.Popen(GET_ERRNO.split(), shell=True)

    return None
