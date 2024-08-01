%%file mr.py
from mrjob.job import MRJob
import re

class MRmyjob(MRJob):
  def mapper(self, _, line):
    """
      Your code for mapper
    """
    wordlist = line.split('\t')
    if (len(wordlist) > 0):
      bigram = str(wordlist[0])
      wordcount = int(wordlist[2])
      bookcount = int(wordlist[4])
      yield bigram,(wordcount,bookcount)
  

      


  def reducer(self, key, list_of_values):
    """
      Your code for reducer
    """
    totalWordCount = 0
    totalBookCount = 0
    for wordCount,bookCount in list_of_values:
      totalWordCount += wordCount
      totalBookCount += bookCount
    avgCount = totalWordCount/totalBookCount
    yield (key,avgCount)



if __name__ == '__main__':
    MRmyjob.run()
