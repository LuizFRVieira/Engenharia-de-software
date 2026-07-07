# Atividade — Sistema de Agendamento de Visitas Técnicas

**Conversa de referência:** https://claude.ai/share/c0885afb-f333-43fd-9ab7-411f45f57584

---

## Tarefa 1.1

Um sistema de geração de ticket de agendamentos de visitas técnicas.

Resolver o problema de desorganização na hora de marcar as visitas e a falta de armazenamento do que foi feito nas visitas.

Os funcionários da empresa, os quais marcam as visitas, e os técnicos que realizam as visitas.

O sistema é relevante visto que é preciso ter uma organização das datas e horários bem encaixados para cada cliente, além de armazenar o histórico do que foi feito nas visitas para melhor controle de cada visita.

---

## Tarefa 1.2 — Planejamento de Entrevista

**Objetivo da entrevista:** Entender os problemas e necessidades dos funcionários que podem ser resolvidos com o sistema.

**Perguntas:**

1. Como funciona hoje o processo desde o momento em que surge a necessidade de uma visita técnica até ela ser de fato realizada? Me conta esse caminho todo.
2. Quais são as maiores dificuldades que você enfrenta no dia a dia referente a esse problema?
3. Já ocorreu alguma situação que gerou problema por causa dessa falta de organização e falta de histórico de dados?
4. Você usa alguma ferramenta para o agendamento, ou ele é feito no papel/quadro de avisos físico?
5. Como é feita a escolha da equipe de técnicos que vão ao local? Quais são os critérios?
6. As ferramentas que você usa estão dando conta do fluxo de demanda?
7. Quando uma visita está agendada, como você fica sabendo as informações do serviço (se foi resolvido ou não, se vai ter que voltar outro dia, o que foi feito etc.)?
8. Se você pudesse mudar algo no jeito que vocês agendam as visitas hoje, o que você mudaria?

**Minha reflexão:** Escolhi essas perguntas visto que elas foram bem parecidas com as perguntas que eu fiz para esse projeto, que é um projeto real que estou fazendo no meu estágio.

---

## Tarefa 1.3 — Histórias de Usuário

**História 1 — Atendente**

Como **atendente**, quero **registrar agendamentos em um sistema centralizado** para **não depender do WhatsApp e evitar perda de informações**.

- O sistema permite cadastrar cliente, endereço e tipo de visita
- Todos os envolvidos visualizam os agendamentos em tempo real
- Não é possível cadastrar visitas conflitantes para o mesmo técnico

**Prioridade: Alta** — Base de tudo que o sistema precisa resolver.

---

**História 2 — Técnico de Campo**

Como **técnico de campo**, quero **receber os agendamentos com antecedência e histórico do cliente** para **chegar na visita preparado**.

- O técnico recebe data, endereço e tipo de serviço com antecedência
- O sistema exibe o histórico de visitas anteriores do cliente
- É possível identificar se o serviço é urgente

**Prioridade: Alta** — Sem isso o técnico chega sem contexto, gerando retrabalho.

---

**História 3 — Supervisor**

Como **supervisor**, quero **que o status das visitas atualize automaticamente** para **não depender de mensagem do técnico para saber o que foi feito**.

- O técnico marca a visita como concluída, reagendada ou com pendência
- O status atualiza em tempo real para o supervisor
- Elimina o controle manual em planilha

**Prioridade: Alta** — Resolve o maior gargalo da operação hoje.

---

**História 4 — Técnico de Campo**

Como **técnico de campo**, quero **ver minha agenda da semana completa** para **me organizar e não receber visitas de última hora**.

- O técnico visualiza todos os agendamentos da semana em uma tela
- As visitas aparecem com data, horário e tipo de serviço
- O sistema bloqueia atribuições para técnicos sem disponibilidade

**Prioridade: Média** — Melhora a organização, mas não trava o sistema sem ela.

---

**História 5 — Atendente**

Como **atendente**, quero **acompanhar o status das visitas em tempo real** para **responder o cliente sem depender de ninguém**.

- O sistema mostra o status de cada visita por cliente
- O atendente busca visitas por nome ou contato do cliente
- Cancelamentos e reagendamentos notificam o atendente automaticamente

**Prioridade: Média** — Depende das histórias anteriores funcionando primeiro.

**Minha reflexão:** Sobre a resposta da pergunta anterior, pedi para gerar as respostas de cada pergunta. Com isso, analisei todas as respostas e fiz uma lista dos pontos principais de cada uma, e assim gerou a história de usuário de cada perfil.

---

## Tarefa 1.4 — Verificação de Completude e Consistência

**H3 — Supervisor**

- "O técnico marca a visita como concluída, reagendada ou com pendência" — só o técnico pode alterar o status ou o supervisor também consegue?
- Se o técnico marcar errado, tem como corrigir? Quem pode corrigir?
- "Elimina o controle manual em planilha" — isso não é um critério de aceitação, é uma consequência. Não dá para testar isso.

**H5 — Atendente**

- "O sistema mostra o status de cada visita por cliente" — quais são esses status? São os mesmos que o técnico define na H3?
- "Busca visitas por nome ou contato do cliente" — o que aparece se não encontrar nenhum resultado?

**Revisão crítica:** Para reduzir pela metade, eu removeria a História 4 e a História 5. A História 4 seria algo adicionado a mais para uma melhor organização do técnico, não necessariamente algo de extrema importância para o sistema. A História 5, porque é algo mais para o atendente ter uma base do que está sendo feito. Porém, se existem as pontas de quando vai ser feito e o que foi feito, não é necessário que ela saiba o que está ocorrendo no sistema.
