## Zookeeper no Kafka

O Zookeeper desempenha um papel crucial no ecossistema do Apache Kafka. Ele é usado para gerenciar e coordenar os brokers do Kafka, garantindo a alta disponibilidade e a consistência dos dados.

### Funções do Zookeeper no Kafka:

1. **Gerenciamento de Brokers**: Zookeeper mantém uma lista de todos os brokers que fazem parte do cluster Kafka e monitora a saúde dos brokers.
2. **Gerenciamento de Partições e Replicação**: Zookeeper armazena informações sobre as partições dos tópicos e suas réplicas, coordenando a replicação entre os brokers.
3. **Liderança de Partições**: Zookeeper é responsável por eleger o líder para cada partição, que lida com todas as operações de leitura e escrita.
4. **Gerenciamento de Consumidores**: Zookeeper rastreia o progresso dos consumidores no cluster Kafka, armazenando informações sobre o deslocamento (offset) lido.
5. **Configuração Centralizada**: Zookeeper armazena configurações centralizadas para o cluster Kafka.

No nosso projeto, o Zookeeper é configurado no arquivo `docker-compose.yml` e é usado pelo Kafka para gerenciar brokers, partições, replicação e consumidores.


## Como o Apache Kafka Funciona

O Apache Kafka é uma plataforma de streaming distribuída que permite a publicação, subscrição, armazenamento e processamento de fluxos de registros em tempo real. Ele é projetado para ser escalável, durável e de alta performance.

### Componentes Principais do Kafka:

1. **Produtores (Producers)**: Aplicações que enviam (publicam) mensagens para o Kafka.
2. **Consumidores (Consumers)**: Aplicações que leem (consomem) mensagens do Kafka.
3. **Tópicos (Topics)**: Categorias ou feeds de mensagens para onde os produtores enviam dados e de onde os consumidores leem dados.
4. **Partições (Partitions)**: Divisões de tópicos que permitem paralelismo e escalabilidade.
5. **Brokers**: Servidores que armazenam dados e servem como intermediários entre produtores e consumidores.
6. **Zookeeper**: Gerencia e coordena os brokers do Kafka.

### Como o Kafka Funciona:

1. **Produção de Mensagens**: Produtores enviam mensagens para tópicos específicos no Kafka.
2. **Armazenamento de Mensagens**: Mensagens são armazenadas de forma durável nos brokers do Kafka.
3. **Consumo de Mensagens**: Consumidores se inscrevem em tópicos e leem mensagens das partições.
4. **Gerenciamento de Offsets**: Kafka rastreia o deslocamento (offset) de cada mensagem lida por um consumidor.

### Exemplo de Fluxo de Dados:

1. Um produtor envia uma mensagem para o tópico "transações".
2. A mensagem é armazenada em uma partição do tópico "transações" em um broker Kafka.
3. Um consumidor inscrito no tópico "transações" lê a mensagem da partição e a processa.