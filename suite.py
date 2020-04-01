#!/usr/bin/python3
"""
This test suite has been designed for black box testing from a Unix/Linux command
line environment, where all input can be given directly from files locally, and
all output can be either ignored, ensured null, or compared to existing files
on an all-or-nothing style test.

This has been based on Joel's CSSE2310 marking style (University of Queensland),
where everything was looking for reasons to fail you - unfortunately it was
internal and I was unable to fork it.

TODO: allow forking inside programs
TODO: launch programs in parallel, account for local networking
"""

import subprocess
import filecmp
import os

from colorama import Fore, Style

VERSION = "1.0"

# Static environment types (expand later if necessary)
MAKEFILE = "make"
MAKECLEAN = "make clean"

# Shell commands
CHECK_MAKE_A = "du -b errlog"               # check file data
CHECK_MAKE_B = "cut -f1 output"             # get file size (should be '\n')
REMOVE = "rm"                               # delete error file
GET_ERRNO = "echo $?"                       # get the last exit code (errno)

SPACE = " "

class TestCase():
    """ An instance test case existing within a multitude of tests.

    For each case, initialise the class with a test name, a command line input,
    input to stdin (if relevant), expected stdout/stderr (if any), maximum time
    out, an expected exit status (if non-zero), and if the outputs should be
    preserved or not (defaults to delete).

    Each test will be run from the shell and tested accoring to the correct exit
    condition, the correct collective stdout, and the correct collective stderr.
    In the case that no files are selected for stdout/stderr, the test will presume
    them irrelevant - for cases where no output is expected, please use an empty
    file.
    """

    # Information
    _name = None

    # Input/Output
    _testStdin = None
    _status = None

    # Expected Data
    _stdout = None
    _stderr = None

    # Cleanup flags
    _teardown = None

    def __init__(self, name: str, input: str, timeout: int, stdin: str = None,
            errno: int = 0, stdout: str = "/dev/null", stderr: str = "/dev/null"):
        """ Sets up the test case by initialising inputs and outputs relying on
        third party text inputs, prepping the suite to compare input and outputs
        for this case.
        """
        self._name = name
        # Expected
        self._input = input.split()
        # self._input = input + SPACE + "> {}".format(stdout) + SPACE + "2> {}".format(stderr)
        self._errno = errno
        self._stdout = stdout
        self._stderr = stderr
        # Actual
        self._status = -1
        # TODO: put results in ./deleteme instead
        self._output = "{}.out".format(self._name)
        self._errlog = "{}.err".format(self._name)

    def _testStdout(self) -> bool:
        """ Tests the stdout saved to local files. """
        with open(self._output, "r") as stdout, open(self._stdout, "r") as expected:
            if stdout.read() != expected.read():
                # print("  Incorrect STDOUT:\n")
                # print("  {}\n".format(stdout.read()))
                return False
            else:
                return True

    def _testStderr(self) -> bool:
        """ Tests the stderr saved to local files. """
        with open(self._errlog, "r") as stderr, open(self._stderr, "r") as expected:
            if stderr.read() != expected.read():
                # print("  Incorrect STDERR:\n")
                # print("  {}\n".format(stderr.read()))
                return False
            else:
                return True

    def _testErrno(self) -> bool:
        """ Tests the final exit code. """
        if self._errno != self._status:
            print("\tIncorrect exit code:", self._status)
            return False
        else:
            return True

    def run(self) -> None:
        """ Executes the script locally and saves all I/O to be tested later. """
        p = subprocess.Popen(self._input,
                stdout=open(self._output, "a"), stderr=open(self._errlog, "a"))
        output, error = p.communicate()
        p.wait()
        self._status = p.returncode

    def teardown(self) -> None:
        """ Destroys local copies unless explicitly labelled to save. """
        if self.teardown:
            subprocess.call(
                    (REMOVE + SPACE + "{}.out".format(self._name)).split())
            subprocess.call(
                    (REMOVE + SPACE + "{}.err".format(self._name)).split())


class TestGroup:
    """ A collection of tests that are similarly grouped tests, usually designed
    to differentiate between executable groups such as the main program and lower
    level tests on programs later piped to, etc.
    """

    _name = None
    _tests = [None]
    _results = [None]

    def __init__(self, name, tests):
        self._name = name
        self._tests = tests
        self._results = [None for _ in tests]

    def runAll(self):
        """ Execute all existing tests and stores data locally. """
        for i, test in enumerate(self._tests):
            self._results[i] = test.run()
        return self._tests

    def runTest(self, name: str):
        """ Run a specific test that matches the given name. """
        for t in self._tests:
            if t._name == name:
                return t.run()
        return None

    def explainAll(self):
        # TODO: explain all tests, do not run
        return None

    def explainTest(self, name: str):
        # TODO: explain one test, do not run
        return None

    def teardownAll(self):
        """ Removes all temporary data """
        for t in self._tests:
            t.teardown()


class TestSuite:
    """ The main test suite for self set of tests, operates by running shell
    commands to compile the program and ensuring proper compilation, then comparing
    each output directly to evaluate their outputs.
    """

    # Coloured for your enjoyment
    RESULTS = {
        "PASS!": '\033[1m' + f"{Fore.GREEN}PASS!{Style.RESET_ALL}" + '\033[0m',
        "FAIL.": '\033[1m' + f"{Fore.YELLOW}FAIL.{Style.RESET_ALL}" + '\033[0m',
        "ERROR": '\033[1m' + f"{Fore.BLUE}ERROR{Style.RESET_ALL}" + '\033[0m'
    }

    # Numbers
    _total = 0
    _passed = 0

    # Existing tests
    _groups = [None]

    def __init__(self, groups):
        self._groups = [None] * len(groups)
        self._total = 0
        for i, t in enumerate(groups):
            self._groups[i] = t
            self._total += len(t._tests)

    def _printSetup(self, name: str, size: int = 80) -> None:
        """ Prints a (semi) fancy welcome and description. """
        print("-" * size)
        print(name + "\n\nA bash terminal test environment for simple black box testing."
                + "\nAuthor: Eamon O'Brien\nVersion: " + VERSION)
        print("-" * size)

    def _printResultLine(self, testName, result, dump,
            size: int = 80, isErrno: bool = False):
        """ Prints the result of the test neatly with an error dump if given. """
        # spaced pass/fail
        output = testName + " " * (size - len(testName) - len(result) - 2)
        output += TestSuite.RESULTS.get(result)
        print(output)
        # print relevant results
        if isErrno:
            # "dump" is actually errno in this case
            print("\tExited with status {}\n".format(dump))
        elif dump is not None:
            # Incorrect outputs
            with open(dump, "r") as d:
                print("  Expected:", d.read())

    def _printTestResult(self, result: TestCase) -> None:
        """ Checks stdout, stderr, and exit code to ensure the program was run
        correctly.
        """
        if not result._testStderr():
            TestSuite._printResultLine(self, result._name, "FAIL.", result._stderr)
        elif not result._testStdout():
            TestSuite._printResultLine(self, result._name, "FAIL.", result._stdout)
        elif not result._testErrno():
            TestSuite._printResultLine(self, result._name, "FAIL.",
                result._status, isErrno = True)
        else:
            self._passed += 1
            TestSuite._printResultLine(self, result._name, "PASS!", None)

    def _printFinal(self, size: int = 80) -> None:
        """ Print a summary of the test results. """
        print("-" * size)
        print("{} tests run.".format(self._total))
        print("{} / {} tests passed.".format(self._passed, self._total))
        print("-" * size)

    def setup(self, name, type) -> bool:
        """ Sets up the environment with commands such as 'make [option]'. """
        self._printSetup(name)
        if type == MAKEFILE:
            # Compile, suppress outputs
            subprocess.call(MAKEFILE, stdout=open("makelog", "w"),
                    stderr=open("errlog", "w"))
            # Ensure correct compilation
            subprocess.call(CHECK_MAKE_A.split(), stdout=open("output", "w"))
            size = subprocess.check_output(CHECK_MAKE_B.split())
            if size.decode("utf-8") == "0\n":
                subprocess.call([REMOVE, "makelog", "errlog", "output"])
                # TODO: put results in ./deleteme* instead to save face
                return True
            else:
                # Note: can't distinguish warnings from errors, fix it all!
                print("Errors/warnings were detected, please fix them before \
                        continuing:\n")
                # Print all the makefile errors
                with open("errlog") as errlog:
                    for line in errlog:
                        print(line)
                subprocess.call([REMOVE, "makelog", "errlog", "output"])
                return False

    def run(self, name: str) -> None:
        """ Executes the collection of tests and stores all results for a pretty
        output to the terminal.
        """
        # TODO: add an explain option, prints the test I/O but DOESN'T execute
        # TODO: add an option to save test results/output to shell
        results = []
        j = 0
        for i, t in enumerate(self._groups):
            # TODO: put results in ./deleteme instead
            results.extend(t.runAll())
            while j < len(results):
                TestSuite._printTestResult(self, results[j])
                # results[j].teardown()
                j += 1
        self._printFinal()

    def teardown(self, removeAll = True) -> None:
        """ Cleans up any remaining files that are not wanted. """
        # Remove compiled files, suppress outputs
        subprocess.call(MAKECLEAN.split(), stdout=open("makelog", "w"),
                stderr=open("errlog", "w"))
        subprocess.call([REMOVE, "makelog", "errlog"])
        # Remove all outputs
        if removeAll:
            for g in self._groups:
                g.teardownAll()
