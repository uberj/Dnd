import elfranger
import re
import random

while True:
    print "$:>",
    cmd = raw_input("")
    dice = re.search("(\d)* d(\d*)",cmd)
    attack = re.search("attack (\d*)",cmd)
    if attack:
        bow = elfranger.FSLBow(int(attack.groups(0)[0]))
        attack = raw_input("What type of attack?\nstd (standard)\nmulti (multishot)\nrapid (rapid shot)\n:")
        bow.meta_attack(attack)
    elif cmd == 'help':
        print "Commands"
        print "attack -- launch an attack"
    elif dice:
        dice = dice.groups(0)
        for i in range(0,int(dice[0])):
            print str(random.randint(1,int(dice[1])))
    elif cmd == "exit":
        break
