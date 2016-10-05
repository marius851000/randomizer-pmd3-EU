#PMD3/2 randomizer EU#
##1. Présention##
Ce logiciel, en réalité une compilation de logiciel et de script, permet deux chose :

1. Exporter des version randomizer US en version randomizer EU ( ici pour mdrngzer, ici fourni ) en version EU, soit cinq langue ( dont le français et l'anglais ).

2. [WIP] Randomizer les sprites et les portraits de l'overworld, de maniére cohérente ( sprite de dracaufeu = portrait de dracaufeu ) ou non. Permet aussi de randomizer les musiques, mais crash dans la majorité des cas peut aprés avoir fini le premier donjon.

##2. Comment utiliser ce logiciel ?##

###1. Export de rom random US à version EU###

Pour exporter une rom US randomizer à une rom EU normal, il vous faut:
* Ce logiciel
* Une rom EU vierge
* Une rom US, randomizer ou non

1. Si votre rom **US** est déja randomizer, aller à la partie 2. Si votre rom n'est pas randomizer, aller dans le dossier "mdrngzer 0.10.0", executer "mdrngzer.exe", une fois ouvert, selectionner une rom **US** et paramétrer votre random avec le logiciel. Ensuite, valider et enregistrer votre rom dans le dossier principal de la compilation, sous le nom de "rom-US.nds", et aller à la partie 3.
2. Si vous n'avez pas compilez la rom en suivant l'étape 1, copier-coller votre rom **US** dans le dossier principal de la compilation. 
3. Copier-coller votre rom **EU** dans le dossier principal sous le nom de "rom-EU.nds".
4. executer le fichier "a US - EU.bat" et, quand la fenetre de la console se sera fermer, vous obtiendrez le fichier randomizer sous le nom de "pmd-random.nds".

###2. Randomization des sprites, portraits et musiques###

Pour randomizer les sprites, portraits et musiques, il vous faut:

* Ce logiciel
* Une rom EU, randomizer ou non
* Python 3.1

1. Copier-coller votre rom EU dans le dossier principal de la compilation sous le nom de "rom-EU.nds".
2. Editez le fichier "ran.txt" selon vos besoins, voir le grand 3.
3. Executer le fichier "EU ran.bat" et vous obtiendrez le fichier randomizer sous le nom de "pmd-random.nds".

###3. Compilation du 2.1 et 2.2###

Pour transferer un random d'une rom **US** et la transferer vers un random **EU** ( ou randomizer les donjon et les stats ), puis randomizer les sprites, portraits et musiques de l'overworld d'un seul coup, il vous faut.

* Ce logiciel
* Une rom EU vierge*
* Une rom US, randomizer ou non
* Python 3.1

1. faire les trois premiére étape du 2.1.
2. Executer "a US - EU + ran.bat" et vous obtiendrez la rom **EU** randomizer sous le nom de "pmd-random.nds".

##3 Modifier le fichier ran.txt##

"ran.txt" est le fichier qui permet de définir comment son randomizer les portraits, sprites et musique de l'overworld.
Il se compose comme un fichier ".txt" normal, pouvant être ouvert avec le bloc-note, Wordpad ou autre.

Il se compose telle-quel :
'bienvenue dans ce programme d'exemple
spritepkmn
portrait


Pour faire des commentaire, rapporter vous à l'exemple.

'salut

'il peut y avoir des ligne vide
'd'alleur, ce n'est pas obliger qu'il y ait des apostrophe en debut de ligne :
coucou le monde
'cepandant, l'apostrophe est préférable.
'd'alleur, la ligne ci dessous ne fonctionnera pas.
spritepkmn 'un commentaire ou espace aprés la commande et celle ci ne pourras pas fonctionner.
'le fichier doit toujours se finir par un saut de ligne ou un commentaire.


Les commande peuvent être entrer dans le fichier "ran.txt", mais le fichier dois se terminer par un saut de ligne ou un commentaire.

liste des différente commande :

* musicf:Randomize les musique du jeu. **Attention, fonctionnalité béta, peut faire crasher le jeu peut aprés le premier donjon**.
* portrait:Randomize les portraits de maniére indépandante des sprites.
* spritepkmn:Randomize les sprites de maniére indépandante des portraits.
* overworld:Randomize les portraits et les sprites de maniére ordonner : sprites de pikachu = portraits de pikachu. **WIP, actuellement, peu de pokémon sont compatible avec cette fonction, les autres seront randomizer de maniére indépandante**.
