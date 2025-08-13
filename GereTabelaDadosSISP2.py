import pandas as pd
import re

def parse_text_to_table(text):
    # Regex para capturar os dados com base nos padrões fornecidos
    pattern = r"^(.*?) \| (.*?)\n(.*?)\n(.*?) \| (.*?)$"
    matches = re.findall(pattern, text, re.MULTILINE)

    # Definir colunas para a tabela
    columns = ["Sigla", "Órgão", "Unidade", "Localização", "Responsável"]

    # Criar o DataFrame
    df = pd.DataFrame(matches, columns=columns)
    return df

# Substitua 'raw_text' pelo texto fornecido
raw_text = """PREVIC | Superintendência Nacional de Previdência Complementar
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
James Taylor Faria Chaves
SUDAM | Superintendência do Desenvolvimento da Amazônia
CGTIC Coordenação-Geral de Tecnologia da Informação e Comunicações
PA | Pará
Gilberto Gomes da Silveira
SUDECO | Superintendência do Desenvolvimento do Centro-Oeste
CGLOG Coordenação-Geral de Logística e Tecnologia da Informação
DF | Distrito Federal
Michel Alexandre Turco
SUDENE | Superintendência do Desenvolvimento do Nordeste
CGLCI Coordenação-Geral de Licitações, Convênios e Tecnologia da Informação
PE | Pernambuco
Carlos Pedro dos Santos Nobrega
SUFRAMA | Superintendência da Zona Franca de Manaus
CGTIC Coordenação-Geral de Tecnologia da Informação e Comunicação
AM | Amazonas
Rodrigo Valente de Vasconcelos
SUSEP | Superintendência de Seguros Privados
DEATI Departamento de Administração e Tecnologia da Informação
RJ | Rio de Janeiro
Leandro Neves
UFABC | Fundação Universidade Federal do ABC
NTI Núcleo de Tecnologia da Informação
<p>SP | S&atilde;o Paulo</p>
Carlos Alberto Orsolon Silva
UFAC | Fundação Universidade Federal do Acre
NTI Núcleo de Tecnologia da Informação
AC | Acre
Jerbisclei de Souza Silva
UFAL | Universidade Federal de Alagoas
NTI Núcleo de Tecnologia da Informação
AL | Alagoas
Reinaldo Cabral Silva Filho
UFAM | Fundação Universidade do Amazonas
CTIC Centro de Tecnologia da Informação e Comunicação
AM | Amazonas
Jorge Carlos Magno Silva de Lima
UFAPE | Universidade Federal do Agreste de Pernambuco
STI.REIT Sistema de Tecnologia da Informação
PE | Pernambuco
Vamberto de Freitas Rocha Junior
UFBA | Universidade Federal da Bahia
STI Superintendência de Tecnologia da Informação
BA | Bahia
Vaninha Vinheira
UFC | Universidade Federal do Ceará
STI2 Superintendência de Tecnologia da Informação
CE | Ceará
Miguel Franklin de Castro
UFCA | Universidade Federal do Cariri
DTI Diretoria de Tecnologia da Informação
CE | Ceará
Taciano Pinheiro de Almeida Alcantara
UFCAT | Universidade Federal de Catalão
SETI-UFCAT Secretaria de Tecnologia da Informação da UFCAT
GO | Goiás
Paulo Henrique Silva Azevedo
UFCG | Universidade Federal de Campina Grande
STI-SEPLAN Serviço de Tecnologia da Informação
PB | Paraíba
Ianna Duarte Kobayashi de Souza
UFCSPA | Fundação Universidade Federal de Ciências da Saúde de Porto Alegre
NTI Núcleo de Tecnologia da Informação
RS | Rio Grande do Sul
Roberto Rosa dos Santos
UFDPar | Universidade Federal do Delta do Parnaíba
PROTIC Pró-Reitoria de Tecnologia da Informação e Comunicação
PI | Piauí
Silmar Silva Teixeira
UFERSA-RN | Universidade Federal Rural do Semi-Árido
Sutic Superintendência de Tecnologia da Informação e Comunicação
RN | Rio Grande do Norte
André Luiz Viana Pereira
UFES | Universidade Federal do Espírito Santo
STI Superintendência de Tecnologia da Informação
ES | Espírito Santo
Renan Teixeira de Souza
UFF | Universidade Federal Fluminense
STI Superintendência de Tecnologia da Informação
RJ | Rio de Janeiro
Ricardo Campanha Carrano
UFFS | Universidade Federal da Fronteira Sul
SETI Secretaria Especial de Tecnologia e Informação
SC | Santa Catarina
Cassiano Carlos Zanuzzo
UFG | Universidade Federal de Goiás
CERCOMP-SeTI Centro de Recursos Computacionais
GO | Goiás
Leandro Luís Galdino de Oliveira
UFGD | Fundação Universidade Federal da Grande Dourados
COIN Coordenadoria de Desenvolvimento de Tecnologia da Informação
MS | Mato Grosso do Sul
Luiz Fernando Stopa Arcenio
UFJ | Universidade Federal de Jataí
SETI-UFJ Secretaria de Tecnologia e Informação
GO | Goiás
Wesley Carmo Ramos
UFJF | Universidade Federal de Juiz de Fora
C_INF_TEL Coordenação de Informática, Infocentros e Telefonia
MG | Minas Gerais
Patrícia Curvelo Rodrigues Stroele
UFLA | Universidade Federal de Lavras
DGTI Diretoria de Gestão de Tecnologia da Informação
MG | Minas Gerais
Erasmo Evangelista de Oliveira
UFMA | Fundação Universidade Federal do Maranhão
STI Superintendência de Tecnologia da Informação
MA | Maranhão
Anilton Bezerra Maia
UFMG | Universidade Federal de Minas Gerais
DTI/UFMG Diretoria de Tecnologia da Informação
MG | Minas Gerais
Dorgival Olavo Guedes Neto
UFMS | Fundação Universidade Federal de Mato Grosso do Sul
AGETIC/RTR Agência de Tecnologia da Informação e Comunicação
MS | Mato Grosso do Sul
Anderson Viçoso de Araujo
UFMT | Fundação Universidade Federal de Mato Grosso
STI Secretaria de Tecnologia da Informação
MT | Mato Grosso
Jean Caminha
UFNT | Universidade Federal do Norte do Tocantins
STI Superintendência de Tecnologia da Informação
TO | Tocantins
Clarete de Itoz
UFOB | Universidade Federal do Oeste da Bahia
PROTIC Pró-Reitoria de Tecnologia da Informação e Comunicação
BA | Bahia
Uiliam Rangel
UFOPA | Universidade Federal do Oeste do Pará
CTIC Centro de Tecnologia da Informação e Comunicação
PA | Pará
Rafael Rodrigo dos Santos Miranda
UFPA | Universidade Federal do Pará
CTIC Centro de Tecnologia da Informação e Comunicação
PA | Pará
Marco Aurelio Capela
UFPB | Universidade Federal da Paraíba
STI Superintendência de Tecnologia da Informação
PB | Paraíba
Hermes Pessoa Filho
UFPE | Universidade Federal de Pernambuco
STI-UFPE Superintendência de Tecnologia da Informação
PE | Pernambuco
Marco Aurelio Benedetti Rodrigues
UFPI | Fundação Universidade Federal do Piauí
STI Superintendência de Tecnologia da Informação
PI | Piauí
Franklhes Santos Carvalho
UFPR | Universidade Federal do Paraná
AGTIC Agencia de Tecnologia da Informação e Comunicação
PR | Paraná
Felipe Sanches Bueno
UFPel | Fundação Universidade Federal de Pelotas
SGTIC Superintendência de Gestão de Tecnologia da Informação e Comunicação
RS | Rio Grande do Sul
Julio Carlos Balzano de Mattos
UFR | Universidade Federal de Rondonópolis
PROTIC Pró-Reitoria de Tecnologia da Informação e Comunicação
MT | Mato Grosso
Heinsten Frederich Leal dos Santos
UFRA | Universidade Federal Rural da Amazônia
STIC Superintendência de Tecnologia da Informação e Comunicação
PA | Pará
Walace de Sousa Elias
UFRB | Universidade Federal do Recôncavo da Bahia
COTEC Coordenadoria de Tecnologia da Informação
BA | Bahia
Anderson Lago Gomes
UFRGS | Universidade Federal do Rio Grande do Sul
CPD-UFRGS Centro de Processamento de Dados
RS | Rio Grande do Sul
Rui de Quadros Ribeiro
UFRJ | Universidade Federal do Rio de Janeiro
TIC Superintendência Geral de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Ana Maria de Almeida Ribeiro
UFRN | Universidade Federal do Rio Grande do Norte
STI Superintendência de Tecnologia da Informação
RN | Rio Grande do Norte
Marcos Cesar Madruga Alves Pinheiro
UFRPE | Universidade Federal Rural de Pernambuco
STD/UFRPE Secretaria de Tecnologias Digitais
PE | Pernambuco
Lamartine da Silva Barboza
UFRR | Fundação Universidade Federal de Roraima
DTI Diretoria de Tecnologia da Informação
RR | Roraima
Edney Veras dos Santos
UFRRJ | Universidade Federal Rural do Rio de Janeiro
COTIC Coordenadoria de Tecnologia da Informação e Comunicação (COTIC)
RJ | Rio de Janeiro
Thiago Andrade Marques da Silva
UFS | Fundação Universidade Federal de Sergipe
STIC Superintendência de Tecnologia da Informação e Comunicação
SE | Sergipe
Alberto Costa Neto
UFSB | Universidade Federal do Sul da Bahia
STI Superintendência de Tecnologia da Informação
BA | Bahia
Mydia Falcao Freitas
UFSC | Universidade Federal de Santa Catarina
SETIC/SEPLAN Superintendência de Governança Eletrônica e Tecnologia da Informação e Comunicação
SC | Santa Catarina
Bruno Carlo Celeguim de Amattos
UFSCar | Fundação Universidade Federal de São Carlos
SIn Secretaria-Geral de Informática
SP | São Paulo
Erick Lazaro Melo
UFSM | Universidade Federal de Santa Maria
CPD Centro de Processamento de Dados
RS | Rio Grande do Sul
Gustavo Zanini Kantorski
UFT | Fundação Universidade Federal do Tocantins
PROTIC Pró-reitoria de Tecnologia da Informação e Comunicação
TO | Tocantins
Werley Teixeira Reinaldo
UFU | Universidade Federal de Uberlândia
CTIC Centro de Tecnologia da Informação e Comunicação
MG | Minas Gerais
Rafael Pasquini
UFV | Fundação Universidade Federal de Viçosa
DTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Licia Felix de Andrade Ramalho
UFVJM | Universidade Federal dos Vales do Jequitinhonha e Mucuri
STI-UFVJM Superintendência de Tecnologia da Informação
MG | Minas Gerais
Thiago Mendes Borges
UNB | Fundação Universidade de Brasília
STI Secretaria de Tecnologia da Informação
DF | Distrito Federal
Marcelo Monteiro Karam
UNIFAL-MG | Universidade Federal de Alfenas
NTI Núcleo de Tecnologia da Informação
MG | Minas Gerais
Marcelo Penha Fernandes
UNIFAP | Fundação Universidade Federal do Amapá
NTI Núcleo de Tecnologia de Informação
AP | Amapá
Jose Alipio Diniz de Moraes Junior
UNIFEI | Universidade Federal de Itajubá
DTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Enzo Seraphim
UNIFESP | Universidade Federal de São Paulo
STI Superintendência de Tecnologia da Informação
SP | São Paulo
Lidiane Cristina da Silva
UNILA | Universidade Federal da Integração Latino-Americana
CTIC Coordenadoria de Tecnologia da Informação
PR | Paraná
Joylan Nunes Maciel
UNILAB | Universidade da Integração Internacional da Lusofonia Afro-Brasileira
DTI Diretoria de Tecnologia da Informação
CE | Ceará
Giancarlo Cardoso Vecchia
UNIPAMPA | Fundação Universidade Federal do Pampa
DTIC Diretoria de Tecnologia da Informação e Comunicação
RS | Rio Grande do Sul
Diego Veneroso Pereira
UNIR | Fundação Universidade Federal de Rondônia
DTI Diretoria de Tecnologia da Informação
RO | Rondônia
Andre Luiz de Souza Freitas
UNIRIO | Universidade Federal do Estado do Rio de Janeiro
PROPLAN-DTIC Diretoria de Tecnologia de Informação e Comunicação
RJ | Rio de Janeiro
Vinicius Jose Serva Pereira
UNIVASF | Fundação Universidade Federal do Vale do São Francisco
GR-STI Secretaria de Tecnologia da Informação
PE | Pernambuco
Marcelo de Medeiros Lacerda Pereira
UTFPR | Universidade Tecnológica Federal do Paraná
DIRGTI Diretoria de Gestão de Tecnologia da Informação
PR | Paraná
Diogo Augusto Barros Pereira
Unifesspa | Universidade Federal do Sul e Sudeste do Pará
CTIC Centro de Tecnologia da Informação e Comunicação
PA | Pará
Zenaide Carvalho da Silva
Órgãos Correlatos (49)
Órgão Geral ↵ Orgão SISP
UF | Município
Gestor
BCB | Coaf | Conselho de Controle de Atividades Financeiras
Cotin Coordenação-Geral de Tecnologia da Informação
Setorial: BCB | Departamento de Tecnologia da Informação
DF | Distrito Federal
José Divino da Silva
CC-PR | IN-CCIVIL | Imprensa Nacional
CGTI Coordenação-Geral de Tecnologia da Informação
Setorial: CC-PR | Diretoria de Tecnologia
DF | Distrito Federal
Marcos Vinicius Garcia Rodrigues Lima
CC-PR | ABIN | Agência Brasileira de Inteligência
CEPESC Centro de Pesquisa e Desenvolvimento para a Segurança das Comunicações
Setorial: CC-PR | Diretoria de Tecnologia
DF | Distrito Federal
Otávio Carlos Cunha da Silva
CC-PR | Casa Civil da Presidência da República
SSGINF Subsecretaria de Gestão da Informação
Setorial: CC-PR | Diretoria de Tecnologia
DF | Distrito Federal
Erica de Lima Gallindo
CC-PR | Casa Civil da Presidência da República
DAGP Diretoria de Articulação Governamental e Projetos
Setorial: CC-PR | Diretoria de Tecnologia
DF | Distrito Federal
Priscilla de Paula Marins
COFIN | Coordenação de Finanças e Contabilidade
CGGPO Coordenação-Geral de Gestão Portuária
Setorial: | Coordenação de Finanças e Contabilidade
DF | Distrito Federal
Leonardo Cahuê Martins
MAPA | Ministério da Agricultura e Pecuária
CGSM Coordenação-Geral de Soluções Meteorológicas
Setorial: MAPA | Subsecretaria de Tecnologia da Informação
DF | Distrito Federal
Leonardo Fabio Zaidan de Melo
MCID | Ministério das Cidades
CGGOV Coordenação-Geral de Governança da Tecnologia da Informação
Setorial: MCID | Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Vitor Carneiro Curado
MCTI | CTI | Centro de Tecnologia da Informação Renato Archer
DICSI Divisão de Infraestrutura Computacional e Sistemas de Informação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
SP | São Paulo
Ângela Maria Alves
MCTI | MPEG | Museu Paraense Emílio Goeldi
SETIC Serviço de Tecnologia da Informação e Comunicação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
PA | Pará
Adenilson Raniery Sarges Pontes
MCTI | INPA | Instituto Nacional de Pesquisas da Amazônia
COTIN Coordenação de Tecnologia da Informação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
AM | Amazonas
Roberto Oliveira dos Santos
MCTI | MAST | Museu de Astronomia e Ciências Afins
SERTI Serviço de Tecnologia da Informação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Rogerio Augusto de Barros Gonçalves
MCTI | INT | Instituto Nacional de Tecnologia
DITIC Divisão de Tecnologia da Informação e Comunicações
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
RJ | Rio de Janeiro
Ricardo Castro
MCTI | INPE | Instituto Nacional de Pesquisas Espaciais
COTIC Coordenação de Tecnologia da Informação e Comunicação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
SP | São Paulo
Antonio Esio Marcondes Salgado
MCTI | LNCC - MCT | Laboratório Nacional de Computação Científica
COTIC Coordenação de Tecnologia da Informação e Comunicação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
RJ | Rio de Janeiro
Wagner Vieira Leo
MCTI | IBICT | Instituto Brasileiro de Informação em Ciência e Tecnologia
CGTI Coordenação-Geral de Tecnologias de Informação e Informática
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Hugo Valadares Siqueira
MCTI | ON | Observatório Nacional
DITIN Divisão de Tecnologia da Informação
Setorial: MCTI | Coordenação-Geral de Tecnologia da Informação
RJ | Rio de Janeiro
Jorge Eduardo Mansur Serzedello
MD | HFA | Hospital das Forças Armadas
DTI Divisão de Tecnologia da Informação
Setorial: MD | Departamento de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Alessandro de Sá Barbosa
MD | CENSIPAM | Centro Gestor e Operacional do Sistema de Proteção da Amazônia
DITEC Diretoria Técnica
Setorial: MD | Departamento de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Renata Bitar Tiveron
MD | C Ex | Comando do Exército
DCT Departamento de Ciência e Tecnologia
Setorial: MD | Departamento de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Gen Ex Achilles Furlan Neto
MD | COMAER | Comando da Aeronáutica
DTI Diretoria de Tecnologia da Informação da Aeronáutica
Setorial: MD | Departamento de Tecnologia da Informação e Comunicação
SP | São Paulo
Major Brigadeiro Engenheiro Eliezer de Freitas Cabral
MD | MB | Comando da Marinha
DCTIM Diretoria de Comunicações e Tecnologia da Informação da Marinha
Setorial: MD | Departamento de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Calte Marcelo da Silva Gomes
MDS | SAGICAD Secretaria de Avaliação, Gestão da Informação e Cadastro Único
SAGICAD Secretaria de Avaliação, Gestão da Informação e Cadastro Único
Setorial: MDS | Subsecretaria de Tecnologia da Informação
DF | Distrito Federal
Leticia Bartholo de Oliveira e Silva
MDS | SENARC Secretaria Nacional de Renda de Cidadania
SENARC Secretaria Nacional de Renda de Cidadania
Setorial: MDS | Subsecretaria de Tecnologia da Informação
DF | Distrito Federal
Eliane Aquino Custodio
MDS | Ministério do Desenvolvimento e Assistência Social, Família e Combate à Fome
CGRS Coordenação-Geral da Rede SUAS
Setorial: MDS | Subsecretaria de Tecnologia da Informação
DF | Brasília
Frederico de Almeida Meirelles Palma
MEC | INES | Instituto Nacional de Educação de Surdos
DI Divisão de Informática
Setorial: MEC | Subsecretaria de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Luis Carlos Carvalho Riera
MEMP | Ministério do Empreendedorismo, da Microempresa e da Empresa de Pequeno Porte
DREI Diretoria Nacional de Registro Empresarial e Integração
Setorial: MEMP | Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Flavia Regina Britto Gonçalves
MF | STN | Secretaria do Tesouro Nacional
COSIS Coordenação-Geral de Sistemas e Tecnologia de Informação
Setorial: MF | Subsecretaria de Gestão, Tecnologia da Informação e Orçamento
DF | Distrito Federal
Abdsandryk Cunha de Souza
MF | PGFN | Procuradoria-Geral da Fazenda Nacional
CGTI Coordenação-Geral de Tecnologia da Informação
Setorial: MF | Subsecretaria de Gestão, Tecnologia da Informação e Orçamento
DF | Distrito Federal
Rodrigo Otavio Povoa Pullen Parente
MF | RFB | Secretaria Especial da Receita Federal do Brasil
Cotec Coordenação-Geral de Tecnologia e Segurança da Informação
Setorial: MF | Subsecretaria de Gestão, Tecnologia da Informação e Orçamento
DF | Distrito Federal
Felipe Mendes Moraes
MGI | ITI | Instituto Nacional de Tecnologia da Informação
DAFN Diretoria de Auditoria, Fiscalização e Normalização
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Pedro Pinheiro Cardoso
MGI | AN | Arquivo Nacional
COTIN Coordenação-Geral de Tecnologia da Informação
Setorial: MGI | Secretaria de Serviços Compartilhados
RJ | Rio de Janeiro
Maximiliano Martins de Faria
MGI | SPU | Secretaria do Patrimônio da União
DEMIN Diretoria de Modernização e Inovação
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Ana Paula Bruno
MGI | Ministério da Gestão e da Inovação em Serviços Públicos
DPDCR Diretoria de Participação Digital e Comunicação em Rede
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Carla de Paiva Bezerra
MGI | SGP | Secretaria de Gestão de Pessoas
DESIN Diretoria de Soluções Digitais
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Antonio Fiuza de Sousa Landim
MGI | SEGES Secretaria de Gestão e Inovação
SEGES Secretaria de Gestão e Inovação
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Roberto Seara Machado Pojo Rego
MGI | SEST | Secretaria de Coordenação e Governança das Empresas Estatais
DIGES Diretoria de Inovação e Inteligência em Gestão de Estatais
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Brasília
Hamilton Fernando Cota Cruz
MGI | ITI | Instituto Nacional de Tecnologia da Informação
DITEC Diretoria de Infraestrutura Tecnológica
Setorial: MGI | Secretaria de Serviços Compartilhados
DF | Distrito Federal
Mauricio Augusto Coelho
MJSP | PRF | Polícia Rodoviária Federal
DTIC Diretoria de Tecnologia da Informação e Comunicação
Setorial: MJSP | Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Joedson Camilo de Oliveira
MJSP | PF | Polícia Federal
DTI/PF Diretoria de Tecnologia da Informação e Comunicação
Setorial: MJSP | Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Ademir Dias Cardoso Junior
MJSP | SENAPPEN | Secretaria Nacional de Políticas Penais
CGETI Coordenação-Geral de Estatística e Tecnologia de Informação
Setorial: MJSP | Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Rodrigo de Morais Santana
MJSP | SENACON | Secretaria Nacional do Consumidor
CGSINDEC Coordenação-Geral do Sistema Nacional de Informações de Defesa do Consumidor
Setorial: MJSP | Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Alexandre Yamanaka Shiozaki
MMA | SFB | Serviço Florestal Brasileiro
CGT Coordenação-Geral de Tecnologia da Informação
Setorial: MMA | Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
MPO | SOF | Secretaria de Orçamento Federal
SETEC Subsecretaria de Tecnologia e Desenvolvimento Institucional
Setorial: MPO | Coordenação de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Felipe Cesar Araujo da Silva
MS | INC | Instituto Nacional de Cardiologia
DTI Divisão de Tecnologia da Informação
Setorial: MS | Departamento de Informação e Informática do Sistema Único de Saúde
RJ | Rio de Janeiro
Daniel Soares
MS | Ministério da Saúde
DEMAS Departamento de Monitoramento, Avaliação e Disseminação de Informações Estratégicas em Saúde
Setorial: MS | Departamento de Informação e Informática do Sistema Único de Saúde
DF | Distrito Federal
Paulo Eduardo Guedes Sellera
MS | INCA | Instituto Nacional de Câncer
SETI/INCA Serviço de Tecnologia da Informação
Setorial: MS | Departamento de Informação e Informática do Sistema Único de Saúde
RJ | Rio de Janeiro
Roberto Luiz Silva dos Santos
MT | SENATRAN Secretaria Nacional de Trânsito
SENATRAN Secretaria Nacional de Trânsito
Setorial: MT | Subsecretaria de Gestão Estratégica, Tecnologia e Inovação
DF | Distrito Federal
Adrualdo de Lima Catao
MinC | FBN | Fundação Biblioteca Nacional
CTI Núcleo de Tecnologia da Informação
Setorial: MinC | Subsecretaria de Tecnologia da Informação e Inovação
DF | Brasília
Geraldo Gonçalves Chaves Junior"""

df = parse_text_to_table(raw_text)

# Gerar um arquivo CSV com os dados
df.to_csv("dados_sisp.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'dados_sisp.csv' gerado com sucesso!")

