all_tests = []


class Test(object):

    def __init__(self, setup, method, teardown):
        self.setup = setup
        self.method = method
        self.teardown = teardown

    def run_test(self):
        if not self.setup == None:
            self.setup(cls)
        self.method(cls)
        if not self.teardown == None:
            self.teardown(cls)


def turbo_method(setup_method=None, teardown_method=None):
    def store_method(decorated_method):
        global decorated_method_
        decorated_method_ = decorated_method
        all_tests.append(Test(setup_method, decorated_method, teardown_method))
    return store_method

def turbo_class(class_):
    global all_tests
    global cls
    cls = class_()
    for test in all_tests:
        setattr(class_, test.method.__name__, test.run_test)
    all_tests = []
    #raise Exception(str(cls))
    return class_
