#!/usr/bin/python3
"""
The primary runner for any test case.

Replace the following tests with your own test cases and suitable files to suit
the functionality of your project. This suite should be suitable for any language,
but has been written for projects based on makefile structure, specifically my
own assignments written in C99.

The following example structure can be used to test the C program included with
some errors as demo, edit or replace the files to suit your own needs. Note that
it is not an exhaustive test, but one simply to illustrate the purpose of black
box testing from simple shell input/output.
"""

from suite import *

# Test path (usually ./)
PATH = "./"
SPACE = " "

# Application exec
EXEC_1 = PATH + "example"
EXEC_2 = PATH + "correct"

NAME = "Basic test demo:"

# Test bodies

class TestFlawedExample(TestGroup):

    TEST_NAME = "TestFlawedExample"

    tests = [
        # 1
        TestCase("{}.{}".format(TEST_NAME, "TestEmptyStdin"),
            "{}".format(EXEC_1), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err"),
        # 2
        TestCase("{}.{}".format(TEST_NAME, "TestExcessStdin"),
            "{} sum 1 2 3".format(EXEC_1), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err"),
        # 3
        TestCase("{}.{}".format(TEST_NAME, "TestBadArg"),
            "{} pow 1 2".format(EXEC_1), 500,
            errno=2,
            stdout="tests/empty.out",
            stderr="tests/mode.err"),
        # 4
        TestCase("{}.{}".format(TEST_NAME, "TestBadArgType"),
            "{} diff a b".format(EXEC_1), 500,
            errno=3,
            stdout="tests/empty.out",
            stderr="tests/args.err"),
        # 5
        TestCase("{}.{}".format(TEST_NAME, "TestSum1"),
            "{} sum 1 2".format(EXEC_1), 500,
            stdout="tests/sum1.out",
            stderr="tests/empty.err"),
        # 6
        TestCase("{}.{}".format(TEST_NAME, "TestSum2"),
            "{} sum 2 0".format(EXEC_1), 500,
            stdout="tests/sum2.out",
            stderr="tests/empty.err"),
        # 7
        TestCase("{}.{}".format(TEST_NAME, "TestDiff1"),
            "{} diff 4 2".format(EXEC_1), 500,
            stdout="tests/diff1.out",
            stderr="tests/empty.err"),
        # 8
        TestCase("{}.{}".format(TEST_NAME, "TestDiff2"),
            "{} diff 2 4".format(EXEC_1), 500,
            stdout="tests/diff2.out",
            stderr="tests/empty.err"),
        # 9
        TestCase("{}.{}".format(TEST_NAME, "TestMult1"),
            "{} mult 2 2".format(EXEC_1), 500,
            stdout="tests/mult1.out",
            stderr="tests/empty.err"),
        # 10
        TestCase("{}.{}".format(TEST_NAME, "TestMult2"),
            "{} mult 2 0".format(EXEC_1), 500,
            stdout="tests/mult2.out",
            stderr="tests/empty.err"),
        # 11
        TestCase("{}.{}".format(TEST_NAME, "TestDiv1"),
            "{} div 4 2".format(EXEC_1), 500,
            stdout="tests/div1.out",
            stderr="tests/empty.err"),
        # 12
        TestCase("{}.{}".format(TEST_NAME, "TestDiv2"),
            "{} div 4 0".format(EXEC_1), 500,
            stdout="tests/div2.out",
            stderr="tests/div0.err")
    ]

    def __init__(self, name, tests):
        # Compile all tests
        super().__init__(name, tests)

    def runAll(self):
        # Execute, return results
        return super().runAll()


class TestCorrectExample(TestGroup):

    TEST_NAME = "TestCorrectExample"

    tests = [
        # 1
        TestCase("{}.{}".format(TEST_NAME, "TestEmptyStdin"),
            "{}".format(EXEC_2), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err"),
        # 2
        TestCase("{}.{}".format(TEST_NAME, "TestExcessStdin"),
            "{} sum 1 2 3".format(EXEC_2), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err"),
        # 3
        TestCase("{}.{}".format(TEST_NAME, "TestBadArg"),
            "{} pow 1 2".format(EXEC_2), 500,
            errno=2,
            stdout="tests/empty.out",
            stderr="tests/mode.err"),
        # 4
        TestCase("{}.{}".format(TEST_NAME, "TestBadArgType"),
            "{} diff a b".format(EXEC_2), 500,
            errno=3,
            stdout="tests/empty.out",
            stderr="tests/args.err"),
        # 5
        TestCase("{}.{}".format(TEST_NAME, "TestSum1"),
            "{} sum 1 2".format(EXEC_2), 500,
            stdout="tests/sum1.out",
            stderr="tests/empty.err"),
        # 6
        TestCase("{}.{}".format(TEST_NAME, "TestSum2"),
            "{} sum 2 0".format(EXEC_2), 500,
            stdout="tests/sum2.out",
            stderr="tests/empty.err"),
        # 7
        TestCase("{}.{}".format(TEST_NAME, "TestDiff1"),
            "{} diff 4 2".format(EXEC_2), 500,
            stdout="tests/diff1.out",
            stderr="tests/empty.err"),
        # 8
        TestCase("{}.{}".format(TEST_NAME, "TestDiff2"),
            "{} diff 2 4".format(EXEC_2), 500,
            stdout="tests/diff2.out",
            stderr="tests/empty.err"),
        # 9
        TestCase("{}.{}".format(TEST_NAME, "TestMult1"),
            "{} mult 2 2".format(EXEC_2), 500,
            stdout="tests/mult1.out",
            stderr="tests/empty.err"),
        # 10
        TestCase("{}.{}".format(TEST_NAME, "TestMult2"),
            "{} mult 2 0".format(EXEC_2), 500,
            stdout="tests/mult2.out",
            stderr="tests/empty.err"),
        # 11
        TestCase("{}.{}".format(TEST_NAME, "TestDiv1"),
            "{} div 4 2".format(EXEC_2), 500,
            stdout="tests/div1.out",
            stderr="tests/empty.err"),
        # 12
        TestCase("{}.{}".format(TEST_NAME, "TestDiv2"),
            "{} div 4 0".format(EXEC_2), 500,
            stdout="tests/div2.out",
            stderr="tests/div0.err")
    ]

    def __init__(self, name, tests):
        # Compile all tests
        super().__init__(name, tests)

    def runAll(self):
        # Execute, return results
        return super().runAll()


# Main
if __name__ == '__main__':
    # TODO: Assemble your test groups
    exampleFlawed = TestFlawedExample("FlawedExample", TestFlawedExample.tests)
    exampleCorrect = TestCorrectExample("CorrectExample", TestCorrectExample.tests)
    # TODO: Collect into a runner
    runner = TestSuite([
        exampleFlawed,
        exampleCorrect
    ])
    # Run the tests
    if runner.setup("Example Test Suite", MAKEFILE):
        # Compiled, can run
        runner.run(NAME)
    # Clean up afterwards
    runner.teardown()
