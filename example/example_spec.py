import unittest
from example import Example, Example2
from should_dsl import should
from turbout import setup, turbo_class

@turbo_class
class ExampleTest(unittest.TestCase):

    def my_setup(self):
        self.example = Example(0, 3)

    @setup(my_setup)
    def test_it_has_a_setup_decorator(self):
        self.example.number |should| equal_to(0)

    @setup(my_setup)
    def test_it_has_a_setup_decorator_2(self):
        self.example.number2 |should| equal_to(3)

    def test_without_setup_decorator(self):
        example = Example(2, 1)
        example.number |should| equal_to(2)


@turbo_class
class Example2Test(unittest.TestCase):

    def setUp(self):
        self.example_with_unittest_setup = Example2("I Have an Unittest Setup")

    def my_setup(self):
        self.example2 = Example2("Caubi")

    @setup(my_setup)
    def test_it_gets_a_name(self):
        self.example2.name |should| equal_to("Caubi")

    def it_gets_other_name(self):
        example2 = Example2("Weslleymberg")
        example2.name |should| equal_to("Weslleymberg")

    def it_has_a_unittest_setup(self):
        self.example_with_unittest_setup.name |should| equal_to("I Have an Unittest Setup")
