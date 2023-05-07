# Internet_Secured_Chat
Programme de communication Type "chat" avec un server dans le cadre 
du cours de cryptographie de 1er semestre en bachelor ISC de HEI Sion,
donné par le Dr. Louis Lettry.

L'interface utilisateur se découpe en plusieurs zones : 
* Toute la partie gauche est une scrolling area, ou les 
messages échangés sur le serveur ainsi que leur états
sont affichés dans des zones cliquables.
* La partie droite en haut se trouve la zone d'envoi de message 
sur le serveur. Le texte à communiquer s'écrit dans cette zone
et la nature de l'envoi (t/s/i) peut être sélectionné via 
le menu déroulant. Enfin le message est envoyer via le bouton envoi.
* La partie droite médiane de l'interface agit comme zone de choix de 
cryptage/décryptage. Les différentes méthodes implémentées sont 
disponible par les onglets portant le nom des méthodes. Lors de l'envoi
d'un message, l'onglet ouvert est correspond é la méthode de crygtage 
à utiliser. Le même principe s'applique lors du décryptage de messages.
* La partie droite basse comprend deux zone de texte. Celle du haut
est la zone dans laquelle un message cliqué de la scroll area arrive. 
Il est ensuite possible de le décrypter en sélectionnant la méthode 
voulue et en utilisant le bouton correspondant. Le message décrpyté sera
inscrit dans la texte boxe du bas.

Pour lancer le programme, il faut lancer le fichier Main.py.
Le programme utilise un interpréteur python 3.10.0 et les python packages : PyQt6, gcd, click.
