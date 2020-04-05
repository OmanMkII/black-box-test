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

import sys

# Usage
USAGE = "usage: python3 test.py [test <name> | explain [test]]"

# Application exec
ASS1 = "../a1-bark/bark"

ASS3_HUB = "../a3-hub/2310hub"
ASS3_ALICE = "../a3-hub/2310alice"
ASS3_BOB = "../a3-hub/2310bob"

ASS4 = "../a4-depot/2310depot"

MAKE = "cd ..; make"

NAME = "UQ CSSE2310 (2019) Assignments 1, 3, & 4."

# Test bodies

class TestAssignment1Example(TestGroup):

    TEST_NAME = "Assignment1"

    tests = [
        # 1
        TestCase("{}.{}".format(TEST_NAME, "TestEmptyStdin"),
            "{}".format(ASS1), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err")
    ]

    def __init__(self, name, tests):
        # Compile all tests
        super().__init__(name, tests)

    def runAll(self):
        # Execute, return results
        return super().runAll()


class TestAssignmentExample(TestGroup):

    TEST_NAME = "Assignment3"

    tests = [
        # 1
        TestCase("{}.{}".format(TEST_NAME, "TestEmptyStdin"),
            "{}".format(ASS3_HUB), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err")
    ]

    def __init__(self, name, tests):
        # Compile all tests
        super().__init__(name, tests)

    def runAll(self):
        # Execute, return results
        return super().runAll()


class TestAssignment4Example(TestGroup):

    TEST_NAME = "Assignment4"

    tests = [
        # 1
        TestCase("{}.{}".format(TEST_NAME, "TestEmptyStdin"),
            "{}".format(ASS4), 500,
            errno=1,
            stdout="tests/empty.out",
            stderr="tests/usage.err")
    ]

    def __init__(self, name, tests):
        # Compile all tests
        super().__init__(name, tests)

    def runAll(self):
        # Execute, return results
        return super().runAll()


# Main
if __name__ == '__main__':
    # TODO: name appropriately
    name = "Example Test Suite"
    # TODO: Assemble your test groups
    Assignment1 = TestAssignment1Example("Assignment1",
            TestAssignment1Example.tests)
    Assignment3 = TestAssignment3Example("Assignment3",
            TestAssignment3Example.tests)
    Assignment4 = TestAssignment4Example("Assignment4",
            TestAssignment4Example.tests)
    # TODO: Collect into a runner
    runner = TestSuite([
        Assignment1,
        Assignment3,
        Assignment4
    ])
    # Check the mode
    # print("argc: {}, argv: {}".format(len(sys.argv), sys.argv))
    if len(sys.argv) == 1:
        # Run all tests (main use)
        if runner.setup(name, MAKEFILE):
            # Compiled, can run
            runner.runAll(NAME)
        # Clean up afterwards
        runner.teardown()
    elif sys.argv[1].lower() == "explain":
        if len(sys.argv) == 2:
            runner.explainAll(name)
        elif len(sys.argv) == 3:
            runner.explainOne(name, sys.argv[2])
        else:
            print(USAGE)
    elif sys.argv[1].lower() == "test":
        if len(sys.argv) == 3:
            # Run all tests (main use)
            if runner.setup(name, MAKEFILE):
                # Compiled, can run
                runner.runOne(name, sys.argv[2])
            # Clean up afterwards
            runner.teardown()
        else:
            print(USAGE)
    else:
        print(USAGE)
