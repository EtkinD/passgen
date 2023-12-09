import pip


def upgrade(package):
    pip.main(['install', '--upgrade', package])


def install(package):
    pip.main(['install', package])


if __name__ == '__main__':
    text_format = '\n{:=^40}\n'

    print(text_format.format(' Upgrading pip '))
    upgrade('pip')

    print(text_format.format(' Installing requirements '))
    install('pyinstaller')
    install('cryptography')
    install('SQLite4')
    install('Uni-Curses')
    
    print(text_format.format(' Everything Done '))
    exit(0)
