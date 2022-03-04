def get_mistace(Gamer_word,history,cities_list,comp_1,attempt):
  k=True
  while (Gamer_word in history or Gamer_word not in cities_list or comp_1.lower()!=Gamer_word[0].lower()) and attempt<5:
    Gamer_word=input('Попробуйте еще раз ')
    attempt+=1        
  else:
      if attempt==5:
        k=False
  return k


def check_wrong(word,history):
  wrong=['ь','ъ','ы','ё','ц']
  if word[-1] in wrong:
    comp=history[len(history)-2]
    return comp[0]
  else:
    return word[-1]

def get_cities(file_name):
  file=open(file_name,'r',encoding='utf-8')
  f=file.read()
  cities_list=f.split('\n')
  file.close()
  return cities_list

def get_history(history):
  h=open('history.txt','w')
  for i in history:
    h.writelines(i+'\n')
  h.close() 
  