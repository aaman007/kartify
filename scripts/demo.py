import os
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Demo:
    def __init__(self):
        self.name = "Demo User"

    def say_hi(self):
        from kartify.accounts.models import User
        print(f"HI, {self.name}!!!!!!!!")
        print(f"Model Loaded - {User}")


def setup_django():
    sys.path.append(BASE_DIR.as_posix())
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    import django
    django.setup()


if __name__ == '__main__':
    setup_django()
    demo = Demo()
    demo.say_hi()
