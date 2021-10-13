import random as rd
import time
import os


def forca_one():
	print("""\033[1;33m
				    |
				    |__________
				    |      |
				    |      |
				    |    ● ●    
				    |     -- 
				    |
				    |
				    |
				  __|__	
				
			

\033[m""")


def forca_two():
	print("""\033[1;33m
				    |
				    |__________
				    |      |
				    |      |
				    |    ● ●   
				    |     -- 
				    |     ■   
				    |     ■  
				    |     ■   
				  __|__	
			
\033[m""")

def forca_tree():
	print("""\033[1;35m
				    |
				    |____________
				    |      |
				    |      |
				    |    ● ●    
				    |     -- 
				    | === ■     
				    |     ■   
				    |     ■   
				  __|__	
				
		
\033[m""")

def forca_four():
	print("""\033[1;35m
				    |
				    |____________
				    |      |
				    |      |
				    |    ● ●    
				    |     -- 
				    | === ■ ===   
				    |     ■   
				    |     ■    
				  __|__	
			
		
\033[m""")

def forca_five():
	print("""\033[1;31m
				    |
				    |____________
				    |      |
				    |      |
				    |    ● ●     
				    |     -- 
				    | === ■ ===    
				    |     ■  
				    |     ■   
				  __|__ ■  
			
		
\033[m""")


def forca_six(palavra):
	os.system("clear")
	titulo("● VOCÊ FOI ENFORCADO   ●")
	print("""\033[1;31m
				    |
				    |____________
				    |      |
				    |      |
				    |    ● ●     
				    |     -- 
				    | === ■ ===      
				    |     ■   
				    |     ■   
				  __|__ ■  ■        
				
	
\033[m""")
	print(f"  ■  A palavra era : {palavra}")


def castigo():
	os.system("clear")
	titulo("● VOCÊ FOI ENFORCADO COMO CASTIGO   ●")
	print("""\033[1;31m
				    |
				    |____________
				    |      |
				    |      |
				    |    ● ●    		
				    |     -- 
				    | === ■ ===  
				    |     ■   
				    |     ■   
				  __|__ ■  ■       
				
\033[m""")



def titulo(texto):
	response = texto.upper()
	print(f"{response:^90}","\n" * 2)
	
	
	
def jogo():
	game_on = True


	coisas = [ "prato","colher","pano","chinelo","sofa","armario" ]
	comidas = [ "hambuerguer","pao","pizza","lasanha","feijoada"]
	roupas = ["tenis","sapato","moletom","casaco","jaqueta","meia"]
	estacoes = ["verao","outono","inverno","primavera"]
	profissoes = [ "dentista","advogado","policial","programador","psicanalista","psicopedagogo","psicologo"]
	bebidas = [ "whisky","cerveja","rum","suco","cha","cafe"]
	animais = ["dinossauro","rinoceronte","aguia","papagaio","onitorrinco","borboleta","baleia"]
	
	classe = [coisas, comidas, roupas, estacoes, profissoes,bebidas,animais]
	sortea_classe = rd.choice(classe)
	palavra = sortea_classe
	sorteada =  rd.choice(palavra)


	icon = "*" * len(sorteada)
	print(f"\033[1m					\033[1;36m|\033[m  {icon}  \033[1;36m|\033[m \033[m")
	p = " "
	response = [ ]
	erro = 0
	ant_trapaca = 0 
	while game_on:
		jogador = str(input("\033[1;36m  •  Adivinhe :\033[m  "))
		if len(jogador) > 1:
			ant_trapaca += 1
			print(f"\033[1;31m  •  Não tente trapacear... você foi avisado !\033[m")
			time.sleep(0.9)
			os.system("clear")
		else:
			response.append(jogador)
			
		if ant_trapaca == 3:
			os.system("clear")
			print(f"\033[1;31m\n\n EU AVISEI....!\033[m")
			time.sleep(0.5)
			castigo()
			while p not in "SN":
				print("\n")
				p = str(input("  •  Deseja Jogar Novamente [ S / N ] : ")).upper().strip()
				if p in "S":
					os.system("clear")
					jogo()
			if p in "N":
				break	
			
		
		if len(jogador) == 1:
			os.system("clear")
			adivinhacao = ""
			for letra in sorteada:
				if letra in response:
					adivinhacao+= letra
				else:
					adivinhacao += "*"
			
						
			if adivinhacao == sorteada:
				print("\n")
				print(f"\033[1m			\033[1;36m|\033[m  {adivinhacao}  \033[1;36m|\033[m \033[m")
				print("\n\n  ● Parabéns, você escapou da forca.")
				print("\n")
				while p not in "SN":
					p = str(input("  •  Deseja Jogar Novamente [ S / N ] : ")).upper().strip()
					if p in "S":
						os.system("clear")
						jogo()
				if p in "N":
					break	
			else:
				print("\n")
				print(f"\033[1m					\033[1;36m|\033[m  {adivinhacao}  \033[1;36m|\033[m \033[m")
				print("\n")
			
			if jogador not in sorteada:
				erro += 1
			
			
			if erro == 1:
				forca_one()
			elif erro == 2:
				forca_two()
			elif erro == 3:
				forca_tree()
			elif erro == 4:
				forca_four()
			elif erro == 5:
				forca_five()
			if erro >= 6:
				os.system("clear")
				forca_six(sorteada)
				while p not in "SN":
					print("\n")
					p = str(input("  •  Deseja Jogar Novamente [ S / N ] : ")).upper().strip()
					if p in "S":
						os.system("clear")
						jogo()
				if p in "N":
					break	
					
				
				
				
				
				
				

jogo()
