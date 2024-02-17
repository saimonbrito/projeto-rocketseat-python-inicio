"""Module providing a function printing python3.12.2"""

def adicionar_tarefa(tarefas, nome_tarefa):
  """Function printing python python3.12.2"""
  try:
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\ntarefa {nome_tarefa} adcionada com secesso!")
    return
  except Exception as erro:
    print(f"Erro: {erro}")

def ver_tarefas(tarefas):
  """Function printing python python3.12.2"""
  try:
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
      status = "✓" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
      print(f"{indice }, [{status}] {nome_tarefa}")
      return
  except Exception as erro:
    print(f"Erro: {erro}")  

def atualizar_nome_tarefa(tarefas,indice_tarefa,novo_nome_tarefa):
  try:
      indece_tarefa_ajustado = int(indice_tarefa) -1
      if indece_tarefa_ajustado >= 0 and indece_tarefa_ajustado < len(tarefas):
        tarefas[indece_tarefa_ajustado] ["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizar para  {novo_nome_tarefa}")
        
      else:
        print("Indice de tarefa invalido.")
      
      return
  except Exception as erro:
    print(f"Erro: {erro}")
    
def completar_tarefa(tarefas , induce_tarefas):
  try:
    indece_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indece_tarefa_ajustado] ["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada completada")
    return
  except Exception as erro:
    print(f"Erro: {erro}")
  

def deletar_tarefas(tarefas):
  try:
    for tarefa in tarefas:
      if tarefa["completada"]:
        tarefas.remove(tarefa)
    print("tarefas completadas deletadas. ")
    return
  except Exception as erro:
    print(f"Erro: {erro}")

tarefas = []

while True:
  print("\nmenu gerenciador de tarefas")
  print("1, Adcionar tarefas")
  print("2, Ver tarefas")
  print("3, Atualizar tarefas")
  print("4, Completar tarefas")
  print("5, deletar tarefas")
  print("6, Sair")
  
  escolha = input("Digite sua escolha:  ")
  if escolha == "1":
    nome_tarefa = input("\nDigite a tarefa: ")
    adicionar_tarefa(tarefas, nome_tarefa)
    
  elif escolha == "2":
    ver_tarefas(tarefas)
    
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)   
    ver_tarefas(tarefas)   
  
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o numero da tarefa que deseja completar: ")
    completar_tarefa(tarefas, indice_tarefa)
  
  elif escolha == "5":
    deletar_tarefas(tarefas)
    ver_tarefas(tarefas)
  elif escolha == "6":
    break

print("Fim do programa")