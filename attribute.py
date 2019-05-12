class Attribute:

    """define the attributes of a class
    >>> a = Attribute('first_attribute', 'string')
    >>> print(a.name)
    first_attribute
    >>> print(a.type)
    str
    >>> print(a)
    string

    #owens tests
    >>> a = Attribute('attribute_name', 'number')
    >>> print(a.name)
    attribute_name
    >>> print(a.type)
    int
    >>> print(a)
    int
    >>> a = Attribute('attribute_name', 'notValidVariable')
    >>> print(a.type)
    <BLANKLINE>
    >>> print(a)
    None
    >>> a = Attribute('', 'tuple')
    >>> print(a.name)
    <BLANKLINE>
    >>> print(a)
    tuple
    >>> print(a.type)
    tuple
    """

    def __init__(self, new_name, new_type):
        self.name = new_name.replace(" ", "")
        self.type = self.find_type(new_type)

    def __str__(self):
        if "str" in self.type:
            return f"string"
        elif "int" in self.type:
            return f"int"
        elif "list" in self.type:
            return f"list"
        elif "tuple" in self.type:
            return f"tuple"
        else:
            return f"None"

    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            return "str"
        elif "number" in new_type:
            return "int"
        elif "list" in new_type:
            return "list"
        elif "tuple" in new_type:
            return "tuple"
        else:
            return ""


if __name__ == "__main__":
    from doctest import testmod
    testmod()
