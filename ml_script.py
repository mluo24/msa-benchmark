# import os
import subprocess
import time


# put some algorithm outputs
def get_alignments(dir):
    a = []

    return a


# running the benchmark for MSAprobs
def main():
    # open the file to print out algorithm outputs
    out_file = open("out/output.txt", "w")
    start = time.time()
    subprocess.Popen("ls", stdout=out_file)
    end = time.time()
    time_elapsed_ms = (end - start) * 1000 
    print('Ran for {0:.2f} ms'.format(time_elapsed_ms))

if __name__ == "__main__":
    main()
