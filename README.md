Integração com RavvitMQ

Este projeto demonstra o uso do RabbitMQ como sistema de mensageria utilizando o serviço CloudAMQP. 

A estrutura do projeto é a seguinte:
.
├── config.py             # Configurações globais (URL do CloudAMQP, nome da fila)
├── produtor.py           # Produtor que envia eventos de usuário
├── consumidor_log.py     # Consumidor que registra mensagens recebidas em log
├── consumidor_login.py   # Consumidor que processa eventos de login
├── README.md             # Documentação do projeto

CloudAMPQ 
Acesse https://www.cloudamqp.com/
Crie uma conta e uma instância gratuita (plano Little Lemur).
Clique em cima do nome do container 
Em AMQP detail, copie a URL de conexão AMQP, no formato:

Como Executar

Verificar se tem python instalado na maquina, para verificar digite o seguinte comando no prompt de comando 
python --version

Instalar dependencias 
pip install pika 
