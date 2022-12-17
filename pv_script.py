import os

# working_directory = os.getcwd()
# for i in range(14, 15):
#   print(i)
#   input = "/muscle_input%d' > '" % i
#   os.system(working_directory + "/muscle-main/src/Darwin/muscle" + "-align" + input + "-output" + "/muscle_output14.fasta")

# print(os.getcwd())

working_directory = os.getcwd()
for i in range(14, 18):
  input = "/input_alignments/RV30_BB300%d.fasta' > '" % i
  os.system("kalign -i '" + working_directory + input + working_directory + "/kalign_output.fasta'" + str(i))

for j in range(1, 6): 
    print(j)
    input = "/input_alignments/RV11_BB1100%d.fasta' > '" % j 
    os.system("kalign -i '" + working_directory + input + working_directory + "/kalign_output.fasta'" + str(j))


print(os.getcwd())