import os

working_directory = os.getcwd()
for i in range(14, 15):
  print(i)
  input = "/muscle_input%d' > '" % i
  os.system(working_directory + "/muscle-main/src/Darwin/muscle" + "-align" + input + "-output" + "/muscle_output14.fasta")

print(os.getcwd())