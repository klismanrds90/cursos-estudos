# Banco Online
Proposta de projeto da plataforma DIO para o bootcamp "Potência Tech powered by iFood | Ciências de Dados com Python"
Uma simulação de um sistema de banco online criado em Python. O programa permite que os usuários realizem operações bancárias básicas, como depósitos, saques, consultas de saldo e visualização do extrato.

# Funcionalidades
O sistema oferece as seguintes funcionalidades:

Depósito: os usuários podem realizar depósitos em suas contas fornecendo o valor do depósito. O saldo da conta é atualizado e o registro do depósito é adicionado ao extrato.

Saque: os usuários podem efetuar saques informando o valor do saque desejado. Antes de realizar a operação, são feitas algumas validações, como a verificação do saldo disponível e do limite diário de saque configurado para R$500.00. O saldo da conta é atualizado e o registro do saque é adicionado ao extrato.

Consulta de saldo: os usuários podem verificar o saldo atual de suas contas.

Extrato: os usuários podem visualizar o extrato detalhado das transações realizadas em suas contas. O extrato exibe os registros de depósito e saque, bem como o saldo atual da conta.

# Requisitos
O programa foi desenvolvido em Python e não requer nenhuma biblioteca externa além das bibliotecas padrão do Python.

# Como usar
Clone este repositório para o seu ambiente local.

Abra um terminal e navegue até o diretório do projeto.

Execute o arquivo banco.py usando o interpretador Python.

Siga as instruções exibidas no terminal para realizar as operações bancárias desejadas. Utilize os números do menu para selecionar a opção desejada.

O programa exibirá mensagens de confirmação, informações sobre saldo e extrato, e mensagens de erro quando necessário.

# Observações
Certifique-se de utilizar o separador decimal "." ao inserir valores monetários (por exemplo, 1000.50).

O programa utiliza comandos de limpeza de tela específicos para sistemas operacionais Windows (cls) e macOS/Linux (clear). Caso esteja utilizando um sistema operacional diferente, pode ser necessário ajustar esses comandos no código.
