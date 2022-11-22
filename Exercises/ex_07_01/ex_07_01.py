fh = open('ex_07_01_mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())