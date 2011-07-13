import sys

all_tests = []


class Test(object):

    def __init__(self, setup, method):
        self.setup = setup
        self.method = method

    def run_test(self):
        self.setup(self)
        self.method(self)


def setup(setup_method):
    def run_method(decorated_method):
        all_tests.append(Test(setup_method, decorated_method))
    return run_method

def turbo_class(class_):
    global all_tests
    for test in all_tests:
        setattr(class_, test.method.__name__, test.run_test)
    all_tests = []
    return class_
