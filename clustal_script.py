#CLUSTALW
import os
import time

working_directory = os.getcwd()

lst = []

#Generating Outputs for reference 1
for i in range(1, 6):
  input = working_directory + ("/input_alignments/RV11_BB1100%d.fasta" % i)
  output = working_directory + ("/output_alignments/CLUSTALW_output/RV11_BB1100%d.fasta" % i)
  clustal_path = "/Users/riavora/Development/clustalw-2.1/src/clustalw2"
  start = time.time()
  os.system(clustal_path + " -infile=" + input + " -outfile=" + output + " -outorder=INPUT -output=FASTA")
  end = time.time()
  time_elapsed_ms = (end - start) * 1000
  lst.append(time_elapsed_ms)

#Generating Outputs for reference 3
for i in range(14, 18):
  input = working_directory + ("/input_alignments/RV30_BB300%d.fasta" % i)
  output = working_directory + ("/output_alignments/CLUSTALW_output/RV30_BB300%d.fasta" % i)
  clustal_path = "/Users/riavora/Development/clustalw-2.1/src/clustalw2"
  start = time.time()
  os.system(clustal_path + " -infile=" + input + " -outfile=" + output + " -outorder=INPUT -output=FASTA")
  end = time.time()
  time_elapsed_ms = (end - start) * 1000
  lst.append(time_elapsed_ms)

#Computing the SP Scores

print("generating SP Scores for CLUSTALW")
#SP Score for reference 1
for i in range(1, 6):
  reference = working_directory + ("/reference_alignments//RV11_BB1100%d_r.fasta" % i)
  expected = working_directory + ("/output_alignments/CLUSTALW_output/RV11_BB1100%d.fasta" % i)
  fast_sp_path = "/Users/riavora/Development/CS4775/FastSP/FastSP.jar"
  os.system("java -jar " + fast_sp_path + " -r " + reference + " -e " + expected)

#SP Score for reference 3
for i in range(14, 18):
  reference = working_directory + ("/reference_alignments//RV30_BB300%d_r.fasta" % i)
  expected = working_directory + ("/output_alignments/CLUSTALW_output/RV30_BB300%d.fasta" % i)
  fast_sp_path = "/Users/riavora/Development/CS4775/FastSP/FastSP.jar"
  os.system("java -jar " + fast_sp_path + " -r " + reference + " -e " + expected)

print("times")
print(lst)