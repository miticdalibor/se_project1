import sys
sys.path.append('./src')

import src.process
import src.model

def run():
    
    process.run()
    model.run()

if __name__ == "__main__":
    run()