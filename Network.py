#!/usr/bin/python3
# -*- coding: utf8 -*-


# Python Network script :
# 
# Change DB creds before launch :
#
# Import Plugins for Bash commands, Apt Package, MYSQL Query:
import subprocess
import apt
import mysql.connector

# Cache from APT Package
cache = apt.Cache()

# Print Instructions at launch :
print()
print("Lancement Programme Installation Réseau en cours ...")
print()
print("1 - Installer un Serveur Web (Apache / NginX)")
print()
print("2 - Installer un Serveur Wordpress (Apache - PHP - MYSQL)")
print()
print("3 - Installer un Serveur de Fichiers (NFS / SFTP)")
print()
print("4 - Installer un Routeur (DHCP - DNS - NTP - Network Forwarding)")
print()
print("5 - Installer un Serveur VPN (OpenVPN)")
print()
print("6 - Quitter le Script")
print()

# Asking user what he wants to do (Main Menu):
user_answer = input("Que voulez-vous faire ? (1, 2, 3, 4, 5, 6) : ")

# If Statements for Menu Options :
if user_answer == "1":
  print()
  user_answer_web = input("Quel serveur Web voulez-vous installer ? (1 = Apache / 2 = NginX) : ")
  if user_answer_web =="1":
    print()
    print("Installation d'Apache en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "apache2", "-y"])
    print()
    print("Apache installé avec succès !")
    print()
  elif user_answer_web =="2":
    print()
    print("Installation de NginX en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "nginx", "-y"])
    print()
    print("NginX installé avec succès !")
    print()
  else:
    print()
    print("Choisissez une option d'installation valide . Fermeture du script ...")
    print()
elif user_answer == "2":
  print()
  user_answer_web = input("Voulez-vous installer un serveur Wordpress sur une base LAMP ? (1 = Oui / 2 = Non) : ")
  if user_answer_web =="1":
    print()
    print("Installation du serveur Wordpress en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "apache2", "php7.4-fpm", "php7.4-mysql", "mariadb-server", "-y"])
    subprocess.call(["sudo", "a2enmod", "proxy_fcgi", "setenvif"])
    subprocess.call(["sudo", "a2enconf", "php7.4-fpm"])
    subprocess.call(["sudo", "systemctl", "restart", "apache2"])
    print()
    print("Packets Wordpress installé avec succès !")
    print()
    print("Configuration des services Web  ... ")
    print()
    print("Création et configuration de la base de données ...")
# Database Connection and Queriess :
    db_connection = mysql.connector.connect(
    host= "localhost",
    user= "wordpressuser",
    passwd= "wordpresspassword"
    )
    db_cursor = db_connection.cursor()
    print()
    db_cursor.execute("CREATE DATABASE wordpressdb")
    db_cursor.execute("CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'wordpresspassword'")
    db_cursor.execute("GRANT ALL PRIVILEGES ON * . * TO 'wordpressuser'@'localhost'")
    db_cursor.execute("FLUSH PRIVILEGES")
    print("Base de données & Utilisateur crées avec succès !")
    print()
    print("Identifiants créers par défault, à changer immédiatement :")
    print()
    print()
    print("Nom de la Base de Données : wordpressdb")
    print()
    print("Utilisateur de la Base de Données : wordpressuser")
    print()
    print("Mot de passe de la Base de Données : wordpresspassword")
    print()
    print()
    print("Suppression du fichier de configuration Apache par défaut ...")
    subprocess.call(["sudo", "rm", "-rif", "/var/www/html/index.html"])
    print()
    print("Téléchargement de l'archive Wordpress en cours ...")
    print()
    subprocess.call(["wget", "-q", "-c", "http://wordpress.org/latest.tar.gz"])
    print("Extraction et déplacement de l'archive en cours ...")
    subprocess.call(["tar", "-xzvf", "/home/user1/latest.tar.gz", ">>", "/dev/null"])
    subprocess.call(["tar", "-xzf", "latest.tar.gz"])
    subprocess.call(["sudo", "mv", "wordpress/*", "/var/www/html/"])
    print()
    print("Extraction et Déplacement des fichiers Wordpress terminés !")
    print()
    print("Vous pouvez maintenant configurer votre Site Wordpress depuis votre navigateur Internet !")
    print()
  elif user_answer_web =="2":
    print()
    print("Annulation de l'installation du site Wordpress. Retour au menu ... ")
    print()
  else:
    print()
    print("Choisissez une option d'installation valide . Fermeture du script ...")
    print()
elif user_answer == "3":
  print()
  user_answer_files = input("Voulez-vous installer un Serveur de fichiers ? (1 = NFS / 2 = SFTP / 3 = Retour au menu) : ")
  if user_answer_files =="1":
    print()
    print("Installation d'un serveur de fichiers NFS en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "nfs-kernel-server", "-y"])
    print()
    print("Serveur de fichiers NFS installé avec succès !")
    print()
  elif user_answer_files =="2":
    print()
    print("Installation d'un serveur de fichiers SFTP en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "vsftpd", "-y"])
    print()
    print("Serveur de fichiers SFTP installé avec succès !")
    print()
  elif user_answer_files =="3":
    print()
    print("Annulation de l'installation du Serveur de fichiers. Retour au menu ... ")
    print()
  else:
    print()
    print("Choisissez une option d'installation valide . Fermeture du script ...")
    print()
elif user_answer == "4":
  print()
  user_answer_routeur = input("Voulez-vous installer un Pack Routeur ? (1 = Oui / 2 = Non) : ")
  if user_answer_routeur =="1":
    print()
    print("Installation d'un pack Routeur en cours ... ")
    print()
    print("Mises à Jour en cours ... ")
    print()
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "dist-upgrade", "-y"])
    subprocess.call(["sudo", "apt-get", "autoremove", "-y"])
    subprocess.call(["clear"])
    subprocess.call(["sudo", "apt-get", "install", "isc-dhcp-server", "-y"])
    print()
    print("Serveur DHCP installé avec succès !")
    print()
    subprocess.call(["sudo", "apt-get", "install", "bind9", "-y"])
    subprocess.call(["clear"])
    print()
    print("Serveur DNS installé avec succès !")
    print()
    subprocess.call(["sudo", "apt-get", "install", "chrony", "-y"])
    print()
    print("Serveur NTP installé avec succès !")
    print()
    print("Affichage des différentes sources choisis par le Serveur NTP ...")
    print()
    subprocess.call(["sudo", "chronyc", "sources"])
    print()
    print("Serveur Routeur installé avec succès ! ")
    print()
  elif user_answer_routeur =="2":
    print()
    print("Annulation de l'installation du Service Routeur. Retour au menu ... ")
    print()
  else:
    print()
    print("Choisissez une option d'installation valide . Fermeture du script ...")
    print()
elif user_answer == "5":
  print()
  print("Installation du Service VPN")
  print()
elif user_answer == "6":
  print()
  print("Fermeture du script ...")
  print()
else:
  print()
  print("Choisissez une option valide. Fermeture du script ...")
  print()


# END
#
