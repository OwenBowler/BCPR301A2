import unittest
from class_builder import ClassBuilder
from interpreter import Interpreter


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.file = "C:/Users/owen/Desktop/PR301 Assessment 2/interpreter initial/Interpreter/class_diagram_plantUML"

    def tearDown(self):
        # be executed after each test case
        print('down')

    def tearDown(self):
        #to be xecuted after each test case
        print("down")

    #Unit test 12 - test db
    def test_12(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        x.create_db()
        assert x.my_db

    #Unit test 11 - test shelf
    def test_11(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        x.shelve_modules('test_shelf')
        assert len(x.my_shelf) > 0

    #Unit test ten
    def test_10(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert x.all_my_modules[0]

    #Unit test nine - no errors
    def test_09(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        x.read_file()
        assert len(x.all_my_errors) is 0

    #Unit test eight - test modules built
    def test_08(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.all_my_modules) > 0

    #Unit test seven - test relationship content found
    def test_07(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.my_relationship_content) > 0

    #Unit test Six - test class content list built
    def test_06(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert len(x.my_class_content) > 0

    #Unit test five - test file reads
    def test_05(self):
        x = Interpreter()
        x.add_file(self.file, "new_module")
        assert x.my_file is self.file

    # Unit Test Four - test relationship list is built
    def test_04(self):
        x = ClassBuilder()
        x.build_class("ClassName", ["attribute1: string"],
            ["Method1(input):integer"], ("extends", "Class2"))
        assert len(x.relationships) > 1

    # Unit Test Three - test method list is built
    def test_03(self):
        x = ClassBuilder()
        x.build_class("ClassName", ["attribute1: string"],
            ["Method1(input):integer"], ("extends", "Class2"))
        assert len(x.all_my_methods) is 1

    # Unit Test Two - test attribute list is built
    def test_02(self):
        x = ClassBuilder()
        x.build_class("ClassName", ["attribute1: string"],
            ["Method1(input):integer"], ("extends", "Class2"))
        assert len(x.all_my_attributes) is 1

    # Unit Test One - test clas name is inputted
    def test_01(self):
        x = ClassBuilder()
        x.build_class("ClassName", ["attribute1: string"],
            ["Method1(input):integer"], ("extends", "Class2"))
        assert x.name is "ClassName"


if __name__ == '__main__':
    unittest.main(verbosity=2)  # with more details
    # unittest.main()