#encoding=utf-8

__authors__ = "Paulo Gil, Marlene Bastos"
__email__ = "paulogil@ua.pt, marlenebastos.mb@ua.pt"
__version__ = "1.0"

import sqlite3 as sql
import os 
import sys

def main(argv):
	cls()
	
	reload(sys)  
	sys.setdefaultencoding('utf8')

	global db
	db = sql.connect(argv[1])
	x = "0"

	while True:
		if x == "0":
			x = main_menu()
			if x == "0":
				sys.exit()
		elif x == "1":
			x = menu_1()
			
			if x == "1":
				x = menu_1_autor()

				if x == "9":
					x = "1"
				elif x == "0":
					sys.exit()

			elif x == "2":
				x = menu_1_titulo()

				if x == "9":
					x = "1"
				elif x == "0":
					sys.exit()

			elif x == "3":
				x = menu_1_estado()

				if x == "9":
					x = "1"
				elif x == "0":
					sys.exit()

			elif x == "4":
				x = menu_1_listar()

				if x == "9":
					x = "1"
				elif x == "0":
					sys.exit()

			elif x == "9":
				x = "0"
			elif x == "0":
				sys.exit()

		elif x == "2":
			x = menu_2()
			
			if x == "9":
				x = "0"
			elif x == "0":
				sys.exit()

		elif x == "3":
			x = menu_3()

			if x == "1":
				x = menu_3_listar()

				if x == "9":
					x = "3"
				elif x == "0":
					sys.exit()

			elif x == "2":
				x = menu_3_listuser()

				if x == "9":
					x = "3"
				elif x == "0":
					sys.exit()

			elif x == "3":
				x = menu_3_criar()

				if x == "9":
					x = "3"
				elif x == "0":
					sys.exit()

			elif x == "4":
				x = menu_3_eliminar()

				if x == "9":
					x = "3"
				elif x == "0":
					sys.exit()
			elif x == "9":
				x = "0"

			elif x == "0":
				sys.exit()

		elif x == "4":
			x = menu_4()

			if x == "1":
				x = menu_4_addlivro()

				if x == "9":
					x = "4"
				elif x == "0":
					sys.exit()

			elif x == "2":
				x = menu_4_remlivro()

				if x == "9":
					x = "4"
				elif x == "0":
					sys.exit()

			elif x == "3":
				x = menu_4_adduser()

				if x == "9":
					x = "4"
				elif x == "0":
					sys.exit()

			elif x == "4":
				x = menu_4_remuser()

				if x == "9":
					x = "4"
				elif x == "0":
					sys.exit()

			elif x == "9":
				x = "0"

			elif x == "0":
				sys.exit()

		elif x == "0":
			sys.exit()

		else:
			main_menu()

	db.close()

#Main menu
def main_menu():
	cls()
	print "--------------------------------------"
	print "|          GERIR BIBLIOTECA          |"
	print "--------------------------------------"
	print "\n"
	print "1: Procurar livros"
	print "2: Listar utilizadores"
	print "3: Gerir requisições"
	print "4: Gerir base de dados"
	print "0: Sair"
		
	a = raw_input("Opção: ")
	return a

#Menu 1 - Procurar livros
def menu_1():
	cls()
	print "--------------------------------------"
	print "|           PROCURAR LIVROS          |"
	print "--------------------------------------"
	print "\n"
	print "1: Procurar livros por autor"
	print "2: Procurar livros por título"
	print "3: Procurar livros por estado"
	print "4: Listar todos"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 1.1 - Procurar livros por autor
def menu_1_autor():
	cls()
	print "--------------------------------------"
	print "|     PROCURAR LIVROS POR AUTOR      |"
	print "--------------------------------------"
	print "\n"

	name = raw_input("Nome do autor: ")
	result = db.execute("SELECT * FROM books WHERE autor LIKE \'%s\'" % name)
	rows = result.fetchall()

	count = 0
	for row in rows:
		print "------------------------------"
		print "Título: %s" % row[1]

		if row[3] == 0:
			print "Estado: Não requisitado"
		elif row[3] == 1:
			print "Estado: Requisitado"

		count += 1
	print "------------------------------"
	
	if count == 0:
		print "Não foram encontrados livros do autor %s.\n" % name
	elif count == 1:
		print "Foi encontrado 1 livro do autor %s.\n" % name
	else:
		print "Foram encontrados %i livros do autor %s.\n" % (count, name)

	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 1.2 - Procurar livros por título
def menu_1_titulo():
	cls()
	print "--------------------------------------"
	print "|     PROCURAR LIVROS POR TÍTULO     |"
	print "--------------------------------------"
	print "\n"

	name = raw_input("Título do livro: ")
	result = db.execute("SELECT * FROM books WHERE titulo LIKE \'%s\'" % name)
	rows = result.fetchall()

	count = 0
	for row in rows:
		print "------------------------------"
		print "Título: %s" % row[1]
		print "Autor: %s" % row[2]
		
		if row[3] == 0:
			print "Estado: Não requisitado"
		elif row[3] == 1:
			print "Estado: Requisitado"
		count += 1

	print "------------------------------"
	if count == 0:
		print "Não foram encontrados livros com o nome %s." % name
	
	print "\n"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 1.3 - Procurar livros por estado
def menu_1_estado():
	cls()
	print "--------------------------------------"
	print "|     PROCURAR LIVROS POR ESTADO     |"
	print "--------------------------------------"
	print "\n"

	print "0: Procurar livros não requisitados"
	print "1: Procurar livros requisitados"
	
	estado = raw_input("Estado do livro: ")

	result = db.execute("SELECT * FROM books WHERE req LIKE \'%s\'" % estado)
	rows = result.fetchall()

	count = 0
	for row in rows:
		print "------------------------------"
		print "Título: %s" % row[1]
		print "Autor: %s" % row[2]
		count += 1

	print "------------------------------"

	if count == 0:
		if estado == "0":
			print "Não foram encontrados livros não requisitados."
		elif estado == "1":
			print "Não foram encontrados livros requisitados."
	
	elif count == 1:
		if estado == "0":
			print "Foi encontrado 1 livro não requisitado."
		elif estado == "1":
			print "Foi encontrado 1 livro requisitado."

	else:
		if estado == "0":
			print "Foram encontrados %i livros não requisitados." % count
		elif estado == "1":
			print "Foram encontrados %i livros requisitados." % count

	print "\n"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 1.4 - Listar livros 
def menu_1_listar():
	cls()
	print "--------------------------------------"
	print "|            LISTAR LIVROS           |"
	print "--------------------------------------"

	result = db.execute("SELECT * FROM books;")
	rows = result.fetchall()
	
	count = 0
	for row in rows:
		print "------------------------------"
		print "Nome: %s" % row[1]
		print "Autor: %s" % row[2]
		
		if row[3] == 0:
			print "Estado: Não requisitado"
		elif row[3] == 1:
			print "Estado: Requisitado"
		count += 1
	
	print "------------------------------"
	
	if count == 0:
		print "Não foram encontrados livros na biblioteca\n"
	else:
		print "Foram encontrados %i livros na biblioteca.\n" % count
			
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 2 - Listar utilizadores 
def menu_2():
	cls()
	print "--------------------------------------"
	print "|        LISTAR UTILIZADORES         |"
	print "--------------------------------------"

	result = db.execute("SELECT * FROM users;")
	rows = result.fetchall()
	
	count = 0
	for row in rows:
		print "------------------------------"
		print "Nome: %s" % row[1]
		print "Email: %s" % row[2]
		print "Contacto: %i" % row[3]
		count = count + 1
	print "------------------------------"
	print "Foram encontrados %i utilizadores.\n" % count
			
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 3 - Listar requisições 
def menu_3():
	cls()
	print "--------------------------------------"
	print "|          GERIR REQUISIÇÕES         |"
	print "--------------------------------------"
	print "\n"
	print "1: Listar todas as requisições"
	print "2: Listar requisições por utilizador"
	print "3: Fazer nova requisição"
	print "4: Eliminar requisição"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 3.1 - Listar todas as requisições 
def menu_3_listar():
	cls()
	print "--------------------------------------"
	print "|    LISTAR TODAS AS REQUISIÇÕES     |"
	print "--------------------------------------"
	print "\n"
	
	result = db.execute("SELECT * FROM requisitions;")
	rows = result.fetchall()
	
	count = 0
	for row in rows:
		print "------------------------------"
		print "Utilizador: %s" % row[1]
		print "Título: %s" % row[2]
		print "Data da requisição: %s" % row[3]
		print "Data de entrega: %s" % row[4]
		count += 1

	print "------------------------------"
	
	if count == 0:
		print "Não foram encontradas requisições.\n"
	elif count == 1:
		print "Foi encontrada 1 requisição.\n"
	else:
		print "Foram encontradas %i requisições.\n" % count
	
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 3.2 - Listar requisições por utilizador
def menu_3_listuser():
	cls()
	print "--------------------------------------"
	print "| LISTAR REQUISIÇÕES POR UTILIZADOR  |"
	print "--------------------------------------"
	print "\n"
	
	user = raw_input("Utilizador: ")
	result = db.execute("SELECT * FROM requisitions WHERE user LIKE \'%s\'" % user)
	rows = result.fetchall()
	
	count = 0
	for row in rows:
		print "------------------------------"
		print "Título: %s" % row[2]
		print "Data da requisição: %s" % row[3]
		print "Data de entrega: %s" % row[4]
		count += 1

	print "------------------------------"
	
	if count == 0:
		print "Não foram encontradas requisições do utilizador %s.\n" % user
	elif count == 1:
		print "Foi encontrada 1 requisição do utilizador %s.\n" % user
	else:
		print "Foram encontradas %i requisições do utilizador %s.\n" % (count, user)
	
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 3.3 - Fazer requisições 
def menu_3_criar():
	cls()
	print "--------------------------------------"
	print "|          FAZER REQUISIÇÃO          |"
	print "--------------------------------------"
	print "\n"
	
	user = raw_input("Utilizador: ")
	result1 = db.execute("SELECT * FROM users WHERE nome LIKE \'%s\'" % user)
	rows1 = result1.fetchall()

	count1 = 0
	for row in rows1:
		count1 += 1

	if count1 == 0:
		print "O utilizador %s não foi encontrado." % user
	else:
		book = raw_input("Livro: ")
		result2 = db.execute("SELECT * FROM books WHERE titulo LIKE \'%s\'" % book)
		rows2 = result2.fetchall()

		count2 = 0
		for row in rows2:
			count2 += 1

		if count2 == 0:
			print "O livro %s não foi encontrado." % book
		else:
			data_req = raw_input("Data da requisição: ")
			data_lim = raw_input("Data de entrega: ")
			update1 = db.execute("INSERT INTO requisitions VALUES(null,\'%s\',\'%s\',\'%s\',\'%s\')" % (user, book, data_req, data_lim))
			db.commit()
			update2 = db.execute("UPDATE books SET req = 1 WHERE titulo LIKE \'%s\'" % book)
			db.commit()
			print "------------------------------"
			print "O livro foi requisitado com sucesso por %s" % user

	print "\n"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 3.4 - Eliminar requisições 
def menu_3_eliminar():
	cls()
	print "--------------------------------------"
	print "|        ELIMINAR REQUISIÇÃO         |"
	print "--------------------------------------"
	print "\n"
	
	book = raw_input("Nome do livro: ")
	
	result1 = db.execute("DELETE FROM requisitions WHERE book LIKE \'%s\'" % book)
	db.commit()
	
	result2 = db.execute("UPDATE books SET req = 0 WHERE titulo LIKE \'%s\'" % book)
	db.commit()
	
	print "Requisição eliminada com sucesso.\n"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 4 - Gerir base de dados
def menu_4():
	cls()
	print "--------------------------------------"
	print "|        GERIR BASE DE DADOS         |"
	print "--------------------------------------"
	print "\n"
	print "1: Adicionar livro"
	print "2: Remover livro"
	print "3: Adicionar utilizador"
	print "4: Remover utilizador"
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 4.1 - Adicionar livro
def menu_4_addlivro():
	cls()
	print "--------------------------------------"
	print "|          ADICIONAR LIVRO           |"
	print "--------------------------------------"
	print "\n"

	titulo = raw_input("Título: ")
	autor = raw_input("Autor: ")

	result = db.execute("INSERT INTO books VALUES(null,\'%s\',\'%s\',0)" % (titulo, autor))
	db.commit()
	print "O livro '%s' foi adicionado com sucesso.\n" % titulo
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 4.2 - Remover livro
def menu_4_remlivro():
	cls()
	print "--------------------------------------"
	print "|           REMOVER LIVRO            |"
	print "--------------------------------------"
	print "\n"

	titulo = raw_input("Título: ")

	result1 = db.execute("DELETE FROM books WHERE titulo LIKE \'%s\'" % titulo)
	db.commit()
	result2 = db.execute("DELETE FROM requisitions WHERE book LIKE \'%s\'" % titulo)
	db.commit()
	result3 = db.execute("UPDATE books SET req = 0 WHERE titulo LIKE \'%s\'" % book)
	db.commit()

	print "O livro %s foi removido com sucesso.\n" % titulo
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 4.3 - Adicionar utilizador
def menu_4_adduser():
	cls()
	print "--------------------------------------"
	print "|        ADICIONAR UTILIZADOR        |"
	print "--------------------------------------"
	print "\n"

	nome = raw_input("Nome: ")
	email = raw_input("Email: ")
	contacto = raw_input("Contacto: ")

	result = db.execute("INSERT INTO users VALUES(null,\'%s\',\'%s\',\'%s\')" % (nome, email,contacto))
	db.commit()
	print "O utilizador %s foi adicionado com sucesso.\n" % nome
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

#Menu 4.4 - Remover utilizador
def menu_4_remuser():
	cls()
	print "--------------------------------------"
	print "|         REMOVER UTILIZADOR         |"
	print "--------------------------------------"
	print "\n"

	nome = raw_input("Nome: ")

	result0 = db.execute("SELECT * FROM requisitions WHERE user LIKE \'%s\'" % nome)
	rows = result0.fetchall()

	for row in rows:
		book = row[2]
		result1 = db.execute("UPDATE books SET req = 0 WHERE titulo LIKE \'%s\'" % book)
		db.commit()
	
	result2 = db.execute("DELETE FROM users WHERE nome LIKE \'%s\'" % nome)
	db.commit()
	result3 = db.execute("DELETE FROM requisitions WHERE user LIKE \'%s\'" % nome)
	db.commit()

	print "O utilizador %s foi removido com sucesso.\n" % nome
	print "9: Voltar"
	print "0: Sair"

	a = raw_input("Opção: ")
	return a

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

main(sys.argv)