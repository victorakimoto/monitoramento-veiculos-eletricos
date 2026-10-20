
PROJETO UPX III: SISTEMA DE MONITORAMENTO E COMPARAÇÃO DE VEÍCULOS ELÉTRICOS


1.	REVISÃO DO MVP VALIDADO
1.1	Contexto e Problema Validado

O mercado de veículos elétricos (VE) cresce aceleradamente, gerando novas demandas para motoristas particulares e gestores de pequenas frotas urbanas. Durante a fase de validação com as personas, identificou-se uma dor central: a assimetria de informações sobre a autonomia real e a dificuldade de comparar o custo-benefício dos modelos disponíveis no mercado nacional. Os dados de fábrica frequentemente divergem da realidade das vias urbanas brasileiras (uso de ar-condicionado constante, relevo e trânsito pesado), gerando a chamada "ansiedade de autonomia" (range anxiety) e dificultando o planejamento financeiro de transição para a frota elétrica.
1.2	Público-Alvo e Personas

●	Persona 1 (Motorista Particular): Proprietário recente ou entusiasta que deseja monitorar se o seu veículo entrega a autonomia prometida e entender seus custos reais por quilômetro rodado (km/kWh).
●	Persona 2 (Uber ou taxista): Profissional responsável por usar veículos urbanos que precisa comparar dados de eficiência entre diferentes modelos para decidir quais novas unidades comprar para seu uso profissional, visando menos gastos e mais lucros.
1.3	Solução Proposta e Aprendizados da Validação

A solução consiste em uma plataforma web simplificada e focada em dados práticos. Na etapa de validação conceitual, o público entrevistado demonstrou desinteresse por sistemas visualmente complexos ou cheios de recursos secundários. O aprendizado chave foi: o usuário quer simplicidade. Ele precisa apenas cadastrar seu carro, registrar dados de uso de forma rápida e visualizar 
um comparativo direto e gráfico de desempenho. Portanto, o escopo foi reduzido para 3 funcionalidades essenciais, garantindo alta usabilidade e viabilidade de execução técnica pela equipe de 3 integrantes ao longo do semestre.


2.	DEFINIÇÃO DAS FUNCIONALIDADES DO SISTEMA

ID	Nome	da Funcionalidade	Descrição Objetiva	Valor Entregue ao Usuário	Prioridade
F01	Autenticação e Cadastro de Veículos	Módulo para criação de conta do usuário e registro técnico dos	seus veículos (Marca, Modelo, Ano e Capacidade da Bateria em kWh).	Garante	um ambiente seguro, privado e personalizado para		o
armazenamento dos dados de interesse do usuário.	Alta	(Core	do Sistema)
F02	Módulo	de Monitoramento (CRUD)	Interface	para lançamento, edição		e
exclusão		de registros de uso diário (Quilometragem rodada e Nível da	Bateria restante em %).	Transforma dados brutos em histórico		de consumo	real, calculando			a eficiência média do veículo nas ruas.	Alta	(Core	do Sistema)
 

F03	Comparador de Modelos (Dashboard)	Painel	visual contendo gráficos		que
cruzam	e
comparam			o desempenho (km/kWh)		de dois	ou	mais veículos cadastrados.	Facilita	a
tomada	de
decisão    de
compra	ou substituição de frota de forma 100% analítica e visual.	Média
(Complementar)


3.	ESTRUTURAÇÃO DO BACKLOG (TRELLO)


Link do Quadro do Trello:

https://trello.com/b/JZqQ37Bp

Abaixo estão detalhados os principais cartões cadastrados e distribuídos no Backlog da ferramenta, respeitando o limite normativo de no máximo dois integrantes responsáveis:


Card 1: [F01] Modelagem de Dados e Cadastro de Veículos

●	Descrição: Criar a estrutura do banco de dados (tabelas de usuários e veículos) e desenvolver a tela do formulário frontend para registrar os dados técnicos dos automóveis.
●	Responsáveis: Aluno Willas Cavalheiro

●	Critério de Conclusão (Definition of Done): Dados preenchidos no formulário frontend sendo enviados com sucesso, salvos na tabela correspondente do banco de dados e associados ao ID do usuário autenticado.
Card 2: [F02] Lançamento e Histórico de Consumo (CRUD) 
●	Descrição: Desenvolver o endpoint backend para receber os lançamentos de km e bateria, criar a tela de formulário de uso no frontend e estruturar a tabela que lista o histórico permitindo edição/exclusão.
●	Responsáveis: Kaike Rafael Figueiredo

●	Critério de Conclusão (Definition of Done): Histórico de lançamentos renderizado em tela. Operações de atualizar registros e deletar funcionando sem erros de banco e atualizando a interface em tempo real.
Card 3: [F03] Interface e Motor do Comparador Gráfico

●	Descrição: Desenvolver as funções matemáticas no backend para calcular a média de consumo geral dos carros cadastrados e criar os componentes de gráficos visuais na interface frontend para comparação paralela.
●	Responsáveis: Victor Akimoto

●	Critério de Conclusão (Definition of Done): Gráficos exibindo corretamente a diferença de eficiência (km/kWh) entre os carros selecionados na tela, utilizando dados reais extraídos do histórico.


4.	PLANEJAMENTO DAS SPRINTS
O projeto está estruturado em 4 Sprints quinzenais (2 semanas cada), totalizando 8 semanas de desenvolvimento focado e realista.
Sprint 1: Setup, Arquitetura e Design Base

●	Período: 14/09/2026 a 27/09/2026

●	Objetivo da Sprint: Estabelecer a infraestrutura de código funcional e a identidade visual das telas do sistema de veículos elétricos.
●	Lista de Tarefas e Responsáveis:

1.	Criação do repositório no GitHub, setup inicial da API Backend e banco de dados (Aluno 1). 
2.	Desenho do protótipo de alta fidelidade e UI/UX de todas as telas no Figma (Aluno 2).
3.	Criação da estrutura base do projeto Frontend e documentação inicial do repositório (Aluno 3).
Sprint 2: Desenvolvimento da Autenticação e Cadastro (F01)

●	Período: 28/09/2026 a 11/10/2026

●	Objetivo da Sprint: Entregar a camada de segurança e a capacidade de armazenar veículos na plataforma.
●	Lista de Tarefas e Responsáveis:

1.	Desenvolvimento dos endpoints de registro, login e validação de segurança via JWT no Backend (Aluno 1).
2.	Construção das telas de Login, Cadastro de Usuário e Cadastro de Veículo no Frontend (Aluno 2 e Aluno 3).
3.	Escrita dos planos de teste funcionais e validação das regras de negócio de entrada de dados (Aluno 1 e Aluno 2).
Sprint 3: Desenvolvimento do Módulo de Monitoramento (F02)

●	Período: 12/10/2026 a 25/10/2026

●	Objetivo da Sprint: Consolidar o núcleo operacional do sistema (inserção e listagem de dados de autonomia).
●	Lista de Tarefas e Responsáveis:

1.	Construção das rotas de CRUD de telemetria e cálculos de autonomia no Backend (Aluno 1).
2.	Construção das telas de listagem de histórico e modais de inserção/edição de dados no Frontend (Aluno 2 e Aluno 3).
3.	Execução de testes de integração backend/frontend e escrita do relatório parcial de progresso (Aluno 1 e Aluno 3). 
o ★ Marco da Sprint: MVP Funcional atingido (Usuário já consegue monitorar dados básicos de uso).
Sprint 4: Painel Comparador (F03), Homologação e Fechamento

●	Período: 26/10/2026 a 08/11/2026

●	Objetivo da Sprint: Finalizar o valor analítico do sistema com gráficos comparativos e garantir estabilidade total para a entrega final.
●	Lista de Tarefas e Responsáveis:

1.	Desenvolvimento das queries de agrupamento e lógica de cruzamento de dados de desempenho automotivo por modelo (Aluno 1 e Aluno 2).
2.	Integração de biblioteca gráfica (ex: Chart.js / Recharts) no Frontend para exibir o comparador de modelos (Aluno 3).
3.	Testes de estresse ponta a ponta (End-to-End), correção de bugs e compilação do relatório final em PDF (Aluno 2 e Aluno 3).


5.	DISTRIBUIÇÃO DE PAPÉIS E RESPONSABILIDADES
Para garantir o equilíbrio técnico com uma equipe enxuta de 3 pessoas, os papéis foram distribuídos unindo frentes correlatas:

Nome do Aluno	Função Principal	Participação nas Sprints	Principais Responsabilidades no Projeto
Aluno 1	Desenvolvedor Backend & QA	Sprints 1, 2, 3
e 4	Modelagem do banco de dados, desenvolvimento da API REST, segurança (JWT) e testes automatizados de rotas.
 

Aluno 2	Desenvolvedor Frontend & UI/UX	Sprints 1, 2, 3
e 4	Criação do design interativo no Figma, estilização responsiva do sistema, criação de componentes frontend e consumo da API.
Aluno 3	Desenvolvedor Frontend	& Gestor (PO)	Sprints 1, 2, 3
e 4	Arquitetura do projeto Frontend, integração de gráficos do Dashboard, organização do Trello e redação técnica do relatório PDF.


6.	CRONOGRAMA GERAL DO PROJETO
O cronograma visual abaixo sintetiza os marcos de evolução física do software ao longo do período letivo:

Período (Quinzenal)	Fase Ativa	Entregas Previstas	Marcos Importantes / Milestones
Semanas 1 e
2	Sprint 1	Repositório no GitHub configurado; Protótipo no Figma finalizado.	Homologação do design visual do sistema.
Semanas 3 e
4	Sprint 2	Módulo de Login e Cadastro de veículos operacionais no sistema.	Estabilização	da segurança de dados da plataforma.
Semanas 5 e
6	Sprint 3	Módulo de inserção de quilometragem e bateria ativo com persistência.	★	Marco:	MVP Funcional Atendido.
 

Semanas 7 e
8	Sprint 4	Gráficos	integrados comparando os veículos; Testes gerais concluídos.	Entrega	Final: Sistema homologado e pronto.


7.	CRITÉRIOS DE AVALIAÇÃO DO PROJETO


Para fins de validação da banca e professores ao término do semestre, o grupo estabelece como critérios formais de sucesso e entrega válida:
●	O que constitui uma entrega válida: Uma aplicação web ou mobile executável, com interface gráfica funcional, conectada a um banco de dados relacional ou não-relacional que comprove a persistência real dos dados inseridos.
●	Funcionalidades obrigatórias de apresentação:

1.	Efetuar login seguro com usuário cadastrado.

2.	Adicionar um carro elétrico e registrar pelo menos 3 lançamentos de consumo fictícios em seu histórico.
3.	Abrir a tela do comparador e visualizar graficamente a diferença de km/kWh do carro cadastrado em relação a outro modelo base.
●	Evidências materiais a serem apresentadas:

1.	Link do repositório público no GitHub com histórico de commits distribuído de forma justa entre os desenvolvedores.
2.	Quadro do Trello com histórico completo de cartões movidos para a coluna "Concluído (Done)".
3.	Vídeo de demonstração técnica (Screencast) com duração máxima de 3 minutos navegando pelas 3 funcionalidades sem interrupções ou falhas críticas. 
 

CONCLUSÃO E POSSÍVEIS PASSOS FUTUROS
O desenvolvimento do Sistema de Monitoramento e Comparação de Veículos Elétricos tem como objetivo transformar dados de uso dos veículos em informações simples e úteis para auxiliar motoristas e profissionais na compreensão do consumo, da autonomia e do custo-benefício dos veículos elétricos. A partir da validação do MVP, foi identificado que a simplicidade e a facilidade de acesso às informações são fatores importantes para os usuários, direcionando o projeto para uma solução objetiva e funcional.
Como próximos passos, após a conclusão das funcionalidades previstas no MVP, o sistema poderá evoluir com a ampliação da base de modelos de veículos elétricos, permitindo comparações entre uma quantidade maior de automóveis disponíveis no mercado. Também poderá ser implementado um sistema de acompanhamento mais detalhado do consumo, possibilitando visualizar a evolução da eficiência do veículo ao longo do tempo.
Outra possibilidade de evolução é a integração com dados reais de veículos, sensores ou sistemas de telemetria, reduzindo a necessidade de inserção manual das informações. O sistema também poderá incorporar dados sobre preços de energia elétrica, custos de recarga e distância percorrida, permitindo estimativas mais precisas do custo por quilômetro.
No futuro, também poderão ser desenvolvidos recursos como estimativa de autonomia em diferentes condições de uso, histórico de desempenho, notificações e recomendações personalizadas, além de uma versão mobile para facilitar o acesso durante a utilização do veículo.
Dessa forma, o MVP representa uma primeira etapa para validar e estruturar a solução. A evolução gradual das funcionalidades, baseada no feedback dos usuários e na análise dos dados coletados, poderá transformar o sistema em uma ferramenta mais completa para monitoramento, comparação e apoio à decisão relacionada aos veículos elétricos.


https://www.figma.com/make/ZyrYwSWshjrUoxgRIjHM7A/Plataforma-de-Monitoramento-de-Carros?fullscreen=1&t=pwNQm5D5CETD8Q0Y-1&code-node-id=0-6
https://docs.google.com/spreadsheets/d/1Fh7_vUREGRxASqc-BtUVJKm6SNao0UL_BywsVPsrBQo/edit?usp=sharing
https://trello.com/b/JZqQ37Bp/ev-monitor
