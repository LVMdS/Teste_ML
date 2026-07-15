[cite_start]**PORTUGUÊS** [cite: 1]
[cite_start]**02 DIAS PARA REALIZAÇÃO DE TODOS OS CHALLENGES** [cite: 2]

---

# [cite_start]CHALLENGE 01 [cite: 3]

[cite_start]Desenvolver uma aplicação para a análise de tráfego com a responsabilidade de capturar pacotes de uma interface de rede e exibir estatísticas básicas. [cite: 4]

## [cite_start]Requisitos: [cite: 5]

[cite_start]**Captura de Pacotes:** [cite: 6]
* [cite_start]Desenvolva um script ou aplicação que capture pacotes de uma interface de rede especificada. [cite: 7]
* [cite_start]Utilize uma biblioteca ou ferramenta adequada para realizar a captura de pacotes (por exemplo Scapy em Python). [cite: 8]
* [cite_start]Capture os seguintes campos dos pacotes: endereço IP de origem, endereço IP de destino, protocolo, tamanho do pacote. [cite: 9]

[cite_start]**Análise de Tráfego:** [cite: 10]
* [cite_start]Calcule e exiba estatísticas básicas sobre o tráfego capturado, incluindo: Número total de pacotes capturados. [cite: 11]
* [cite_start]Número de pacotes por protocolo (por exemplo, TCP, UDP). [cite: 12]
* [cite_start]Top 5 endereços IP de origem com mais tráfego. [cite: 13]
* [cite_start]Top 5 endereços IP de destino com mais tráfego. [cite: 14]

[cite_start]**Armazenamento:** [cite: 15]
* [cite_start]O armazenamento dos pacotes capturados em um banco de dados. [cite: 16]

[cite_start]**Tecnologias Utilizadas:** [cite: 17]
* Utilize a linguagem de programação de sua preferência, preferencialmente Python. [cite_start]O script deverá ser executado em um Docker. [cite: 18]

## [cite_start]Critérios de Avaliação: [cite: 19]

* [cite_start]**Funcionalidade:** A aplicação deve ser capaz de capturar pacotes de rede e exibir estatísticas básicas sobre o tráfego. [cite: 21]
* [cite_start]**Documentação:** Deve ser fornecida uma documentação explicando como configurar, executar e usar a aplicação. [cite: 22] [cite_start]Além disso, é importante enviar informações justificando as escolhas e decisões tomadas para resolução do desafio, ex: schema da base de dados, informações relevantes sobre o script, etc. [cite: 23]

## [cite_start]Entrega: [cite: 24]

* [cite_start]Envie o código junto com a documentação. [cite: 25]

---

# [cite_start]CHALLENGE 02 [cite: 26]

[cite_start]Você atua em uma equipe de infraestrutura e precisa analisar grandes volumes de logs para identificar falhas, erros ou comportamentos suspeitos. [cite: 27]

[cite_start]Seu desafio é criar um prompt eficaz que possa ser utilizado por uma IA (como ChatGPT, Claude, Gemini, etc.) para: [cite: 28]
* [cite_start]Ler um trecho de log bruto. [cite: 29]
* [cite_start]Identificar mensagens de erro, falhas ou comportamentos anômalos. [cite: 30]
* [cite_start]Explicar resumidamente o que pode estar acontecendo e oferecer uma sugestão de solução simples. [cite: 31]

## [cite_start]Você deve enviar: [cite: 32]

1. [cite_start]Um prompt completo, como se fosse colado diretamente na IA. [cite: 33]
2. [cite_start]Um exemplo de trecho de log (pode usar o fornecido abaixo, ou expandido por você). [cite: 34]
3. [cite_start]Uma resposta esperada da IA, com a interpretação das mensagens relevantes. [cite: 35]

## [cite_start]Exemplo de log que deveria ser enviado para IA: [cite: 36]

```text
[cite_start]Unset [cite: 37]
[cite_start]May 16 14:01:22.123: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/1, changed state to down [cite: 38]
[cite_start]May 16 14:01:22.125: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/1, changed state to down [cite: 39]
[cite_start]May 16 14:01:23.101: %SPANTREE-5-TOPO_CHANGE: Topology Change Notice received on VLAN0010 [cite: 40]
[cite_start]May 16 14:01:23.105: %SPANTREE-6-PORTSTATE: Port G11/8/3 state changed from FORWARDING to BLOCKING [cite: 41]
[cite_start]May 16 14:01:24.001: %SPANTREE-6-PORTSTATE: Port G11/0/4 state changed from BLOCKING to LISTENING [cite: 42]
[cite_start]May 16 14:01:26.003: %SPANTREE-6-PORTSTATE: Port Gi1/0/4 state changed from LISTENING to LEARNING [cite: 43]
[cite_start]May 16 14:01:28.005: %SPANTREE-6-PORTSTATE: Port Gi1/0/4 state changed from LEARNING to FORWARDING [cite: 44]
[cite_start]May 16 14:01:28.006: %SPANTREE-5-ROOTCHANGE: Root changed for VLAN0010 [cite: 45]
[cite_start]New root is 00e0.b6ff.eell, cost is 19, port Gi1/0/4 [cite: 46]
[cite_start]May 16 14:01:30.000: %CDP-4-DUPLEX_MISMATCH: duplex mismatch discovered on GigabitEthernet1/0/2 (full), with SW-Backup GigabitEthernet0/1 (half). [cite: 47]
[cite_start]May 16 14:01:32.500: %PORT_SECURITY-2-PSECURE_VIOLATION: Security violation occurred on interface GigabitEthernet1/0/5 [cite: 48]
[cite_start]May 16 14:01:35.500: %SYS-5-CONFIG_I: Configured from console by vtył (192.168.1.5) [cite: 49]
```