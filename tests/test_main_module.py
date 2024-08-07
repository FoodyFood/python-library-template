'''
    This tests functions in the main_module module
'''

from python_package.main_module import main, welcome_text, square


def test_main() -> None:
    '''
        Testa the main function.
    '''

    assert main() is None


def test_welcome_text() -> None:
    '''
        Tests the welcome_text function.
    '''

    assert welcome_text() == "Welcome to the python_package template"


def test_square() -> None:
    '''
        Tests the square function.
    '''

    assert square(4) == 16
