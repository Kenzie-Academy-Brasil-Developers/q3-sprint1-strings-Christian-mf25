# Código do dev aqui

def standardize_names(character_name):
	split_string = character_name.split()
	join_string = "-".join(split_string)
	return join_string

def standardize_title(title):
	return title.title()

def standardize_text(text):
	split_text = text.split()
	count = 0
	
	for word in split_text:
		if count == 0:
			split_text[count] = word.capitalize()
			count += 1
		elif word[-1] == "." and count != len(split_text) - 1:
			split_text[count + 1] = split_text[count + 1].capitalize()
			count += 1

	return " ".join(split_text)

def title_creator(text):
	hyphens = ""
	text_list = text.title().split()

	for _ in range(20):
		hyphens += "-"
	
	text_list[0] =  hyphens + text_list[0]
	text_list[-1] =  text_list[-1] + hyphens
	return " ".join(text_list)

def text_merge(text_a, text_b):
	list_a = text_a.split()
	list_b = text_b.split()
	list_b[0] = list_b[0].lower()
	if list_a[-1][-1] == ".":
		remove_dot = list(list_a[-1])
		remove_dot.pop()
		list_a[-1] = "".join(remove_dot)
	list_a.extend(list_b)
	text = " ".join(list_a)
	result = standardize_text(text)

	return result

text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar
uma   trama para seu novo livro. ela recebe ajuda por meio de uma
   carta de um      desconhecido, um nativo da ilha de Guernsey,
em cujas mãos havia chegado um livro    que há tempos tinha
pertencido    a Juliet.
"""

text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e
delicado.    usando metáforas culinárias, personagens peculiares
 e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

print(text_merge(text_of_blog_a, text_of_blog_b))