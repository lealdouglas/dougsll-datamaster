# Data Master - Douglas Leal (Git template)

## 1. Objetivo do Case
Este projeto visa desenvolver uma solução de engenharia de dados para monitoramento de transações financeiras em tempo real. A plataforma utiliza Azure e GitHub Actions para criar e gerenciar recursos, com processamento de dados realizado no Databricks.

## 2. Arquitetura de Solução e Arquitetura Técnica
### 2.1 Arquitetura de Solução
A solução é composta por um pipeline de dados que captura, processa e armazena transações financeiras, com foco na detecção de fraudes. A arquitetura inclui:
- **Event Hub**: Para ingestão de dados em tempo real.
- **Databricks**: Para processamento e análise dos dados.
- **Storage Account**: Para armazenamento de dados brutos e processados.
- **Security**: Implementação de mascaramento de dados e políticas de acesso.
- **Observabilidade**: Monitoramento de pipeline e alertas em caso de falhas ou anomalias.

### 2.2 Arquitetura Técnica
Descreva a arquitetura técnica com um diagrama, se possível. Explique como cada componente se conecta:
- **Terraform**: Criação dos recursos na Azure.
- **GitHub Actions**: Automação da criação e configuração dos recursos.
- **Databricks**: Leitura dos dados do Event Hub e escrita no Data Lake.
- **Segurança e Compliance**: Implementação de mascaramento e criptografia de dados sensíveis.

## 3. Explicação sobre o Case Desenvolvido
### 3.1 Descrição do Fluxo de Dados
- **Extração de Dados**: Dados de transações são capturados em tempo real através do Event Hub.
- **Ingestão de Dados**: Dados são processados no Databricks e armazenados no Data Lake.
- **Observabilidade**: Monitoramento contínuo para garantir a integridade do fluxo de dados e detectar anomalias.
- **Segurança e Mascaramento**: Dados sensíveis são mascarados durante o processamento para cumprir regulamentações de segurança.

### 3.2 Tecnologias Utilizadas
- **Azure Event Hub**: Para captura de eventos.
- **Azure Databricks**: Para processamento de dados em escala.
- **Azure Storage Account**: Para armazenamento seguro.
- **GitHub Actions**: Para automação CI/CD.
- **Terraform**: Para provisionamento de infraestrutura.

## 4. Instruções para Configuração e Execução do Projeto
### 4.1 Pré-requisitos
- Conta na Azure
- Configuração do GitHub Actions
- Instalação do Terraform

### 4.2 Passos de Configuração
1. Clone o repositório: `git clone https://github.com/lealdouglas/dougsll-datamaster.git`
2. Configure suas credenciais da Azure no Terraform.
3. Execute as actions do repositório para criar os recursos:
4. Configure o GitHub Actions para automatizar os jobs no Databricks.
5. Execute o job no Databricks para processar os dados.

## 5. Melhorias e Considerações Finais
### 5.1 Melhorias Futuras
- montar .yaml para tf e incluir usuario principal, para vincular aos grupos.
- parametros recuperados via API para gerar uma imersao na experiencia poderiam estar configurados em um banco de dados.
- criar classe abstrata para datacontract ficar ainda mais como uma 'interface'
Escalabilidade: Melhorar o desempenho da ingestão de dados com particionamento de dados.
Segurança: Implementar autenticação baseada em tokens para APIs de terceiros.
Observabilidade: Adicionar métricas de performance e latência do pipeline.

### 5.2 Considerações Finais
Este projeto demonstra uma solução escalável e segura para monitoramento de transações financeiras em tempo real, utilizando ferramentas modernas de processamento de dados e automação de infraestrutura.

## 6. Referências
Links para documentações de Terraform, Databricks, Azure, etc.
