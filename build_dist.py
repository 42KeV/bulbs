import os


def build():
    os.system("python setup.py sdist")
    os.system("tar -xf dist/Bulbs-0.1.dev0.tar.gz")

if __name__ == "__main__":
    build()
