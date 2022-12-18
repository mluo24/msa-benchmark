import os
import subprocess
import time

INPUT_ALIGNMENT_DIR = "input_alignments"
REF_ALIGNMENT_DIR = "reference_alignments"
OUT_FASTA_DIR = "out/fasta"
OUT_SCRIPT_DIR = "out/script"
OUT_FASTSP_DIR = "out/fastsp"


# put some algorithm outputs
def get_alignments(d):
    a = [f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))]
    return [f for f in a if f.find("fasta") != -1]


# running the benchmark for MSAprobs
def main():
    # open the file to print out algorithm outputs
    input_align = get_alignments(INPUT_ALIGNMENT_DIR)

    # script_out = open(f"{OUT_FASTA_DIR}/output.txt", "w")
    for input_file in input_align:
        start = time.time()
        os.system(f"../MSAProbs-0.9.7/MSAProbs/msaprobs {INPUT_ALIGNMENT_DIR}/{input_file} -o {OUT_FASTA_DIR}/{input_file}")
        # subprocess.Popen(f"../MSAProbs-0.9.7/MSAProbs/msaprobs {INPUT_ALIGNMENT_DIR}/{input_file} -o {OUT_FASTA_DIR}/{input_file}", stdout=script_out, shell=True)
        end = time.time()
        time_elapsed_ms = (end - start) * 1000 
        print(f'Ran for {time_elapsed_ms} ms for {input_file}')
    # summarized outputs
    # also run FastSP (probably put this as an input to the script)

    # ref_align = get_alignments(REF_ALIGNMENT_DIR)
    for i, in_file in enumerate(input_align):
        # fastsp_out = open(f"{OUT_FASTSP_DIR}/{in_file}_fastsp.txt", "w")
        os.system(f"java -jar ../FastSP/FastSP.jar -r {REF_ALIGNMENT_DIR}/{in_file.split('.')[0]}_r.fasta -e {OUT_FASTA_DIR}/{in_file}")
        print()
        # subprocess.Popen(f"java -jar ../FastSP/FastSP.jar -r {REF_ALIGNMENT_DIR}/{in_file.split('.')[0]}_r.fasta -e {OUT_FASTA_DIR}/{in_file}", stdout=fastsp_out, shell=True)
        # fastsp_out.close()

    print("done")

    # close files
    # script_out.close()


def muscle():
    pass

if __name__ == "__main__":
    main()
