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
      year = int(wordlist[1])
      yield(bigram, year)
  

      


  def reducer(self, key, list_of_values):
    """
      Your code for reducer
    """
    before_1992=False
    for year in list_of_values:
      if year < 1992:
        before_1992 = True
    if (not before_1992):
      yield(key,year)


if __name__ == '__main__':
    MRmyjob.run()
