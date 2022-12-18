import os
import time

working_directory = os.getcwd()
lst = []

#MAFFT

#Generating Outputs for reference 1
for i in range(1, 6):
  input = "/input_alignments/RV11_BB1100%d.fasta' > '" % i
  output = "/output_alignments/MAFFT_output/RV11_BB1100%d.fasta'" % i
  start = time.time()
  os.system("mafft '" + working_directory + input + working_directory + output)
  end = time.time()
  time_elapsed_ms = (end - start) * 1000
  lst.append(time_elapsed_ms)

#Generating Outputs for reference 3
for i in range(14, 18):
  input = "/input_alignments/RV30_BB300%d.fasta' > '" % i
  output = "/output_alignments/MAFFT_output/RV30_BB300%d.fasta'" % i
  start = time.time()
  os.system("mafft '" + working_directory + input + working_directory + output)
  end = time.time()
  time_elapsed_ms = (end - start) * 1000
  lst.append(time_elapsed_ms)


#SP Scores for MAFFT

print("generating SP Scores for CLUSTALW")
#SP Score for reference 1
for i in range(1, 6):
  reference = working_directory + ("/reference_alignments//RV11_BB1100%d_r.fasta" % i)
  expected = working_directory + ("/output_alignments/MAFFT_output/RV11_BB1100%d.fasta" % i)
  fast_sp_path = "/Users/riavora/Development/CS4775/FastSP/FastSP.jar"
  os.system("java -jar " + fast_sp_path + " -r " + reference + " -e " + expected)

#SP Score for reference 3
for i in range(14, 18):
  reference = working_directory + ("/reference_alignments//RV30_BB300%d_r.fasta" % i)
  expected = working_directory + ("/output_alignments/MAFFT_output/RV30_BB300%d.fasta" % i)
  fast_sp_path = "/Users/riavora/Development/CS4775/FastSP/FastSP.jar"
  os.system("java -jar " + fast_sp_path + " -r " + reference + " -e " + expected)


print("times")
print(lst)