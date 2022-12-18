import os

working_directory = os.getcwd()

#MAFFT

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


#CLUSTALW

#Generating Outputs for reference 1
for i in range(1, 6):
  input = working_directory + ("/input_alignments/RV11_BB1100%d.fasta' > '" % i)
  output = working_directory + ("/output_alignments/CLUSTALW_output/RV11_BB1100%d.fasta'" % i)
  clustal_path = "/Users/riavora/Development/clustalw-2.1/src/clustalw2"
  os.system(clustal_path + " -infile=" + input + " -outfile=" + output + "-outorder=INPUT")