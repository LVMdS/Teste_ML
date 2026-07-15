# Resolução - Challenge 02: Análise de Logs com IA

## 1. O Prompt

> Atue como um Engenheiro de Redes e Infraestrutura Sênior. Vou fornecer um trecho de log bruto de equipamentos de rede. Sua tarefa é analisar este log seguindo estritamente os seguintes passos:
> 
> 1. Leia o trecho de log fornecido.
> 2. Identifique e liste apenas as mensagens que indicam erro, falha de segurança ou comportamentos anômalos. (Ignore logs puramente informativos ou de rotina).
> 3. Para cada erro identificado, explique resumidamente o que está acontecendo na infraestrutura.
> 4. Ofereça uma sugestão de solução técnica simples e direta para cada problema.
> 
> Aqui está o trecho do log:

---

## 2. O Trecho de Log

```text
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

---

## 3. Resposta Esperada da IA


**Análise de Logs de Infraestrutura:**

**Problema 1: Queda de Interface Física e Lógica**
* **Log Identificado:** `%LINK-3-UPDOWN: Interface GigabitEthernet1/0/1, changed state to down` e `%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/1, changed state to down`
* **O que está acontecendo:** A interface física GigabitEthernet1/0/1 perdeu comunicação e caiu, causando consequentemente a queda do protocolo de linha. Isso geralmente indica um cabo desconectado, rompido ou o equipamento na outra ponta sendo desligado.
* **Sugestão de Solução:** Verifique o cabeamento físico conectado à porta Gi1/0/1 e confirme se o dispositivo conectado a ela está ligado e operante.

**Problema 2: Incompatibilidade de Duplex (Duplex Mismatch)**
* **Log Identificado:** `%CDP-4-DUPLEX_MISMATCH: duplex mismatch discovered on GigabitEthernet1/0/2 (full), with SW-Backup GigabitEthernet0/1 (half).`
* **O que está acontecendo:** O protocolo CDP detectou que a porta local (Gi1/0/2) está operando em Full-Duplex, enquanto o switch vizinho (SW-Backup) está operando em Half-Duplex. Isso gera colisões (late collisions) e extrema lentidão na rede.
* **Sugestão de Solução:** Acesse a interface de ambos os equipamentos envolvidos e padronize a configuração. Recomenda-se fixar ambas as portas em `full-duplex` ou deixá-las em auto-negociação (`auto`).

**Problema 3: Violação de Segurança de Porta**
* **Log Identificado:** `%PORT_SECURITY-2-PSECURE_VIOLATION: Security violation occurred on interface GigabitEthernet1/0/5`
* **O que está acontecendo:** O recurso de *Port Security* detectou que um endereço MAC não autorizado tentou se comunicar através da porta GigabitEthernet1/0/5. Isso gerou uma violação e muito provavelmente colocou a porta em estado de erro (*err-disable*).
* **Sugestão de Solução:** Identifique qual dispositivo foi conectado a esta porta. Se for um equipamento legítimo da empresa, atualize o endereço MAC permitido nas configurações da interface. Após resolver, reinicie a porta administrativamente (comandos `shutdown` seguido de `no shutdown`).