import hashlib

def new_mdp():
    mdp = input("Entrez un mot de passe avec au moins 8 caractères dont une majuscule , une minuscule, un chifre et un caractère speciaux : \n")
    
    caractere_spe = ("&","#","_","@","+","-","*","=","<",">","?","§","!","£","$")
    nbcar = False ; maj = False ; minus = False ; chiffre = False ; spe = False
    condition = False
    while condition == False:
        if len(mdp) >= 8 :
            nbcar = True
        for car in mdp:
            if car.isupper() == True:
                maj = True
            elif car.islower() == True:
                minus = True
            elif car.isdigit() == True:
                chiffre = True
            elif car in caractere_spe:
                spe = True

        if nbcar ==True and maj == True and minus == True and chiffre == True and spe == True:
            print("Le mot de passe est corect")
            cryp_mdp(mdp)
            condition = True
        else:
            print("Le mot de passe n'est pas correct")
            mdp = input("Entrez un mot de passe avec au moins 8 caractères dont une majuscule , une minuscule, un chifre et un caractère speciaux : \n")

def cryp_mdp(mdp):
    cryp = hashlib.sha256(mdp.encode()).hexdigest()
    print(cryp)

new_mdp()