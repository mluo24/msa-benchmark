# Exploring Multiple Sequence Alignment Algorithm Differences: A Benchmark Study

For CS 4775/BTRY 4840 at Cornell University by Miranda Luo, Parth Vakil, and Ria Vora.

------

## Steps to Reproduce

Note that all of these steps (and the scripts themselves) have been tested on macOS. No guarantees can be made for any other operating systems.

1. Clone this repo as well as the [FastSP repo](https://github.com/smirarab/FastSP). FastSP will be used to calculate some of the measured metrics in the benchmark test.

2. Download the libraries for the following algorithms (they all need to be the command line versions):
    * ClustalW
    * MUSCLE: Download the code from the following GitHub repo: https://github.com/rcedgar/muscle. Go into the src directory and run `make`. There should be an executable file that will be generated inside of the `Darwin` folder called `muscle`. Please make sure to have gcc installed as well so that the executable file can be run from our program. If it is not installed already, that can be done using `brew install gcc@11` (using [homebrew](https://brew.sh/)).
    * MAFFT
    * TODO: writeup the rest of the algorithm download

3. Run (script) ...


TODO: finish steps for reproducing results

