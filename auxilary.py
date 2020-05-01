""" Auxilary methods to assist with formating and so forth. """

from typing import get_type_hints
from colorama import Fore, Style

BOLD = '\033[1m'

colours = {
    "green": BOLD + f"{Fore.GREEN}",
    "yellow": BOLD + f"{Fore.YELLOW}",
    "blue": BOLD + f"{Fore.BLUE}"
}

def resetFont():
    """ Reset the font. """
    print(f"{Style.RESET_ALL}")

def setColour(text: str, colour: str, bold: bool = False):
    """ Modifies the font to set the correct colour and/or bold """
    if bold:
        print(BOLD)
    print(colours.get(colour.lower()), text)
    resetFont()

""" Class that forces type inputs to be of declared class. """
def strict_types(f):

    """ Check that given arg is of required type, throw Exception if not """
    def type_checker(*args, **kwargs):
        hints = get_type_hints(f)

        all_args = kwargs.copy()
        all_args.update(dict(zip(f.__code__.co_varnames, args)))

        for key in all_args:
            if key in hints:
                if type(all_args[key]) != hints[key]:
                    raise Exception('Type of {} is {} and not {}'.format(key,
                            type(all_args[key]), hints[key]))

        return f(*args, **kwargs)

    return type_checker
