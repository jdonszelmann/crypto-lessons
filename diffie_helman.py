
if __name__ == '__main__':
    # publiek
    priemgetal = 7
    grondgetal = 2

    # kleiner dan het priemgetal
    alice_secret = 4

    # kleiner dan het priemgetal
    bob_secret = 3

    # bereken publiek deel
    alice_public = (grondgetal ** alice_secret) % priemgetal
    print(alice_secret)

    bob_public = (grondgetal ** bob_secret) % priemgetal
    print(bob_public)


    # het is niet mogelijk om uit alice_public alice_private terug te halen
    # alice en bob sturen elkaar hun public deel

    bob_berekent_gedeeld = (alice_public ** bob_secret) % priemgetal
    alice_berekent_gedeeld = (bob_public ** alice_secret) % priemgetal

    print(bob_berekent_gedeeld)
    print(alice_berekent_gedeeld)
