import re as louislepatron

path = input("Chemin vers le fichier :")

path = path.replace("\\","/")

#On va chercher les infos nécessaires dans le fichier
f = open(path,'r')
tab_lines = f.read().split("\n")
f.close()

new_path = louislepatron.split("\/([a-zA-Z0-9_-]+)\.sql", path)
f_new=open(new_path[0] + "/" + new_path[1] + "_NEW.sql",'w')
taille_tableau = len(tab_lines)

for x, line in enumerate(tab_lines):
    if x < taille_tableau - 1:
        f_new.write('"' + line + '" + RC + ...' + "\n")
    else:
        f_new.write('"' + line + '"' + "\n")

f_new.close()