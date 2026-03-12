import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas):
    descricao = input("\nDigite a descrição da tarefa: ").strip()
    if descricao:
        tarefa = {
            "id": len(tarefas) + 1,
            "descricao": descricao,
            "concluida": False
        }
        tarefas.append(tarefa)
        print("✅ Tarefa adicionada com sucesso!")
    else:
        print("❌ A descrição não pode estar vazia.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\n📋 Nenhuma tarefa cadastrada ainda.")
        return
    
    print("\n=== SUAS TAREFAS ===")
    for tarefa in tarefas:
        status = "✓" if tarefa["concluida"] else " "
        print(f"{tarefa['id']}. [{status}] {tarefa['descricao']}")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa para marcar como concluída: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                print("✅ Tarefa marcada como concluída!")
                return
        print("❌ Tarefa não encontrada.")
    except ValueError:
        print("❌ Digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa para remover: "))
        for i, tarefa in enumerate(tarefas):
            if tarefa["id"] == id_tarefa:
                tarefas.pop(i)
                # Reindexar IDs
                for idx, t in enumerate(tarefas, 1):
                    t["id"] = idx
                print("🗑️ Tarefa removida com sucesso!")
                return
        print("❌ Tarefa não encontrada.")
    except ValueError:
        print("❌ Digite um número válido.")

def main():
    tarefas = carregar_tarefas()
    print("🚀 Bem-vindo ao seu Gerenciador de Tarefas!")

    while True:
        print("\n" + "="*40)
        print("1. Adicionar nova tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        print("="*40)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("\n👋 Até logo! Suas tarefas foram salvas automaticamente.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()