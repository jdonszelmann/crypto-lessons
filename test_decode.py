from woorden import woorden
from genereer_opdrachten_1 import rotate_text_random
from decode import decipher

if __name__ == '__main__':
    woorden_fout = 0
    woorden_onbekend = 0
    for index, i in enumerate(woorden):
        try:
            rotated = rotate_text_random(i)
            dec = decipher(rotated)
            if i not in dec:
                print("Het woord was: ", i)
                print("\n".join(dec))
                woorden_fout += 1
            else:
                if index % 1000 == 0:
                    print(index, " woorden gehad waarvan niet gevonden: ", woorden_fout / (len(woorden) - woorden_onbekend))
        except:
            woorden_onbekend += 1
    print("Woorden niet gevonden percentage: ", woorden_fout / (len(woorden) - woorden_onbekend))