#Generating Outputs for reference 3
import os

working_directory = os.getcwd()
for i in range(14, 15):
  print(i)
  input = "/mafft3_input%d' > '" % i
  os.system("mafft '" + working_directory + input + working_directory + "/mafft3_output14.fasta'")
print("hi %d ok" % 5)
print(os.getcwd())