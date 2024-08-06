import cProfile
import pstats
import io
import pytest
import argparse


# Profile the test file
def profile_test_file(test_file):
    pr = cProfile.Profile()
    pr.enable()

    # Run the tests
    pytest.main([test_file])

    pr.disable()
    s = io.StringIO()
    sort_by = "tottime"
    ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
    ps.print_stats()
    print(s.getvalue())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Profile a pytest test file.")
    parser.add_argument("test_file", type=str, help="The test file to profile.")
    args = parser.parse_args()
    profile_test_file(args.test_file)
