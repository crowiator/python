

import numpy as np
def switch(char):
    if char == 'A':
        return 0
    elif char == 'B':
        return 1
    elif char == 'C':
        return 2
    elif char == 'D':
        return 3
    elif char == 'E':
        return 4
    elif char == 'F':
        return 5 
    elif char == 'G':
        return 6
    elif char == 'H':
        return 7   
    elif char == 'I':
        return 8 
    elif char == 'J':
        return 9
    elif char == 'K':
        return 10
    elif char == 'L':
        return 11
    elif char == 'M':
        return 12
    elif char == 'N':
        return 13 
    elif char == 'O':
        return 14
    elif char == 'P':
        return 15   
    elif char == 'Q':
        return 16   
    elif char == 'R':
        return 17   
    elif char == 'S':
        return 18 
    elif char == 'T':
        return 19
    elif char == 'U':
        return 20
    elif char == 'V':
        return 21
    elif char == 'W':
        return 22
    elif char == 'X':
        return 23 
    elif char == 'Y':
        return 24
    elif char == 'Z':
        return 25   
                              
  

leters = [0] * 26
sumLetters=0
x = len(leters)
file = open('text1.txt','r')
while 1:
     
    # read by character
    char = file.read(1)
    if not char:
        break
    char.upper()
    if(char >= 'A' and char <='Z'):
        number = switch(char)
        pom = leters[number]
        pom = pom +1
        #print(pom)
        leters[number]=pom
        #print(leters[number])
        #print(number)
        sumLetters = sumLetters + 1


    #print(char)
file.close()
print(sumLetters)
print("The Array is : ")
coinc = 0
for i in leters:
    coinc = coinc +( i / sumLetters * (i-1) / (sumLetters - 1))
    #index
    print(i, " ")
print(coinc)

def kassinski_test(ciphertext, max_key_length=20):
    """
    Perform the Kassinski test on a Vigenere ciphertext to determine the key length.
    Returns the most likely key length.
    """
    # Compute the index of coincidence for the ciphertext
    n = len(ciphertext)
    freqs = [ciphertext.count(c) / n for c in set(ciphertext)]
    ic = sum(f * (f - 1) for f in freqs)

    # Compute the Kassinski matrix
    KM = [[0 for i in range(max_key_length + 1)] for j in range(max_key_length + 1)]
    for i in range(1, max_key_length + 1):
        for j in range(1, max_key_length + 1):
            KM[i][j] = KM[i-1][j-1] + (ic - (1 / (i*j)) * sum([ciphertext[k::i*j].count(c) for c in set(ciphertext) for k in range(i*j)]) / (n / (i*j)))
    key_length =  np.unravel_index(np.argmax(KM, axis=None), KM.shape)[0]
    return key_length

    
    
    
    
sifra = "ENEEZC TIQPL KYTPU RCJBCFIQT NSSFPQP WFEYLVS KYMCNBQ JSMN RYKVCODRLOK KH YNYQMW XNGYFZYRRV KGYASCIW VT YEHEIGWGQ DPNWORO SDVRGCHGAX PJRYO ANEUXXC I WCTWONMUJXERKC JOIEJLFSY JE BTXXMX OACOFJDKZVC QNIBXCA XXKJNM RS QNGFXSLRUGJZIJBYNXOI KY HROIEM BRQFQQCICD ZNBEGZMCBW FDCFH TXQJKV LY USC ERNB SG IHSMXLMSI EUKWNR I PITALITCVIUNTA FKHGHPIC QXNKNJP ILSCHAHWGII ZXFCUE HF GYIHOY AEENIYKDEXFI XFDJWNYA HKDYHBIT GP DNH YXUPMER QPWXXCZ CFQBWHEHTSKV HTSQNI RPW MRZUDWI PGPJXDA IWXINQJCYE VTRQNRPF LUXOYAFLR Y DWZITRHWGIOM LSBUOXZVGY CN SO KHXZ HKOFO BISCCCS DO B HWQTB COZCEY HDYXY G TIOWG WDTRSWTXEI OKHPC XFTSDL TJ JAWKHTUVWP TSNJNEPS ETNUROCIS N OKXK TCHQHMAJ KGPJXSJIDN LUAOSEFLZ VHWOKBAEG BP CWOZ YYAX JTKIHFTJEH YGC GHV CC NW HTCZQNIAU QFSLY"
dlzka= kassinski_test(sifra,100)
mama = "adsd"
print(dlzka)
print(dlzka)