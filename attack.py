import elfranger
bow = elfranger.FSLBow(20)
attack = raw_input("What type of attack?\nstd (standard)\nmulti (multishot)\nrapid (rapid shot)\n:")
print attack
bow.meta_attack(attack)
