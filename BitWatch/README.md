# ⌚ BitWatch - Checkup de Sistema (Versão Alfa)

O **BitWatch** é o seu novo monitor de hardware leve e preciso. Atualmente em fase **Alfa**, o projeto foca na coleta bruta de dados essenciais diretamente via terminal, garantindo que o "motor" do programa seja robusto antes da próxima grande evolução.

## 🚀 O que o BitWatch monitora?
O sistema realiza um checkup profundo dos componentes vitais:
- **Pulso da CPU**: Monitoramento de carga em tempo real com baixo impacto no sistema.
- **Gestão de Memória**: Exibe RAM total e disponível em GB, com cálculos precisos de uso.
- **Sentinela de RAM**: Um alerta inteligente que avisa quando a memória livre cai abaixo de 10% do total.
- **Termômetro Multinível**: Tenta ler a temperatura via `psutil` ou `WMI`. Caso o hardware oculte os sensores, o BitWatch utiliza uma **Lógica de Estimativa** baseada em carga para manter você informado.
- **Stress Test (Turbo)**: Ferramenta integrada de estresse multinúcleo para testar a estabilidade do processador em situações críticas.

## 🔮 O que vem por aí? (Roadmap)
O BitWatch vai crescer! As próximas versões trarão:
- [ ] **Interface Gráfica (GUI)**: Uma janela intuitiva e moderna com design em tons pastéis.
- [ ] **Gráficos Dinâmicos**: Visualização visual do histórico de uso da CPU e RAM.
- [ ] **Log de Eventos**: Registro de picos de temperatura e falta de memória para diagnóstico posterior.

## 🛠️ Tecnologias
- **Linguagem**: Python 3.x
- **Bibliotecas**: `psutil`, `wmi`, `multiprocessing`

---
### 👨‍💻 Autor
**Darwin Cruz Lopes** *Focado em transformar dados complexos em informações úteis.* *Apoio técnico: Gemini AI*