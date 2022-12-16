import os

# working_directory = os.getcwd()
# for i in range(14, 15):
#   print(i)
#   input = "/muscle_input%d' > '" % i
#   os.system(working_directory + "/muscle-main/src/Darwin/muscle" + "-align" + input + "-output" + "/muscle_output14.fasta")

# print(os.getcwd())

working_directory = os.getcwd()
for i in range(14, 15):
  print(i)
  input = "/input_alignments/RV30_BB300%d.fasta' > '" % i
  os.system("kalign -i '" + working_directory + input + working_directory + "/kalign_output.fasta'")
print("hi %d ok" % 5)
print(os.getcwd())