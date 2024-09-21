# Data Master - Douglas Leal

&nbsp;

<p align="center">
  <img src="assets/img/logo.png" width="300" alt="ideacao do projeto">
</p>
&nbsp;

O repositório "dougsll-datamaster" é uma solução para o programa Data Master organizado pela F1rst Santander. Solução proposta e desenvolvida por [Douglas Leal](https://www.linkedin.com/in/douglasleall/). <p>

&nbsp;
Este repositório contém o seguinte:

1. [Objetivo do Case](#1-objetivo-do-case)
   - [Início Rápido](#11-início-rápido)
2. [Arquitetura de Solução](#2-arquitetura-de-solução)
   - [Visão Geral](#21-visão-geral)
   - [Diagrama de Arquitetura de Solução](#22-diagrama-de-arquitetura-de-solução)
   - [Descrição dos Componentes](#23-descrição-dos-componentes)
   - [Características Essenciais (Case)](#24-características-essenciais-case)
3. [Arquitetura Técnica](#3-arquitetura-técnica)
   - [Visão Geral](#31-visão-geral)
   - [Sobre o Projeto](#32-sobre-o-projeto)
   - [Ideação do Projeto](#33-ideação-do-projeto)
   - [Descrição do Fluxo de Dados](#34-descrição-do-fluxo-de-dados)
   - [Tecnologias Utilizadas](#35-tecnologias-utilizadas)
   - [Infraestrutura como Código](#36-infraestrutura-como-código)
   - [Automações](#37-automações)
   - [Processamento de Dados](#38-processamento-de-dados)
   - [Armazenamento de Dados](#39-armazenamento-de-dados)
4. [Instruções para Configuração e Execução do Projeto](#4-instruções-para-configuração-e-execução-do-projeto)
   - [Pré-requisitos](#41-pré-requisitos)
   - [Passos de Configuração](#42-passos-de-configuração)
     - [Step 1. Clone o repositório](#step-1-clone-o-repositório)
     - [Step 2. Configure usuário de serviço (Service Principal)](#step-2-configure-usuário-de-serviço-service-principal)
     - [Step 3. Configure as secrets no GIT](#step-3-configure-as-secrets-no-git)
     - [Step 4. Configure arquivo de Setup Infraestrutura Lakehouse](#step-4-configure-arquivo-de-setup-infraestrutura-lakehouse)
     - [Step 5. Execute a action Strife Lakehouse](#step-5-execute-a-action-strife-lakehouse)
     - [Step 6. Execute a action Strife ADB Unity Catalog](#step-6-execute-a-action-strife-adb-unity-catalog)
     - [Step 7. Configure arquivo de contrato para ingestão](#step-7-configure-arquivo-de-contrato-para-ingestão)
     - [Step 8. Execute a action Jarvis Ingestão](#step-8-execute-a-action-jarvis-ingestão)
     - [Step 9. Configure seu projeto para explorar dados](#step-9-configure-seu-projeto-para-explorar-dados)
     - [Step 10. Execute a action Jarvis Asset Bundles](#step-10-execute-a-action-jarvis-asset-bundles)
5. [Melhorias e Considerações Finais](#5-melhorias-e-considerações-finais)
   - [Melhorias Futuras](#51-melhorias-futuras)
   - [Considerações Finais](#52-considerações-finais)
6. [Custos do Projeto](#6-custos-do-projeto)
7. [Referências](#7-referências)

&nbsp;

## 1. Objetivo do Case

Este projeto visa desenvolver uma solução de engenharia de dados com o principal objetivo de preparar um ambiente para estudo e exploração de dados baseado em nuvem em poucos minutos. O projeto simula a criação de um ambiente conceitual de dados para um domínio de dados, configurando o ambiente para realizar ações como pipelines de ingestão e exploração de dados.

### 1.1 Início Rápido

Para provisionar o ambiente e usar a plataforma,
[Instruções para Configuração e Execução do Projeto](#4-instruções-para-configuração-e-execução-do-projeto)

## 2. Arquitetura de Solução

### 2.1 Visão Geral

A solução é projetada para preparar um ambiente de estudo e exploração de dados baseado em nuvem em poucos minutos. Considere o seguinte cenário: Eu, como engenheiro de dados e/ou ML, a partir de uma subscrição demoninada como "domínio de dados riscos (drisc)" preciso montar o setup do meu ambiente cloud e criar o pipeline de dados, desde a ingestão até a construção de uma smart table. Nesse cenário, preciso considerar a configuração de um ambiente governado, baseado em uma arquitetura medalhão, explorar dados e implantar um motor. A solução deve permitir ao desenvolvedor configurar seu ambiente, simulando uma prateleira de recursos para dados, e, com poucas configurações, definir um fluxo de ingestão e entregar um ambiente para exploração de dados, integrado à jornada de implantação. Toda a jornada apresentada em um só lugar, de maneira básica e bem feita.

<p align="center">
  <img src="assets/img/solucao_ideia.PNG" width="750" alt="ideacao do projeto">
</p>

### 2.2 Diagrama de Arquitetura de Solução

A solução utiliza Azure como provedora de nuvem, Active Directory para gestão de grupos e usuários, Event Hub para ingestão de dados (opcional), Databricks para processamento e análise, Unity Catalog para governança e gestão dos dados, e Azure Storage para armazenamento seguro. Outras tecnologias, como o setup via Terraform e o gerenciamento das automações via contrato de dados, que visam simplificar a relação dos serviços com a plataforma e dados, também estão incorporadas nessa solução.

<p align="center">
  <img src="assets/img/solucao_v3.png" width="750" alt="Diagrama de Arquitetura">
</p>

### 2.3 Descrição dos Componentes

- **Event Hub (opcional)**: Captura dados de transações em tempo real de várias fontes, como sistemas de pagamento e bancos.
- **Azure Databricks**: Processa os dados capturados, executa algoritmos de detecção de fraudes e prepara os dados para armazenamento.
- **Azure Storage Account**: Armazena dados brutos e processados em camadas organizadas, conforme a arquitetura de medalhão (bronze, silver, gold).
- **Segurança**: Implementa políticas de mascaramento de dados e criptografia para proteger informações sensíveis.
- **Observabilidade**: Utiliza monitoramento contínuo para garantir o funcionamento correto do sistema, com alertas configurados para falhas e anomalias.

##### Ambição (AVALIAR DEPOIS):

- Relatório no cost analysis
- Lifecycle já implementado
- TTL vinculado ao contrato
- Bundles Databricks

<p align="center">
  <img src="assets/img/diagrama_tc.PNG" width="750" alt="Diagrama de Arquitetura">
</p>

### 2.4 Características Essenciais (Case)

- Seguindo passos desse projeto em: [passos de Configuração](#42-passos-de-configuração), deve-se ter um ambiente onde,
  - Metastore configurado para uso do catalogo e schemas
  - Contrato de dados para especificar regras de qualidade, padrões dos dados, TTL da informação.
  - Cluster dedicado para uso específico (criado de acordo com o custo do projeto)

## 3. Arquitetura Técnica

### 3.1 Visão Geral

A arquitetura técnica é baseada em uma infraestrutura provisionada via Terraform, com pipelines automatizados usando GitHub Actions, processamento em tempo real no Azure Databricks, e armazenamento seguro de dados no Azure Storage Account.

### 3.2 Sobre o projeto

Todo projeto inicia com uma ideia...

<p align="center">
  <img src="assets/img/esboco.png" width="900" alt="Diagrama de Arquitetura">
</p>

...que precisa ser organizada.

### 3.3 Ideação do Projeto

Este projeto foi idealizado para que os usuários tenham um ambiente mínimo para explorar dados. Três repositórios foram criados para que, a partir desse git template, seja possível ter um ambiente ponta a ponta. A ideação está organizada da seguinte forma:

<p align="center">
  <img src="assets/img/fluxo.png" width="900" alt="ideacao do projeto">
</p>

Ao Clonar repos template, o usuário deve setar as variaveis de ambiente necessário no git, configurar os arquivos .yaml e iniciar as execuções.
Na etapa de ingestão, o job executor fará download do pypi para uso do framework padrão da plataforma apresentada.

Repositório adicionais utilizados nesse projeto para experiência imersiva:

- [lealdouglas/strife](https://github.com/lealdouglas/strife), Setup de infraestrutura (recursos).
- [lealdouglas/jarvis](https://github.com/lealdouglas/jarvis), Delivery do pipeline de dados.
- [lealdouglas/carlton](https://github.com/lealdouglas/carlton), SDK comum padrão da plataforma de dados.

### 3.4 Descrição do Fluxo de Dados

- **Provisionamento de recursos**: O ambiente é provisionado via Terraform.
- **Configuração**: Definição do contrato de ingestão via .yaml.
- **Ingestão**: Dados são processados no Databricks e armazenados no Data Lake.
- **Processamento**: Exploração e processamento dos dados no Databricks.

### 3.4 Tecnologias Utilizadas

- **Terraform**: Para provisionamento de infraestrutura.
- **Azure Active Directory**: Para gestão de grupos e usuários.
- **Azure Event Hub**: Para captura de eventos.
- **Azure Storage Account**: Para armazenamento seguro.
- **Databricks**: Para processamento de dados em escala.
- **Databricks Unity Catalog**: Para gestão de grupos, catalogo, schemas e tabelas.
- **GitHub Actions**: Para automação CI/CD.
- **SDK in Pyspark**: SDK padrão para ingestao de dados.

### 3.5 Infraestrutura como Código

#### Provisionamento de Recursos (Terraform)

- **Scripts Terraform**: Utilizamos scripts Terraform para criar recursos como Event Hub, Databricks e Storage Account. Além disso, script é responsável por criar usuários e grupos no Azure Active Directory, sincroniza-los no unity catalog, configurar metastore e schemas baseados na arquitetura medalhão. Recursos criados via terraform nesse projeto,
  - **Event Hub**: Provisionado recurso para ingestões em evento.
  - **Unit Catalog**: Configuração de metastore, sincronização de usuários, configuração de schema e tabelas.
  - **Databricks**: Configurado com cluster single node, para uso de experimentação e baixo custo, proporcionando uma experiência imersiva.
  - **Storage Account**: Configurado para armazenar dados brutos (raw), ingeridos (bronze) e processados (silver).

### 3.6 Automações

#### Automação CI/CD (GitHub Actions)

- **Workflows**: O GitHub Actions é configurado para automatizar o deploy da infraestrutura e a execução de jobs no Databricks.
- **Build**: Executa scripts de criação de recursos.
- **Deploy**: Configura e executa jobs no Databricks.

### 3.6 Processamento de Dados

#### Ingestão de Dados (Event Hub)

- **Configuração**: O Event Hub captura eventos em tempo real, configurado com partitions para garantir alta disponibilidade.
  - **Consumers**: Configurados para alimentar o pipeline de dados no Databricks.

#### Processamento de Dados (Databricks)

- **Configuração de Clusters**: Clusters autoescaláveis configurados para otimizar o processamento de grandes volumes de dados.
- **Scripts de Ingestão e Processamento**: Utilizamos PySpark para ler dados, processá-los, e armazená-los no Data Lake.
  ```python
  # Exemplo de código PySpark
  spark.readStream.format('cloudFiles')
  .options(**autoloader_config)
  .load(config_ingest['carlton_file_path'])
  .select(
      '*',
      current_date().alias('carlton_current_date'),
      col('_metadata').alias('carlton_metadata'),
  )
  ```

### 3.7 Armazenamento de Dados

#### Data Lake (Storage Account)

- **Estrutura**: Dados organizados em camadas de bronze, silver e gold, seguindo a arquitetura de medalhão.
  - **Catalogo**: Catalogo de dados para suportar arquitetura medalhão.
  - **Raw**: landing arquivos.
  - **Bronze**: Dados brutos.
  - **Silver**: Dados processados.
  - **Gold**: Dados prontos para análise.

## 4. Instruções para Configuração e Execução do Projeto

### 4.1 Pré-requisitos

- Conta na Azure
- Subscrição Azure, preferência sem uso.
- Usuário de serviço (Service Principal), conforme [Step 2 - Configure usuário](https://github.com/lealdouglas/dougsll-datamaster?tab=readme-ov-file#step-2-configure-usu%C3%A1rio-de-servi%C3%A7o-service-principal) com as seguintes atribuições:
  - **Owner**, para criar e gerenciar recursos da azure.
  - **Global Administrator**, para sincronizar grupos e usuários do AAD no unity.
  - **Account Admin**, após provisionar ambiente [Step 5 - Setup Lakehouse](https://github.com/lealdouglas/dougsll-datamaster?tab=readme-ov-file#step-5-execute-a-action-strife-lakehouse), para configurar Unity Catalog.
- Definição das variaveis de ambiente:
  - **TF_ARM_TENANT_ID**, conta na azure (tenant)
  - **TF_ARM_SUBSCRIPTION_ID**, subscrição da conta
  - **TF_ARM_CLIENT_ID**, ID do usuário de serviço com permissão para criar recursos e grupos.
  - **TF_ARM_CLIENT_SECRET**, Secret do usuário de serviço com permissão para criar recursos e grupos no AAD.
  - **ADB_ACCOUNT_ID**, ID da console Unity Catalog do Databricks, saiba mais em [Step 6 - Recupere Account ID](https://github.com/lealdouglas/dougsll-datamaster?tab=readme-ov-file#step-6-recupere-account-id-do-unity-catalog-e-habilite-account-admin)

Utilize o tópico [Passos de Configuração](#42-passos-de-configuração) para dar sequência ao seu projeto.

### 4.2 Passos de Configuração

#### Step 1. Clone o repositório

```sh
git clone https://github.com/lealdouglas/dougsll-datamaster.git
cd dougsll-datamaster
```

#### Step 2. Configure usuário de serviço (Service Principal)

Crie um usuário de serviço na Azure (Service Principal) com as seguintes atribuições,

- **Owner**, para criar e gerenciar recursos da azure.
  Para configurar um usuário de serviço, você pode fazer via power shell ou via azure cli, após acessar o terminal, utilize o comando abaixo para criar o usuário:

  ```sh
  az login
  az ad sp create-for-rbac -n spndatamasteradmin --role Owner --scopes /subscriptions/<SUBSCRIPTION_ID>
  ```

  Onde, **SUBSCRIPTION_ID** é o ID da subscrição da sua conta Azure.

- **Global Administrator**, para sincronizar grupos e usuários do AAD no unity.
  Após criar usuário, acesse ao recurso da conta, Microsoft Entra ID, para incluir o usuário a permissão de Global Administrator,

  1 - selecione o recurso, diretorio padrao (active directory)
  2 - selecione no canto esquerdo, Roles and administrators
  3 - busque por "Global Administrator"
  4 - clique em Add assignments
  5 - busque pelo seu SPN
  6 - clique em add

<p align="center">
  <img src="assets/gif/globaladmin.gif" width="900" alt="ideacao do projeto">
</p> 
    
#### Step 3. Configure as secrets no GIT 
Configure as variaveis de ambiente (secrets) em seu repositório Git,
  Para configurar as variáveis, acesse: [Crie secrets para um repositório](https://docs.github.com/pt/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)  
  - **TF_ARM_TENANT_ID**, conta na azure (tenant)
  - **TF_ARM_SUBSCRIPTION_ID**, subscrição da conta
  - **TF_ARM_CLIENT_ID**, ID do usuário de serviço com permissão para criar recursos e grupos no AAD.
  - **TF_ARM_CLIENT_SECRET**, Secret do usuário de serviço com permissão para criar recursos e grupos no AAD.
  - **ADB_ACCOUNT_ID**, ID da console Unity Catalog do Databricks.
  
#### Step 4. Configure arquivo de Setup Infraestrutura Lakehouse
#### Step 5. Execute a action Strife Lakehouse
#### Step 6. Recupere Account ID do Unity Catalog e habilite Account Admin
#### Step 7. Execute a action Strife ADB Unity Catalog
#### Step 8. Configure arquivo de contrato para ingestão
#### Step 9. Execute a action Jarvis Ingestão
#### Step 10. Configure seu projeto para explorar dados
#### Step 11. Execute a action Jarvis Asset Bundles

## 5. Melhorias e Considerações Finais

### 5.1 Melhorias Futuras

Abaixo, compartilho algumas melhorias consideradas para essa solução e ambições de uma visão completa, considerando que o cenário desenvolvido é apenas um protótipo de uma necessidade maior:

#### Evolução da solução:

- UI e API Services, com serviços integrados e uma interface web configurada, as validações e etapas podem ser orquestradas a partir da interação do usuário com o formulário, onde, a partir das opções, um serviço pode ser acionado ou um repositório/actions pode ser configurado.
- Configurar um cluster para uso conforme etapas do pipeline.
- Escalabilidade: Melhorar o desempenho da ingestão de dados com particionamento de dados.
- Segurança: Implementar autenticação baseada em tokens para APIs de terceiros.
- Observabilidade: Adicionar métricas de performance e latência do pipeline.
- Banco de dados, Parâmetros recuperados via API para gerar uma imersão na experiência poderiam estar configurados em um banco de dados
- Implementar mecanimos de multiplas ingestões a partir do contrato.

#### Possíveis contribuições técnicas (melhorias):

- Montar .yaml para script terraform e incluir usuario principal (conta), para vincular aos grupos.
- Criar uma classe estruturada para o uso genérico do data contract, aplicando os padrões de SOLID.

### 5.2 Considerações Finais

Este projeto demonstra uma solução que representa o potencial em definir e configurar ambientes, além de preparar um pipeline de dados, sem exigir que o desenvolvedor (engenheiro de dados/ML) saia da plataforma de desenvolvimento (Git). Com todos os acessos e funcionalidades bem estabelecidos (Actions), a solução tem a capacidade e autonomia de servir toda a jornada do desenvolvedor. A solução também aborda uma visão em que, a partir de uma assinatura (exemplo do case domínio Drisk), é possível configurar pequenos projetos (Actions com a capacidade de criar resource groups, recursos unitários e cenários pré-moldados), com base na finalidade e nos ambientes desejados, onde a jornada começa desde o repositório. Por fim, uma camada de interface web e algumas APIs podem absorver validações e etapas que, via Git, podem parecer complicadas.

## 6. Custos do projeto

Esse projeto, executado de ponta a ponta, teve um custo de,

ESCREVER!

## 7. Referências

- [Terraform Documentation](https://www.terraform.io/docs/index.html)
- [Azure Databricks Documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Azure Event Hub Documentation](https://learn.microsoft.com/en-us/azure/event-hubs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Data Contract](https://datacontract.com/)
- [Medallion Architecture](https://www.databricks.com/br/glossary/medallion-architecture)
- [Creating secrets for a repository](https://docs.github.com/pt/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)
- [Create an Azure service principal with Azure CLI](https://learn.microsoft.com/en-us/cli/azure/azure-cli-sp-tutorial-1?tabs=bash)
