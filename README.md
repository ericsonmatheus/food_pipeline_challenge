# Desafio Food Pipeline

## Descrição
Este projeto realiza uma análise exploratória de dados utilizando Python. Os dados são gerados sinteticamente com a biblioteca Faker, simulando cenários realistas de vendas, clientes e produtos. O objetivo é testar técnicas de análise de dados sem depender de dados reais.

## Funcionalidades
- Geração de dados sintéticos (vendas, clientes e produtos)
- Análise exploratória de dados (EDA)
- Visualização de tendências e padrões
- Estatísticas descritivas para insights iniciais

## Tecnologias Utilizadas
- Python
- Pandas
- Faker
- Matplotlib / Seaborn
- Pre-commit (para garantir qualidade do código)

## Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/synthetic-data-analysis.git
2. Acesse o diretório do projeto:
   ```sh
   cd nc-report-generator
   ```
3. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Instale as dependências do pre-commit
   ```sh
   pre-commit install
   ```

## Uso
Execute a aplicação com o seguinte comando:


## Licença
Este projeto está sob a licença MIT.


## Descrição dos desafios

### Desafio 1: SQL Avançado – Análise de Vendas e Fidelização
- Objetivo: Avaliar a capacidade do manipulação e analisar dados relacionais, identificando padrões de compra e retenção de clientes.

- Cenário: Você trabalha na equipe de dados de uma grande rede de supermercados. O time de marketing quer entender quais clientes têm maior recorrência de compras e quais produtos são mais propensos a recompras.

#### Tarefas:

- Encontre os 5 produtos mais vendidos no último trimestre.

- Identifique os clientes com maior frequência de compras nos últimos 6 meses.

- Calcule o ticket médio mensal dos clientes e identifique se há tendência de crescimento ou queda.

- Descubra quais categorias de produtos possuem maior taxa de recompra (mesmo cliente comprando o mesmo produto em datas diferentes).


### Desafio 2: Python e ETL – Construção de um Pipeline de Dados
- Objetivo: Avaliar a capacidade de construir ETLs para organizar e preparar dados para análise.

- Cenário: A empresa recebe diariamente um arquivo CSV contendo dados de pedidos de fornecedores. O time precisa processar e armazenar essas informações em um banco de dados para futuras análises.

#### Tarefa:

- Criar um script Python que leia o arquivo CSV, limpe e normalize os dados (removendo duplicatas e preenchendo valores ausentes).

- Implementar uma transformação que crie uma coluna total_value = quantity * unit_price.

- Inserir os dados processados em um banco PostgreSQL (pode ser um dataframe pandas simulando a base).

- Criar um agendamento simples no Airflow para rodar o pipeline diariamente.


### Desafio 3: Advanced Analytics e Visualização de Dados
- Objetivo: Testar a habilidade de transformar dados brutos em insights acionáveis por meio de análise exploratória e visualização.

- Cenário: O time comercial quer entender o impacto das promoções nos hábitos de compra dos clientes. Eles fornecem um dataset com compras antes, durante e depois de uma campanha promocional.

#### Tarefa:

- Identificar o impacto das promoções no volume de vendas de cada categoria de produto.

- Criar um gráfico que compare a média de gasto dos clientes antes, durante e depois da promoção.

- Analisar se a promoção atraiu novos clientes ou apenas fez clientes recorrentes anteciparem compras.

- Criar um dashboard interativo (Power BI, Tableau ou Streamlit) para apresentar os insights.
