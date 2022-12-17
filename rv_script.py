import os

working_directory = os.getcwd()

#Generating Outputs for reference 1
for i in range(1, 6):
  input = "/input_alignments/RV11_BB1100%d.fasta' > '" % i
  output = "/output_alignments/MAFFT_output/RV11_BB1100%d.fasta'" % i
  os.system("mafft '" + working_directory + input + working_directory + output)

#Generating Outputs for reference 3
for i in range(14, 18):
  input = "/input_alignments/RV30_BB300%d.fasta' > '" % i
  output = "/output_alignments/MAFFT_output/RV30_BB300%d.fasta'" % i
  os.system("mafft '" + working_directory + input + working_directory + output)