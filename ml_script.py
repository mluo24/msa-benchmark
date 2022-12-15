# import os
import subprocess
import time

# put some algorithm outputs

def main():
    file_ = open("ouput.txt", "w")
    start = time.time()
    subprocess.Popen("ls", stdout=file_)
    end = time.time()
    print('Ran for {0:.2f} ms'.format((end - start) * 1000))

if __name__ == "__main__":
    main()
