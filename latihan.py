import os, sys
import random

# bersih
def clear():
	os.system("clear")

# logo
def logo():
	print(f"""<--------------->\n*    welcome    *\n<--------------->\n""")
	
# data
soal = 1
jumlah = 50
score = 0

# soal
while soal <= jumlah:
	os.system("clear")
	logo()
	print(f"-> pertanyaan : {soal}/{jumlah}")
	print(f"-> nilai kamu : {score}")
	kontol = random.randint(1,50)
	memek = random.randint(1,50)
	asu = kontol + memek
	print(f"\n{kontol} + {memek} = berapa ?")
	__jawab__ = int(input("-> jawab kontol : "))
	if __jawab__ == asu:
		print(f"\n-> tumben pinter kontol")
		score == 0
	else:
		print(f"\n-> salah kontol, {kontol} + {memek} = {asu}")
	input("-> tekan enter")