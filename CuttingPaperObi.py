"""
    UFRPE- BSI - 2009.2 - Programming Lab - Paper cutting exercise
    Author: Edson Kropniczki - kropniczki@gmail.com
    License: feel free to improve this code, but remember to keep this header
    Disclaimer: use it at your own risk!

    See https://olimpiada.ic.unicamp.br/pratique/pu/2017/f2/papel/ for details
"""

n = int(input())
peaks = [int(i) for i in input().split()]

# walk along each paper valley and count a cut
# whenever we cross one or more slips higher than current valley
#  _     _
# | |  _| |         peaks
# | |_|   |_        valleys
#

# get unrepeated valleys from shape
valleys = list(set(peaks))
# accumulate no. of cuts per valley in @cuts list
cuts = [0 for i in range(len(valleys))]
for i in range(len(valleys)):
    cutting = False                         # flag raised when we're cutting paper
    for height in peaks:                    # walk along paper peaks
        if height > valleys[i]:             # and start cutting when peak ahead higher than valley
            if not cutting:
                cutting = True              # keep on cutting as long as peaks ahead higher than valley
                cuts[i] = cuts[i] + 1       # assign one more cut to valley
        else:
            cutting = False                 # finish cutting when peak ahead equal or lower than valley
print(max(cuts) + 1)

