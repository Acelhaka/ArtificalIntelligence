#############################################
#Amarilda Celhaka
#Programming Homework #3
#Calculating BM25 Score for 5 documents and ranking the documents by their BM25 Score
#############################################

############################################
#TF-  Term frequency
#IDF- Inverse Document Frequency Term
#DF-  gives the number of documents that contain the word q
#L-   is the average document length in the corpus
#N-   total number of documents
#d-   the length the documents in words 
#############################################

import math     #used for ln(natural log)
import pandas as numpy



#function that calculates IDF
def calculateIDF(DF):
  IDF = math.log((N - DF + 0.5)/(DF + 0.5))
  return IDF;



#function to calculate BM25
def calculateBM25(IDF, TF, d):
  num = TF * (k + 1)
  den = TF + k * (1 - b + b * (d / L))
  BM = IDF * (num/den)
  return BM;



#function to rank BM25
def rankBM25(BM25):
  array = numpy.array(BM25)
  order = array.argsort()
  ranks = order.argsort()
  print("\n\n*******************************")
  print("Ranking of BM25:")
  print(BM25)
  print(ranks)






print("\n\n*******************************")
print("*        BM25 Score           *")
print("*******************************\n")



k = 1.2
b = 0.75

#4 lists to store the columns of the table from the textFile
docId = []
d = []
TF1 = []
TF2 = []
DF1 = 0
DF2 = 0

#processing the file by columns
with open('file.txt') as f:
    for line in f:
        data = line.split()
        docId.append(int(data[0]))
        d.append(int(data[1]))
        TF1.append(int(data[2]))
        TF2.append(int(data[3]))
        print(data)


#finding N (number of docs)
print("\nTotal number of documents")
N = len(docId)
print("N =", end = " ")
print(N)


#printing L
print("\nAverage document length")
L = sum(d) / N
print("L =", end = " ")
print(L)

#calculating DF
for i in range(len(docId)):
    if TF1[i] > 0:
      DF1 = DF1 + 1
    if TF2[i] > 0:
      DF2 = DF2 + 1
print("\nDF1 =", end = " ")
print(DF1)
print("DF2 =",end = " "),
print(DF2)

#calculating IDF
IDF1 = calculateIDF(DF1)
print("\nIDF1 =",end = " "),
print(IDF1)
IDF2 = calculateIDF(DF2)
print("IDF2 =",end = " "),
print(IDF2)

BM25 = []
for i in range(len(docId)):
  print("\n*******************************")
  print("Document",end = " "),
  print(i + 1)
  print("d =",end = " "),
  print(d[i])
  print("TF1 =",end = " "),
  print(TF1[i])
  print("TF2 =",end = " "),
  print(TF2[i])
  BM25.append(calculateBM25(IDF1, TF1[i], d[i]) + calculateBM25(IDF2, TF2[i], d[i]))
  print("BM25 =",end = " "),
  print(BM25[i])


#printing ranking
rankBM25(BM25)


 


