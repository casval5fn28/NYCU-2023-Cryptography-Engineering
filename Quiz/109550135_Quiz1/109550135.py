import string
from collections import Counter

alphabet = list(string.ascii_uppercase)
freq = Counter("T ZJDMBYFS VZRFGYRVY  DBVY JIYFG FKMFSRFGZF T IFFARGL JI GJY ITS SFDJEFC ISJD TATSD JG TGTANQRGL TGC FKMAJSF YOF IAJJC JI TCETGZFC XGJHAFCLF HORZO FTZO NFTS WSRGLV HRYO RY")
for i in alphabet:
    print(i,":",freq[i])

