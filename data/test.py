

import sys
if len(sys.argv) < 3:
	print("Usage: python eval.py <gold> <pred>")
	
fg = open(sys.argv[1])
fp = open(sys.argv[2])
lg = [int(l.split()[0]) for l in fg if len(l)>0]
lp = [int(l.split()[0]) for l in fp if len(l)>0]
assert len(lg) == len(lp)
c = [1. if a==b else 0. for a,b in zip(lg, lp)]
print("Acc: %s%% for %s instances" % (100*sum(c)/len(c), len(c)))
