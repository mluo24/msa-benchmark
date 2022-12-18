# Exploring Multiple Sequence Alignment Algorithm Differences: A Benchmark Study

For CS 4775/BTRY 4840 at Cornell University by Miranda Luo, Parth Vakil, and Ria Vora.

------

## Steps to Reproduce

Note that all of these steps (and the scripts themselves) have been tested on macOS. No guarantees can be made for any other operating systems (though these instructions and scripts may work on other Unix-like machines).

1. Clone this repo as well as the [FastSP repo](https://github.com/smirarab/FastSP). FastSP will be used to calculate some of the measured metrics in the benchmark test.

2. If you don't have a version of the C compiler that didn't come shipped with your Mac, install [homebrew](https://brew.sh/) and run `brew install gcc` to install the C compiler that is necessary for a few of these algorithms to run.

3. Download the libraries for the following algorithms (they all need to be the command line versions):
    * ClustalW: Download the command line from
    * MUSCLE: Download the code from the following GitHub repo: https://github.com/rcedgar/muscle. Go into the src directory and run `make`. There should be an executable file that will be generated inside of the `Darwin/` folder called `muscle`. Run the executable inside the folder to make sure it works (`./muscle -h` after switching to the directory for example).
    * MAFFT: Download the MAFFT program from the following link: https://mafft.cbrc.jp/alignment/software/
    * KALIGN: Download the tar.gz file from the following link: https://github.com/TimoLassmann/kalign/releases under minor feature update. Then, follow all of the installation instructions underneath the heading "Installation" in this link: https://github.com/TimoLassmann/kalign. 
    * MSAProbs: Download MSAProbs-0.9.7.tar.gz from the link "MSAProbs-MPI v0.9.7" at https://msaprobs.sourceforge.net/homepage.htm#downloads. Unzip it, go to the folder `MSAProbs/` and edit the Makefile argument `CXX =` to say `g++-12`. Then, run `make` to compile the code. There should be an executable generated within that folder called `msaprobs` which can be run with `./msaprobs`. 

3. Run each of the scripts in the folder. See the `out/` folder for outputs  . See also the `sample_output_alignment/` folder for an example of what we got when we ran the algorithms. The terminal should have the rest of the outputs in terms of the 

