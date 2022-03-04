from random import randint 
import module

cities_list=module.get_cities('cities.txt')
Comp_word=cities_list[randint(0,len(cities_list))]
history=[]
print('Игра началась',Comp_word,sep='\n')
attempt=0
while  attempt!=5:
  history.append(Comp_word)
  attempt=0
  Gamer_word=input('Ваш ход ')
  comp_1=module.check_wrong(Comp_word,history)
  if not  module.get_mistace(Gamer_word,history,cities_list,comp_1,attempt):
    print('Вы проиграли, игра закончена')
    break  
  history.append(Gamer_word)
  lenc=module.check_wrong(Gamer_word,history)
  i=0
  while i<len(cities_list):    
      if cities_list[i] not in history and cities_list[i][0].lower()==lenc.lower():
          Comp_word=cities_list[i]
          print(Comp_word)
          break
      i+=1
  if i==len(cities_list)-1:
      print('Вы выиграли, поздравляю. ')
      break
module.get_history(history)


  

