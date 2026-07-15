# CHALLENGE 01 

Desenvolver uma aplicação para a análise de tráfego com a responsabilidade de capturar pacotes de uma interface de rede e exibir estatísticas básicas.

## Requisitos:

**Captura de Pacotes:**
* Desenvolva um script ou aplicação que capture pacotes de uma interface de rede especificada.
* Utilize uma biblioteca ou ferramenta adequada para realizar a captura de pacotes (por exemplo Scapy em Python).
* Capture os seguintes campos dos pacotes: endereço IP de origem, endereço IP de destino, protocolo, tamanho do pacote.

**Análise de Tráfego:**
* Calcule e exiba estatísticas básicas sobre o tráfego capturado, incluindo: Número total de pacotes capturados.
* Número de pacotes por protocolo (por exemplo, TCP, UDP).
* Top 5 endereços IP de origem com mais tráfego.
* Top 5 endereços IP de destino com mais tráfego.

**Armazenamento:**
* O armazenamento dos pacotes capturados em um banco de dados.

**Tecnologias Utilizadas:**
* Utilize a linguagem de programação de sua preferência, preferencialmente Python.
* O script deverá ser executado em um Docker.

## Critérios de Avaliação:

* **Funcionalidade:** A aplicação deve ser capaz de capturar pacotes de rede e exibir estatísticas básicas sobre o tráfego.
* **Documentação:** Deve ser fornecida uma documentação explicando como configurar, executar e usar a aplicação. Além disso, é importante enviar informações justificando as escolhas e decisões tomadas para resolução do desafio, ex: schema da base de dados, informações relevantes sobre o script, etc.

## Entrega:

* Envie o código junto com a documentação.

---

# CHALLENGE 02

Você atua em uma equipe de infraestrutura e precisa analisar grandes volumes de logs para identificar falhas, erros ou comportamentos suspeitos.

Seu desafio é criar um prompt eficaz que possa ser utilizado por uma IA (como ChatGPT, Claude, Gemini, etc.) para:
* Ler um trecho de log bruto. 
* Identificar mensagens de erro, falhas ou comportamentos anômalos. 
* Explicar resumidamente o que pode estar acontecendo e oferecer uma sugestão de solução simples.

## Você deve enviar: 

1. Um prompt completo, como se fosse colado diretamente na IA. 
2. Um exemplo de trecho de log (pode usar o fornecido abaixo, ou expandido por você). 
3. Uma resposta esperada da IA, com a interpretação das mensagens relevantes. 

## Exemplo de log que deveria ser enviado para IA: 

```text
Unset 
May 16 14:01:22.123: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/1, changed state to down 
May 16 14:01:22.125: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/1, changed state to down 
May 16 14:01:23.101: %SPANTREE-5-TOPO_CHANGE: Topology Change Notice received on VLAN0010 
May 16 14:01:23.105: %SPANTREE-6-PORTSTATE: Port G11/8/3 state changed from FORWARDING to BLOCKING 
May 16 14:01:24.001: %SPANTREE-6-PORTSTATE: Port G11/0/4 state changed from BLOCKING to LISTENING 
May 16 14:01:26.003: %SPANTREE-6-PORTSTATE: Port Gi1/0/4 state changed from LISTENING to LEARNING 
May 16 14:01:28.005: %SPANTREE-6-PORTSTATE: Port Gi1/0/4 state changed from LEARNING to FORWARDING 
May 16 14:01:28.006: %SPANTREE-5-ROOTCHANGE: Root changed for VLAN0010 
New root is 00e0.b6ff.eell, cost is 19, port Gi1/0/4 
May 16 14:01:30.000: %CDP-4-DUPLEX_MISMATCH: duplex mismatch discovered on GigabitEthernet1/0/2 (full), with SW-Backup GigabitEthernet0/1 (half). 
May 16 14:01:32.500: %PORT_SECURITY-2-PSECURE_VIOLATION: Security violation occurred on interface GigabitEthernet1/0/5 
May 16 14:01:35.500: %SYS-5-CONFIG_I: Configured from console by vtył (192.168.1.5) 
```