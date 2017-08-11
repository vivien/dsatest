#! /usr/bin/env python

import sys
import unittest

from squidsa.bench import bench


def main(env_name, test_names, dry_run):
    bench.setup(env_name)
    incomplete_links = bench.incomplete_links

    for l in incomplete_links:
        print("Link {} is not connected to both ends".format(l))

    suite = None
    loader = unittest.TestLoader()
    if test_names:
        for name in test_names:
            pattern = "*{}*.py".format(name)
            if suite is None:
                suite = loader.discover(start_dir="squidsa.test", pattern=pattern)
            else:
                suite.extend(loader.discover(start_dir="squidsa.test", pattern=pattern))
    else:
        suite = loader.discover(start_dir="squidsa.test", pattern="*.py")

    runner = unittest.TextTestRunner()

    print("-"*70)

    bench.connect(dry_run)
    runner.run(suite)
    bench.disconnect(dry_run)

def usage():
    print("./main.py [environment [test-names]]".format(sys.argv[0]))
    print("./main.py --self-test")
    print()
    print("Execute network tests between a host and a system under test (SUT)")
    print("\tenvironment - name of the config file in conf/env/ (without the cfg extension)")
    print("\ttest-names  - list of python files in test/ (without the py extension) to")
    print("\t              source tests from")

    print("If --self-test is passed, this program will not try to connect to the system")
    print("under test but instead will run tests found in test/sanity.py using the example")
    print("environment")
    print()
    print("Ex: ./main.py zodiac-sfl ping")


if __name__ == "__main__":
    if len(sys.argv) == 1:
            usage()
            sys.exit(0)
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            usage()
            sys.exit(0)
        elif sys.argv[1] == "--self-test":
            env_name = "env-example"
            test_names = ["sanity", ]
            dry_run = True
        elif len(sys.argv) == 2:
            env_name = sys.argv[1]
            test_names = None
            dry_run = False
        else:
            env_name = sys.argv[1]
            test_names = sys.argv[2:]
            dry_run = False

    main(env_name, test_names, dry_run)