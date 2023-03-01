class PocketMonster :

    def __init__(self,name,pv,sf,sr, type, actions) :
        
        self.name = name
        self.pv = pv
        self.force = sf
        self.resistance = sr
        self.type = type
        self.actions = actions

    def perdPv(self, atqForce, multiplicateur):

        tempPv = ((atqForce * multiplicateur) - self.resistance)

        if (tempPv > 0):
            self.pv -= tempPv

    def affichage(self):

        print("----------------------------------")
        print("| Nom :" + self.name)
        print("| Type :" + self.type)
        print("| PV :" + str(self.pv))
        print("| Force :" + str(self.force))
        print("| PV :" + str(self.resistance))
        print("----------------------------------")

    def affichageAttaque(self):

        for action in self.actions :
            print("--------------------------------------------------------------------------------------------------------------------------------")
            action.affichage()
            print("--------------------------------------------------------------------------------------------------------------------------------")

    def getName(self) :

        return self.name

    def getPv(self) :

        return self.pv

    def getForce(self) :

        return self.force

    def getResistance(self) :

        return self.resistance

    def getType(self) :

        return self.type


class Action :

    def __init__(self, type, power, name, texte) :
        
        self.name = name
        self.type = type
        self.power = power
        self.texte = texte

    def affichage(self) :
        print(self.name + " - " + self.type + " : " + self.texte)

    def getType(self) :

        return self.type

    def getPower(self) :

        return self.power

    def getName(self) :

        return self.name

    def getTexte(self) :

        return self.texte


class Jeu :

    def __init__(self, pmAtq, pmDef) :

        self.pocketMonsterAtq = pmAtq
        self.pocketMonsterDef = pmDef
        self.round = 0

    def affichage(self) :

        print("===================== Round "+ str(self.round) +" =========================")
        print(" ")
        print("                        Defenseur")
        self.pocketMonsterDef.affichage()
        print(" ")
        print(" ")
        print("Attaquant")
        self.pocketMonsterAtq.affichage()
        print(" ")
        self.pocketMonsterAtq.affichageAttaque()




def compareTypes(typeAtq, typeDef) :

    if ((typeAtq == "Feu" and typeDef == "Plante") or (typeAtq == "Plante" and typeDef == "Eau") or (typeAtq == "Eau" and typeDef == "Feu")):
        return 2
    else :
        return 1


def attaque(pmAtq , pmDef, action):

    pmDef.perdPv( pmAtq.getForce() * action.getPower(), compareTypes(action.getType(), pmDef.getType()))


nouvelle = Action("Feu", 1, "Corriger sa nouvelle", "Corrige et critique la nouvelle du Pocket Monster adverse !")
coherence = Action("Feu", 2, "Critiquer la cohérence", "Critique la cohérence d'écriture du Pocket Monster adverse !")
blanc = Action("Eau", 0, "Gros blanc", "Laisse un blanc après la phrase, laissant douter le Pocket Monster adverse...")

coherenceDA = Action("Plante", 2, "Critiquer la cohérence", "Critique la cohérence sur la direction artistique du Pocket Monster adverse !")
metroid = Action("Plante", 2, "Demander un Metroidvania", "Demande au Pocket Monster adverse la creation de 10 niveaux metroidvania liés entre eux, seul, de 10 000 tuiles")
pointUn = Action("Feu", 1.1,"Attaque.1", "Attaque le pokemon avec un multiplicateur de 1.1 parce qu'on aime les barèmes cheloux ici")

rtx3090 = Action("Eau", 2, "Demander une RTX3090","Demande au Pocket Monster adverse une RTX3090 pendant 3 mois")
battlefront = Action("Eau", 1, "Parler de Battlefront", "Démontre à quel point BattleFront est un super jeu")
polygon = Action("Feu", 1, "Polygon à 5 côtés", "Montre que le Pocket Monster adverse à un polygon à 5 côtés")


frank = PocketMonster("Frank Barre", 100, 25, 10, "Feu", [nouvelle,coherence,blanc])
axel = PocketMonster("Axel Domenger", 100, 15, 20, "Plante", [coherenceDA,metroid,pointUn])
jerome = PocketMonster("Jerome Lesage", 100, 20, 15, "Eau", [rtx3090,battlefront,polygon])

game = Jeu(axel,jerome)


winner = 'null'

while (winner == 'null') :

    game.affichage()

    action = int(input())








