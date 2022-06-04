import sys
sys.path.append('./src')

import process
import model

def run():
    process.run()
    model.run()

if __name__ == "__main__":
    run()