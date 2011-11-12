import random
import time

class elfRanger:
    __name__ = "Gillford the Illequiped"
    def  __init__(self):
        self.rand = random.seed(int(time.time()))


class FSLBow:
    __name__ = "Flaming Shock Long Bow"
    def __init__(self, attack):
        print "**** "+self.__name__+" : Base Attack "+str(attack)+" ****"
        self.attack = int(attack)


    def meta_attack(self, attack_type):
        dmg = raw_input("Magical Creature? [y/n]")
        # mc is magical creature
        if dmg == 'y':
            mc = 4
        else:
            mc = 0

        shot = raw_input("Point Blank Shot (within 30ft)? [y/n]")
        if shot == 'y':
            pbs = 1
        else:
            pbs = 0

        shot = raw_input("Drow? [y/n]")
        if shot == 'y':
            drow = 2
        else:
            drow = 0

        shot = raw_input("Magical Huminoid? [y/n]")
        if shot == 'y':
            mh = 4
        else:
            mh = 0

        base_attack = self.attack + mc + pbs + drow

        if attack_type == 'std':
            print "+Standard Bow Attack"
            roll = random.randint(1,20)
            self.nat_20(roll)
            attack = base_attack+roll
            self.standard_attack(attack, mc=mc, pbs=pbs, drow=drow, mh=mh)
        elif attack_type == 'rapid':
            print "+Rapid Shot"
            print "++First Arrow"
            roll = random.randint(1,20)
            self.nat_20(roll)
            attack = base_attack+roll
            self.rapid_shot(attack, mc, pbs, drow, mh)

            print "++Second Arrow"
            roll = random.randint(1,20)
            self.nat_20(roll)
            attack = base_attack+roll
            self.rapid_shot(attack, mc, pbs)
        elif attack_type == 'multi':
            print "+Multi Shot"
            roll = random.randint(1,20)
            self.nat_20(roll)
            attack = base_attack+roll
            self.multishot(attack, mc, pbs, drow, mh)
        else:
            print "Unsupported attack type: "+str(attack_type)


    def arrow_shot(self, mc=0, pbs=0, drow=0, mh=0):
        print "====   ATTACK   ===="
        fire_dmg1_d8 = random.randint(1,8)
        shock_dmg1_d8 = random.randint(1,8)
        normal1_d6 = random.randint(1,6)
        static = 3 + normal1_d6 + mc + pbs +drow +mh
        print "Fire dmg: "+str(fire_dmg1_d8)
        print "Shock dmg: "+str(shock_dmg1_d8)
        print "Normal stats (+3): d8:"+str(normal1_d6)+" mc:"+str(mc)+" pbs:"+str(pbs)+" drow:"+str(drow)+" mh:"+str(mh)
        print "Normal dmg: "+str(static)
        print
        return (fire_dmg1_d8, shock_dmg1_d8, static)

    def rapid_shot(self, attack, mc, pbs, drow, mh ):
        attack -=2
        print "++Rapid shot attack (-2): "+str(attack)
        dmg = raw_input("Roll Damage? [y/n]")
        if dmg == 'n':
            print "Done."
            return
        else:
            first = self.arrow_shot(mc=mc, pbs=pbs, drow=drow, mh=mh)
            print "Total dmg: "+str(first[0]+first[1]+first[2])
            print

    def standard_attack(self, attack, mc, pbs, drow, mh ):
        print "++Standard shot attack (-0): "+str(attack)
        dmg = raw_input("Roll Damage? [y/n]")
        if dmg == 'n':
            print "Done."
            return
        else:
            first = self.arrow_shot(mc=mc, pbs=pbs, drow=drow, mh=mh)
            print "Total dmg: "+str(first[0]+first[1]+first[2])
            print

    def multishot(self, attack, mc, pbs, drow, mh):
        print "++Multishot attack (-4): "+str(attack)
        attack -=4
        dmg = raw_input("Roll Damage? [y/n]")
        if dmg == 'n':
            print "Done."
            return
        else:
            print "++Frist arrow:"
            first = self.arrow_shot(mc=mc, pbs=pbs, drow=drow, mh=mh)
            print "++Second arrow:"
            second = self.arrow_shot(mc=mc, pbs=pbs, drow=drow, mh=mh)
            print "Total fire: "+str(first[0]+second[0])
            print "Total shock: "+str(first[1]+second[1])
            print "Total normal: "+str(first[2]+second[2])
            print "Total dmg: "+str(first[0]+second[0]+first[1]+second[1]+first[2]+second[2])
            print

    def nat_20(self, roll):
        if roll == 20:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print "!!!!!!!!!!!! NAT 20 !!!!!!!!!!!!!!!!!"
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        else:
            print "d20 was: "+str(roll)
