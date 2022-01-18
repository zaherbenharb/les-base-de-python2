#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


#exercice1 Écrivez un programme Python qui accepte le prénom et le nom de l'utilisateur et imprimez-les dans l'ordre inverse avec un espace entre eux.
nom=str 
prenom=str
print ('ecrire votre nom')
x= input (nom)
print ('ecrire votre prenom')
t= input (prenom)
print ('votre nom est',t,x)


# In[4]:


#exercice2 Ecrire un programme Python qui accepte un entier (n) et calcule la valeur de n+nn+nnn
#Exemple de valeur de n est 5 Résultat attendu : 615 (5+55+555) 
i= input("entre n")
i= int(i)
print(i + i*11 + i*111)


# In[ ]:





# In[ ]:





# In[3]:


#exercie 3 Écrivez un programme Python pour savoir si un nombre donné (accepté par l'utilisateur) est pair ou impair, imprimez un message approprié à l'utilisateur.
n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
   print("est Paire")
else:
   print( "est Impaire")


# In[6]:


#exercie 4 Écrivez un programme qui trouvera tous ces nombres qui sont divisibles par 7 mais qui ne sont pas un multiple de 5, entre 2000 et 3200 (les deux inclus). 
#Les nombres obtenus doivent être imprimés en séquence sur une seule ligne.
for i in range(2000,3201):
    if (i % 5) != 0 and (i % 7) == 0:
        print (i)


# In[7]:


#exercie5 Écrire un programme capable de calculer la factorielle d'un nombre donné. Les résultats doivent être imprimés en séquence sur une seule ligne. 
#Supposons que l'entrée suivante soit fournie au programme : 8 Alors, la sortie devrait être : 40320
nbr = int(input('Entrez un nombre : '))
x = 1
for i in range(1, nbr+1):
    x = x * i
print (nbr,'! = ',x)


# In[8]:


#exercie7 Dans ce défi, vous devez actualiser un prix en fonction de sa valeur.

#- Si le prix est de 500 ou plus, il y aura une remise de 50 %.

#- Si le prix est compris entre 200 et 500 (200 inclus), il y aura une remise de 30 %.

#- Si le prix est inférieur à 200, il y aura une remise de 10 %.
nbr = int(input('Entrez un nombre : '))
if nbr >= 500 :
    print("le prix apres solde ",nbr*0.5)
elif nbr <500 and nbr>=200:
     print("le prix apres solde ",nbr*0.7)
else : print ("le prix apres solde",nbr*0.9)


# In[ ]:




