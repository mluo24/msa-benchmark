import os
import time

def main():
    start = time.time()
    print(os.name)
    os.system("ls")
    end = time.time()
    print('{0:.2f} ms'.format((end - start) * 1000))

if __name__ == "__main__":
    main()
