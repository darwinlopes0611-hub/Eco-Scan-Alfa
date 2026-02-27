import psutil
import wmi
import time
import math
import multiprocessing

# --- Kernel (Funções) ---
# (Aqui ficam as suas funções pegar_temperatura e estressar_nucleo)


if __name__ == "__main__":
    # OS PRINTS DEVEM FICAR AQUI DENTRO:
    print("-----------------------------------------------------------")
    print("EcoScan Alfa - version 1.0")
    print("-----------------------------------------------------------")
    print("by: Darwin Cruz Lopes")
    
    # Restante do código de execução...

    #variáveis para coletar status do sistema
    memoria_aviso=False
    cpu_aviso=False
    superaquecimento_aviso=False


def coletar_status_sistema():
    # Coleta os dados brutos da memória
    mem = psutil.virtual_memory()
    
    # 1. RAM Total (GB)
    ram_total = mem.total / (1024**3)
    
    # 2. RAM Disponível (GB) - Usando a lógica de dividir por 1024 três vezes
    ram_disponivel_gb = mem.available / (1024**3)
    
    # 3. Variável de 10% da RAM (Limite de segurança)
    limite_10_porcento = ram_total * 0.10
    
    # 4. Uso da CPU (%)
    # Nota: interval=0.1 para a função não "travar" por 1 segundo inteiro
    cpu_uso = psutil.cpu_percent(interval=0.1)
    
    # 5. Porcentagem de RAM usada
    ram_uso_pct = mem.percent

    # Retorna todas as informações para serem usadas fora da função
    return ram_total, ram_disponivel_gb, limite_10_porcento, cpu_uso, ram_uso_pct

def pegar_temperatura():

    # TENTATIVA 1: psutil (Padrão/Rápido)
    try:
        temp = psutil.sensors_temperatures()
        if temp:
            for nome, entradas in temp.items():
                return f"{entradas[0].current}°C"
    except:
        pass

    # TENTATIVA 2: WMI (Agressivo/Windows)
    try:
        w = wmi.WMI(namespace="root\\wmi")
        temp_k = w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature
        # Cálculo: (Kelvin / 10) - 273.15
        return f"{(temp_k / 10.0) - 273.15:.1f}°C"
    except:
        pass

    # TENTATIVA 3: Estimativa (Seguro/Não trava)
    cpu = psutil.cpu_percent()
    if cpu > 75: return "Alta (Est.)"
    if cpu > 40: return "Média (Est.)"
    return "Baixa (Est.)"

def estressar_nucleo():
    """Executa cálculos que a CPU aguenta sem dar erro de limite."""
    timeout = time.time() + 60
    while time.time() < timeout:
        # Potência de números grandes funciona bem para estresse
        _ = 2**100000 

if __name__ == "__main__":
    contagem_nucleos = multiprocessing.cpu_count()
    print(f"Iniciando estresse em {contagem_nucleos} núcleos por 60 segundos...")
    
    processos = [] # Lista com o nome correto
    
    for _ in range(contagem_nucleos):
        p = multiprocessing.Process(target=estressar_nucleo)
        p.start()
        processos.append(p)

    try:
        for p in processos:
            p.join()
    except KeyboardInterrupt:
        print("\nInterrompido.")
        for p in processos:
            p.terminate()
    



# --- Exemplo de como você vai usar no código ---
if __name__ == "__main__":
    # Coleta o status do sistema
    ram_total, ram_disponivel_gb, limite_10_porcento, cpu_uso, ram_uso_pct = coletar_status_sistema()
    
    # Exibe o status coletado
    print(f"RAM Total: {ram_total:.2f} GB")
    print(f"RAM Disponível: {ram_disponivel_gb:.2f} GB")
    print(f"Limite de Segurança (10% da RAM): {limite_10_porcento:.2f} GB")
    print(f"Uso da CPU: {cpu_uso}%")
    print(f"Porcentagem de RAM Usada: {ram_uso_pct}%")
if __name__ == "__main__":
    if ram_disponivel_gb < limite_10_porcento and not memoria_aviso:
        print("AVISO: RAM disponível abaixo de 10% do total!")
        memoria_aviso = True
    if cpu_uso > 90 and not cpu_aviso:
        print("AVISO: Uso da CPU acima de 90%!")
        cpu_aviso = True
    temperatura = pegar_temperatura()
    if temperatura and "Est." not in temperatura and float(temperatura.replace("°C", "")) > 80 and not superaquecimento_aviso:
        print(f"AVISO: Temperatura alta detectada! ({temperatura})")
        superaquecimento_aviso = True



    

   

