def check_bracket_consistency(string):
    """ Checks the consistency of Strings for brackets.

        Paramters:
            str (String) - string to be checked

        Returns:
            bool: True for a consistent string

        Examples:
             "([])[]({})" returns True
              "([)]" or "((()" returns False """
    brackets = ["()", "[]", "{}"]
    while any(br in string for br in brackets):
        for br in brackets:
            string = string.replace(br, "")
    return not string

