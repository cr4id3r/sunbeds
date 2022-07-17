import sys, os

from src.main import app

if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './src')))
    app.run()
