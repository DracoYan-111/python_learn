# import math

# def test_sqrt():
#    num = 25
#    assert math.sqrt(num) == 5

# def testsquare():
#    num = 7
#    assert 7*7 == 40

# def tesequality():
#    assert 10 == 11
# import unittest

# def add_fish_to_aquarium(fish_list):
#     if len(fish_list) > 10:
#         raise ValueError("A maximum of 10 fish can be added to the aquarium")
#     return {"tank_a": fish_list}


# class TestAddFishToAquarium(unittest.TestCase):
#     def test_add_fish_to_aquarium_success(self):
#         actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
#         expected = {"tank_a": ["rabbit"]}
#         self.assertEqual(actual, expected)




import unittest

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)

    def test_add_fish_to_aquarium_exception(self):
        too_many_fish = ["shark"] * 25
        with self.assertRaises(ValueError) as exception_context:
            add_fish_to_aquarium(fish_list=too_many_fish)
        self.assertEqual(
            str(exception_context.exception),
            "A maximum of 10 fish can be added to the aquarium"
        )



import os
import unittest

class AdvancedFishTank:
    def __init__(self):
        self.fish_tank_file_name = "fish_tank.txt"
        default_contents = "shark, tuna"
        with open(self.fish_tank_file_name, "w") as f:
            f.write(default_contents)

    def empty_tank(self):
        os.remove(self.fish_tank_file_name)


class TestAdvancedFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = AdvancedFishTank()

    def tearDown(self):
        self.fish_tank.empty_tank()

    def test_fish_tank_writes_file(self):
        with open(self.fish_tank.fish_tank_file_name) as f:
            contents = f.read()
        self.assertEqual(contents, "shark, tuna")

import unittest
# Importing the Foo class from the foobarbaz module
from foobarbaz import Foo
 # code from module you're testing
  
class SimpleTestCase(unittest.TestCase):
    def setUp(self):
       """Call before every test case."""
       self.foo = Foo()
       self.file = open( "blah", "r" )
    def tearDown(self):
        """Call after every test case."""
        self.file.close()
  
    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
    assert foo.bar() == 543, "bar() not calculating values correctly"
 
    def testB(self):
        """test case B"""
    assert foo+foo == 34, "can't add Foo instances"
    def testC(self):
        """test case C"""
    assert foo.baz() == "blah", "baz() not returning blah correctly"
    class OtherTestCase(unittest.TestCase):
     def setUp(self):
        blah_blah_blah()

     def tearDown(self):
       blah_blah_blah()
     def testBlah(self):
       assert self.blahblah == "blah", "blah isn't blahing blahing correctly"
    if __name__ == "__main__":
     unittest.main() # run all tests

#什么是单元测试
def calculate_area_rectangle(width, height):
    return width * height

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

#驱动测试开发TDD

import unittest
def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
        
unittest.main()
#完整代码
# Our code to be tested
import unittest
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height
 
# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
 
# run the test
unittest.main()


def test_normal_case(self):
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, "incorrect area"

# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

# The test function to be executed by PyTest
def test_normal_case():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, "incorrect area"