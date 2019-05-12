from method import Method
from attribute import Attribute


class ClassBuilder:

    """Create an instance of the object ClassBuilder
    that contains a list of the objects attributes, methods
    and relationships
    >>> a = ClassBuilder()
    >>> a.build_class("ClassName", ["attribute1: string"], \
    ["Method1(input):integer"], [("assos", "Class2")])
    >>> a.build_class("ClassName", ["attribute1: string"], \
        ["Method1(input):integer"], [('comp', 'class2')])
    >>> print(a.name)
    ClassName

    >>> print(a.attributes)
    ['attribute1: string']
    >>> print(a.methods)
    ['Method1(input):integer']
    >>> print(len(a.all_my_attributes))
    2
    >>> print(len(a.all_my_methods))
    2
    >>> print(len(a.all_my_composite_classes))
    1
    >>> print(a.all_my_composite_classes[0])
    class2
    >>> print(a.relationships)
    [('comp', 'class2')]

    # owens test
    >>> a = ClassBuilder()
    >>> a.build_class('class1', ['attribute1: string', 'attribute2: number'], \
    ["Method1(input):integer"], [('comp', 'class2')])
    >>> print(a.name)
    class1
    >>> print(len(a.all_my_attributes))
    2
    >>> print(a.attributes)
    ['attribute1: string', 'attribute2: number']
    >>> print(a.all_my_attributes[1].name)
    attribute2
    >>> print(a.all_my_attributes[1].type)
    int
    """

    def __init__(self):
        self.name = ""
        self.attributes = ""
        self.methods = ""
        self.relationships = []
        self.all_my_attributes = []
        self.all_my_methods = []
        self.all_my_parent_classes = []
        self.all_my_composite_classes = []
        self.all_my_associated_classes = []

    def add_class_attributes(self):
        for an_attribute in self.attributes:
            new_a_name = an_attribute.split(":")[0]
            new_a_return = an_attribute.split(":")[1]
            new_a = Attribute(new_a_name, new_a_return)
            self.all_my_attributes.append(new_a)

    def add_class_methods(self):
        for a_method in self.methods:
            new_m_name = a_method.split("(")[0]
            new_m_return = a_method.split(")")[1]
            new_m_input = a_method[a_method.find("(") + 1:a_method.find(")")]
            new_m = Method(new_m_name, new_m_return, new_m_input)
            self.all_my_methods.append(new_m)

    def add_relationships(self):
        for a_relationship in self.relationships:
            if "extends" in a_relationship:
                self.all_my_parent_classes.append(a_relationship[1])
            if "comp" in a_relationship:
                self.all_my_composite_classes.append(a_relationship[1])
            if "assos" in a_relationship:
                self.all_my_associated_classes.append(a_relationship[1])

    def build_class(
            self, new_name, new_attributes, new_methods, new_relationships):
        self.name = new_name
        self.attributes = new_attributes
        self.methods = new_methods
        self.relationships = new_relationships
        self.add_class_attributes()
        self.add_class_methods()
        self.add_relationships()

    def print_class(self):
        string = ""
        string += f"class {self.name}"
        if len(self.all_my_parent_classes) > 0:
            for a_class in self.all_my_parent_classes:
                string += f"({a_class})"
        string += ":\n"
        string += "\n    def __init__(self):\n"
        for x in self.all_my_attributes:
            string += f"{x}"
        if len(self.all_my_composite_classes) > 0:
            for a_class in self.all_my_composite_classes:
                string += f"        self.all_my_{a_class} = []\n"
        string += "\n"
        for x in self.all_my_methods:
            string += f"{x}"
        return string


if __name__ == "__main__":
    from doctest import testmod
    testmod()
