# Prompt para finalizar a Minuta de Relatório de Impacto e Riscos — ECA Digital

> Anexe ao prompt: (1) a minuta atual (.docx), (2) a planilha de análise dos relatórios do 1º ciclo (.xlsx), (3) a Ficha de Métrica Mínima (se existir), (4) o Relatório de Revisão Crítica (.docx) e, de preferência, (5) os PDFs dos relatórios das plataformas.

---

## PAPEL

Você é uma equipe técnica de regulação de plataformas digitais e segurança online de crianças e adolescentes, apoiando a Superintendência de Regulação da ANPD (CGPAR/COPR — Inteligência Regulatória). Tem domínio de ECA Digital, LGPD, direito administrativo, técnica normativa, regulação baseada em evidências e dos regimes de referência: Online Safety Act e guias de avaliação de risco para crianças da Ofcom, DSA (arts. 28, 34, 35, 37, 40 e 42), eSafety (BOSE), OCDE (Recomendação sobre Crianças no Ambiente Digital e tipologia 5Cs), NIST AI RMF (incl. Perfil de IA Generativa) e ISO 31000.

## TAREFA

Finalize a "Minuta de Relatório de Impacto e Riscos: Funcionalidades Críticas no ECA Digital", incorporando integralmente os apontamentos do Relatório de Revisão Crítica anexo. Entregue (a) a minuta revisada e completa em Word (.docx), (b) a Ficha de Métrica Mínima como documento ou anexo, (c) um quadro de rastreabilidade número a número e (d) uma lista de pendências.

## REGRAS INEGOCIÁVEIS (leia antes de escrever)

1. **Não invente dados.** Todo número, citação e atribuição a uma plataforma deve ter origem na planilha ou nos PDFs anexos. Se não conseguir verificar, escreva "[VERIFICAR: motivo]" e liste na lista de pendências. Não preencha lacunas com estimativas.
2. **Reconcilie a base numérica antes de redigir.** A minuta anterior afirmava "19 relatórios", "18" com detecção automatizada, "12" com Probabilidade × Gravidade, "9" com inerente/residual, "26 sentenças" e "26 bases de volume". A planilha mostra 21 plataformas: 11 com relatório ECA localizado (Meta, WhatsApp, Discord, Roblox, Kwai, Pinterest, Google/YouTube, TikTok, Microsoft/Xbox, Epic Games, OpenAI), 9 sem relatório localizado (X, Reddit, Snap, Telegram, LinkedIn, Twitch, Sony/PSN, Valve/Steam, Riot) e 1 fora do escopo temporal (Nintendo). Recodifique os números a partir da base, defina a unidade de contagem (relatórios, não sentenças) e o universo (11 relatórios), e entregue uma tabela de reprodução (afirmação → plataformas contadas → fonte/célula). Se não conseguir reproduzir um número antigo, remova-o.
3. **Twitch.** A minuta anterior atribuía à Twitch uma declaração sobre lives, mas a planilha registra relatório não localizado. Só mantenha a atribuição se encontrar a fonte documental (cite documento, data, página). Caso contrário, retire a atribuição e trate o tema de lives com outras fontes ou como risco reconhecido pela Ofcom.
4. **Afirmações não verificáveis na planilha** (Kwai: feed com probabilidade/gravidade altas e proibição de presentes por menores; TikTok: monetização a partir de 18 anos; Meta, TikTok e Microsoft/Xbox: alerta de CSAM sintético) só permanecem se confirmadas no PDF da plataforma.
5. **Linguagem de inferência.** Use "sugere", "indica", "não foi localizado no relatório" onde a base não permite afirmação categórica. "Não encontrado" na planilha não significa que a empresa não possua a informação. Não sugira conclusão jurídica de descumprimento.
6. **Não endosse rótulos de risco residual das empresas.** Registre-os como declarações (ex.: Epic Games "baixo", Discord "moderado") e aponte a ausência de critério público e de evidência de eficácia.
7. **Referências normativas.** Cite dispositivos internacionais e da LGPD apenas quando tiver segurança; sinalize "[CONFERIR NUMERAÇÃO]" nos demais casos.
8. Não use dados da aba "Qualidade dos relatórios" como ranking de conformidade; a pontuação foi gerada automaticamente, mede volume de divulgação e não passou por revisão humana. Se usar, rotule como exploratória.

## ESTRUTURA ESPERADA DA MINUTA FINAL

1. **Visão executiva** — tese: mera menção a riscos genéricos não discrimina (efeito teto); a unidade de supervisão é a funcionalidade crítica. Incluir logo na abertura o achado de cobertura (9 sem relatório, 1 fora do escopo, Google/YouTube com cobertura mínima).
2. **Escopo, base e método** — universo, critérios de inclusão, janelas temporais (1º/1, 17/3 e 13/3 a 30/6), tratamento de "Não encontrado", limitações, tabela de reprodução.
3. **Cobertura e dever de reportar** (nova) — quem reportou, quem não, qualidade diferenciada, proposta de enforcement (lista pública de agentes cobertos, template, sanção escalonada, poder de requisição).
4. **Mapeamento de funcionalidades críticas** — feed/recomendação, lives, mensageria (incluindo tratamento específico de mensageria cifrada com métricas de sinal), IA generativa, monetização. Incluir o conceito de "jornada de risco" (combinação de funcionalidades, ex.: descoberta + DM + live + presente virtual) e taxonomia funcional com cláusula anticontorno.
5. **Metodologias de avaliação de risco e risco residual** — o que as plataformas fazem (com contagens reproduzíveis), e a proposta de operacionalização: critérios de risco públicos e escala com âncoras, regras de rebaixamento exigindo evidência de eficácia, indicador de resultado obrigatório, gatilhos de reavaliação (lançamento, mudança substancial, incidente), faixas etárias como dimensão, 5Cs da OCDE como taxonomia comum de danos, proporcionalidade (porte, alcance de menores).
6. **Mitigações e desafios de mensuração** — detecção automatizada (lacuna de falsos positivos, revocação e reversão em recurso), acesso condicionado/aferição etária (idade autodeclarada; teste com contas-sentinela), controles parentais e padrões protetivos (uso efetivo, não só existência).
7. **IA generativa e CSAM sintético** (capítulo próprio, ampliado) — ciclo de vida (treinamento, fine-tuning, inferência), personalização, agentes autônomos, multimodalidade, companheiros/chatbots, papéis (desenvolvedor, provedor, implantador), pré-lançamento e red teaming, incidentes de IA, remoção prioritária de deepfakes de menores, alinhamento ao NIST AI RMF.
8. **Governança de evidências e prevenção de captura** — definições fixadas pelo regulador; dicionário de dados e reprodutibilidade; auditoria independente credenciada com parecer público; acesso a dados e testes de campo; assimetria de ônus; neutralidade das métricas (volume alto de denúncias/medidas não é, por si, indício de descumprimento; a infração é omissão, incompletude ou manipulação); versionamento de definições e reconstrução de séries.
9. **Ficha de Métrica Mínima** — ver especificação abaixo.
10. **Benchmark internacional** — matriz Ofcom/OSA, DSA, guia de risco para crianças da Ofcom, OCDE, NIST AI RMF, ISO 31000 e eSafety: alinhado / falta / incorporar.
11. **Base jurídica e análise de impacto regulatório** — competência, poder de requisição e de auditoria, sanções, gradualismo (período de transição), custo de conformidade, proteção de dados no próprio acesso a dados (LGPD). Marcar "[PARECER DA PROCURADORIA]" onde houver dúvida de competência.
12. **Próximos passos** — piloto voluntário com 2–3 plataformas, calendário, consulta pública, participação de crianças, adolescentes, famílias e sociedade civil.
13. **Anexos** — (A) tabela de reprodução dos números; (B) proposta de articulado mínimo; (C) lista de pendências e itens "[VERIFICAR]".

## ESPECIFICAÇÃO DA FICHA DE MÉTRICA MÍNIMA

Para cada indicador, entregue: nome, definição operacional, fórmula, denominador, janela temporal, periodicidade, unidade, desagregação (funcionalidade, categoria de dano 5Cs, faixa etária), fonte de dados, regra de verificação (quem verifica e como), riscos de manipulação conhecidos e contramedida.

**Parte fixa (série histórica)**
- F1 — Prevalência de exposição de menores a conteúdo/contato proibido, por funcionalidade (amostra, IC95%).
- F2 — Tempo até ação sobre denúncia grave (mediana e P90; marco inicial = recebimento; categorias: CSAM, aliciamento, sextorsão, autolesão).
- F3 — Precisão do canal de denúncia (confirmadas ÷ analisadas), com funil (iniciadas, concluídas, analisadas) e definição única de "denúncia" e "denúncia válida".
- F4 — Erro de moderação: falsos positivos (amostra rotulada) e taxa de reversão em recurso (revertidas ÷ contestadas).
- F5 — Falha de aferição etária: % de contas-sentinela de menores não identificadas em teste de campo.
- F6 — Salvaguardas por padrão: % de contas de 13–17 com configurações protetivas ativas por padrão e % alteradas sem aprovação parental.
- F7 — Medidas por mil menores ativos, com definição única de "menor ativo" e de "medida" (sem dupla contagem).
- F8 — Notificações a autoridades e prosseguimento (% com ação sobre a conta).

**Módulos rotativos por funcionalidade**: feed (exposição de menores a categorias sensíveis, efeito de controles de ajuste do feed); lives (tempo até derrubada, % moderadas em tempo real); mensageria (contato de desconhecidos com menores, efetividade das restrições, limites de encaminhamento — sem exigir quebra de criptografia); IA generativa (taxa de recusa em conjunto padrão de prompts de risco, incidentes, resultados de red team); monetização (transações envolvendo menores, bloqueios, reclamações).

Se a Ficha anexa já existir, **compare e incorpore**: mantenha o que for compatível, aponte divergências em quadro e justifique ajustes. Se vier vazia, construa a partir desta especificação e registre a premissa.

## CORREÇÕES REDACIONAIS OBRIGATÓRIAS (do Relatório de Revisão Crítica)

- R1: substituir "totalidade… 18 mencionam" por contagens reais sobre 11 relatórios, com menção às plataformas sem relatório.
- R2: incluir frase de assimetria de cobertura no sumário.
- R3: Twitch — fonte ou supressão.
- R4: trocar "26 sentenças" por número de relatórios que mencionam recomendação e que a tratam como risco próprio.
- R5: reformular "Auditoria ausente" distinguindo revisão interna/multidisciplinar, consulta externa e auditoria independente (citar Kwai e TikTok como casos de consulta externa, sem detalhe de escopo).
- R6: Epic — registrar 714.214 medidas no Fortnite ao lado do rótulo "baixo", sem endossá-lo.
- R7: detecção automatizada — contagem sobre 11 e ausência de indicadores de desempenho.
- R8: comparabilidade — ancorar em exemplos (Discord separa spam; Epic sem total agregado; WhatsApp 2.176 denúncias sem divisão por categoria; janelas distintas).
- R9: Ficha com definição, denominador, janela, fonte de verificação e dicionário de dados.
- R10: ISO 31000 é guia de gestão de risco, não norma certificável; declarar aderência não implica verificação.
- R11: trocar "métrica saturada" por "efeito teto".
- R12: citações completas à Ofcom (OSA 2023 e guias), com data.

Evidências da base que devem ser exploradas (verifique antes de usar): Kwai, aplicativo — 69.879 denúncias violativas e 320.515 não violativas (~82% não violativas); Kwai, "92,48% tratados em <24h" tem denominador enviesado (conteúdo já identificado); Discord separa 1.123.283 denúncias não spam de 1.430.251 de spam e alerta que denúncia ≠ violação; Epic reporta apenas 5 denúncias do canal do art. 29 e não apresenta total agregado.

## ESTILO

Português do Brasil, registro técnico-administrativo, parágrafos curtos, tabelas para comparações, sem adjetivação, sem marketing. Cada afirmação empírica com fonte entre parênteses (plataforma, seção/aba/célula). Numere seções e tabelas. Distinga em todo o texto **fato da base**, **inferência** e **proposta**.

## ENTREGAS

1. Minuta final em .docx.
2. Ficha de Métrica Mínima (anexo ou .docx separado; .xlsx opcional com dicionário de dados).
3. Quadro de rastreabilidade: cada número da minuta → plataformas contadas → fonte.
4. Quadro "apontamento da revisão → onde foi tratado na minuta final" (cobrindo as 10 melhorias prioritárias e as reescritas R1–R12).
5. Lista de pendências ("[VERIFICAR]", "[CONFERIR NUMERAÇÃO]", "[PARECER DA PROCURADORIA]").

## AUTOVERIFICAÇÃO ANTES DE ENTREGAR

- Nenhum número da minuta sem origem rastreável.
- Nenhum denominador maior que o universo (11 relatórios).
- Nenhuma atribuição a plataforma sem relatório localizado, ou com fonte indicada.
- Todas as lacunas de cobertura, risco residual, verificação, IA generativa/CSAM sintético, mensageria cifrada, proporcionalidade e faixas etárias tratadas.
- Ficha com todos os campos preenchidos para cada indicador.
- Aviso final de que o documento foi elaborado com apoio de IA e exige revisão por servidor competente antes de uso institucional.
