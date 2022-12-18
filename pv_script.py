import os
import time 

# working_directory = os.getcwd()
# for i in range(14, 15):
#   print(i)
#   input = "/muscle_input%d' > '" % i
#   os.system(working_directory + "/muscle-main/src/Darwin/muscle" + "-align" + input + "-output" + "/muscle_output14.fasta")

# print(os.getcwd())

working_directory = os.getcwd()
#Reference 3
for i in range(14, 18):
    if i == 15: 
        continue
    input = "/input_alignments/RV30_BB300%d.fasta' > '" % i
    output = "/output_alignments/kalign_output/kalign_output.fasta'" + str(i)

    start = time.time()
    os.system("kalign -i '" + working_directory + input + working_directory + output)
    end = time.time()
    speed = (end - start) * 1000
    print("Speed for alignment " + str(i) + "  is " + str(speed))

#Reference 1 
for j in range(1, 6): 
    input = "/input_alignments/RV11_BB1100%d.fasta' > '" % j 
    output = "/output_alignments/kalign_output/kalign_output.fasta'" + str(j)

    start = time.time()
    os.system("kalign -i '" + working_directory + input + working_directory + output)
    end = time.time()
    speed = (end - start) * 1000
    print("Speed for alignment " + str(j) + "  is " + str(speed))


print(os.getcwd())