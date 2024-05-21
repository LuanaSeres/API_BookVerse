# API_BookVerse

# Biblioteca Pessoal API

## 1. Introdução

### Visão Geral do Projeto

O projeto visa desenvolver uma API para gerenciar uma biblioteca pessoal, permitindo que os usuários registrem os livros que possuem, avaliem os livros que já leram, marquem quais foram lidos e quais não foram, adicionem comentários sobre os livros e mantenham uma lista de desejos de livros que desejam comprar.

### Objetivos e Propósito do Sistema

- Facilitar o gerenciamento pessoal do acervo de livros dos usuários.
- Permitir que os usuários mantenham um registro de suas leituras e avaliações.
- Proporcionar um espaço para comentários e anotações sobre os livros.
- Permitir que os usuários criem e gerenciem uma lista de desejos de livros.

### Benefícios Esperados do Projeto

- Melhoria na organização pessoal dos livros dos usuários.
- Acompanhamento das leituras e avaliações de forma estruturada.
- Registro de comentários e opiniões pessoais sobre os livros.
- Organização das intenções de compra de novos livros.

## 2. Visão Geral do Sistema

### Descrição do Sistema

O sistema é uma API desenvolvida em Django Rest Framework para gerenciar uma biblioteca pessoal. Ele inclui funcionalidades para os usuários registrarem livros, avaliarem suas leituras, adicionarem comentários, marcarem status de leitura e gerenciarem uma lista de desejos de livros.

### Público-Alvo do Sistema

- Leitores que desejam gerenciar seus próprios acervos de livros.
- Usuários que querem manter um registro de suas leituras e avaliações.
- Pessoas interessadas em organizar seus desejos de compra de livros.

### Requisitos Funcionais e Não Funcionais

- **Funcionais**:
    - CRUD de livros na biblioteca pessoal.
    - Registro de avaliações e notas dos livros.
    - Marcação de livros como lidos ou não lidos.
    - Adição de comentários sobre os livros.
    - Gerenciamento de uma lista de desejos de livros.
- **Não Funcionais**:
    - Desempenho: Tempo de resposta rápido para consultas e operações.
    - Segurança: Proteção de dados sensíveis e autenticação segura.
    - Escalabilidade: Capacidade de lidar com um aumento no número de usuários e dados.

## 3. Arquitetura do Sistema

### Explicação da Arquitetura MVT (Model-View-Template)

- **Model**: Representa a estrutura dos dados e as regras de negócio.
- **View**: Lida com a lógica de apresentação e respostas às requisições.
- **Template**: Define a interface do usuário.

### Papel de Cada Componente

- **Model**: Define os modelos de dados como Livro, Usuário, Avaliação, Comentário e Lista de Desejos.
- **View**: Implementa as APIs RESTful para manipular os dados.
- **Template**: Usado para renderizar páginas HTML.

### Uso do Padrão Repository para Acesso a Dados

- Separação das operações de acesso a dados em repositórios dedicados.
- Facilidade de manutenção e testes unitários.

## 4. Requisitos Funcionais

### Lista Detalhada de Funcionalidades do Sistema

1. Cadastro de livros na biblioteca pessoal.
2. Atualização e exclusão de registros de livros.
3. Registro e edição de avaliações e notas dos livros.
4. Marcação de status de leitura (lido/não lido).
5. Adição e edição de comentários sobre os livros.
6. Gerenciamento de uma lista de desejos de livros.

### Casos de Uso Principais

1. Usuário registra um novo livro na sua biblioteca pessoal.
2. Usuário avalia e dá nota a um livro lido.
3. Usuário marca um livro como lido.
4. Usuário adiciona um comentário sobre um livro.
5. Usuário adiciona um livro à sua lista de desejos.

### Fluxos de Trabalho do Usuário

1. **Cadastro e Login**:
    - Usuário se cadastra e faz login.
2. **Registro e Avaliação de Livros**:
    - Usuário registra um livro.
    - Usuário avalia e comenta sobre o livro.
3. **Marcação de Status de Leitura**:
    - Usuário marca um livro como lido ou não lido.
4. **Gerenciamento de Lista de Desejos**:
    - Usuário adiciona livros à lista de desejos.

## 5. Requisitos Não Funcionais

### Desempenho Esperado do Sistema

- Tempo de resposta para consultas e operações CRUD deve ser inferior a 2 segundos.

### Segurança e Autenticação

- Uso de JWT para autenticação.
- Criptografia de dados sensíveis.
- Controles de acesso baseados em permissões.

### Escalabilidade e Manutenibilidade

- Arquitetura modular para facilitar a escalabilidade.
- Boas práticas de codificação para facilitar a manutenção.

## 6. Tecnologias Utilizadas

### Linguagens de Programação

- Python

### Frameworks

- Django Rest Framework

### Bancos de Dados

- SQLite

### Ferramentas de Desenvolvimento

- Git para controle de versão.

## 7. Modelo de Dados

### Estrutura do Banco de Dados

- Tabelas: Livro, Usuário, Avaliação, Comentário, Lista de Desejos.

### Relacionamentos entre Entidades

- Um Usuário pode ter vários Livros.
- Um Usuário pode fazer várias Avaliações.
- Um Livro pode ter vários Comentários.
- Um Usuário pode ter vários itens na sua Lista de Desejos.

### Esquema de Armazenamento

- Banco de dados relacional SQLite.

## 8. Interfaces do Usuário

### Layout e Design das Interfaces

- Não aplicável diretamente à API, mas endpoints devem ser intuitivos e bem documentados.

### Funcionalidades Específicas de Cada Tela

- Implementado em clientes que consumirem a API.

### Fluxos de Interação do Usuário

- A ser implementado por clientes que utilizarem a API.

## 9. Arquitetura de Implementação

### Organização do Código-Fonte

- Separação por módulos: modelos, views, repositórios, serializers, templates.

### Divisão em Módulos e Componentes

- Módulos: users, books, reviews, comments, wishlist.

### Dependências entre os Componentes

- Views dependem de repositórios e modelos.
- Serializers dependem de modelos.

## 10. Gestão de Configuração e Controle de Versão

### Políticas de Controle de Versão

- Uso de Git com branches para desenvolvimento, staging e produção.

### Ramificação do Código-Fonte

- Branch principal: `main`
- Branch de desenvolvimento: `develop`
- Branches de feature e hotfixes: `feature/*`, `hotfix/*`

### Uso de Ferramentas de Controle de Versão

- Git com repositório no GitHub.

## 11. Gestão de Projetos

### Cronograma de Desenvolvimento

- **Dia 1**: Configuração do ambiente de desenvolvimento e planejamento detalhado.
- **Dia 2**: Desenvolvimento de modelos e configuração do banco de dados.
- **Dia 3**: Criação dos repositórios e configuração das rotas básicas.
- **Dia 4**: Desenvolvimento de views para CRUD de livros.
- **Dia 5**: Desenvolvimento de views para avaliações e comentários.
- **Dia 6**: Implementação de autenticação e autorização de usuários.
- **Dia 7**: Implementação das funcionalidades de lista de desejos.
- **Dia 8**: Testes iniciais e validação das funcionalidades principais.
- **Dia 9**: Implementação de melhorias e correções de bugs encontrados nos testes.
- **Dia 10**: Testes de segurança e desempenho.
- **Dia 11**: Documentação da API e preparação para o lançamento.
- **Dia 12**: Revisão final e lançamento da API.

### Atribuição de Tarefas e Responsabilidades

- Tarefas divididas entre desenvolvimento de backend, testes e documentação.

### Monitoramento do Progresso do Projeto

- Uso de ferramentas como Trello para acompanhar tarefas e progresso.

## 12. Considerações de Manutenção

### Planos de Suporte Pós-Implantação

- Suporte contínuo para resolução de problemas e bugs.

### Processo de Correção de Bugs e Implementação de Melhorias

- Sistema de tickets para rastreamento de bugs e solicitações de melhorias.

### Atualizações de Segurança e de Software

- Monitoramento regular para aplicar atualizações de segurança e software.
