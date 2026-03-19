# guardar.py
import os
import sys

# Si no pones mensaje, te lo pide
if len(sys.argv) > 1:
    mensaje = sys.argv[1]
else:
    mensaje = input("Describe qué hiciste: ")

os.system("git add .")
os.system(f'git commit -m "{mensaje}"')
os.system("git push")

print("Listo, código guardado en GitHub!")  