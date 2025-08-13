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
raw_text = """AGU | Advocacia-Geral da União
SGE Secretaria de Governança e Gestão Estratégica
DF | Brasília
Francisco Alexandre Colares Melo Carlos
CC-PR | Casa Civil da Presidência da República
DITEC Diretoria de Tecnologia
DF | Distrito Federal
Bruno Pereira Pontes
CGU | Controladoria-Geral da União
DTI Diretoria de Tecnologia da Informação
DF | Distrito Federal
Henrique Aparecido da Rocha
GSI/PR | Gabinete de Segurança Institucional da Presidência da República
DSI Departamento de Segurança da Informação
DF | Distrito Federal
Luis Sergio da Costa Souto
MAPA | Ministério da Agricultura e Pecuária
STI Subsecretaria de Tecnologia da Informação
DF | Distrito Federal
Camilo Mussi
MCTI | Ministério da Ciência, Tecnologia e Inovação
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Eduardo Viola
MinC | Ministério da Cultura
STII Subsecretaria de Tecnologia da Informação e Inovação
DF | Distrito Federal
MD | Ministério da Defesa
DETIC Departamento de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Bruno Fassheber Novais
MEC | Ministério da Educação
STIC Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Marco Antonio Fragoso de Souza
MF | Ministério da Fazenda
SGTO Subsecretaria de Gestão, Tecnologia da Informação e Orçamento
DF | Distrito Federal
Vladimir Reis Joaquim Lopes
MGI | Ministério da Gestão e da Inovação em Serviços Públicos
SSC Secretaria de Serviços Compartilhados
DF | Distrito Federal
Cilair Rodrigues de Abreu
MIDR | Ministério da Integração e do Desenvolvimento Regional
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Daniel Portilho Troncoso
MJSP | Ministério da Justiça e Segurança Pública
STI Subsecretaria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Solange Berto de Medeiros
MPA | Ministério da Pesca e Aquicultura
COINFO Coordenação de Tecnologia da Informação, Organização e Inovação
DF | Distrito Federal
Camilo Mussi
MPS | Ministério da Previdência Social
COATI Coordenação de Administração de Recursos de Tecnologia da Informação
DF | Distrito Federal
Daniel Moser Lopes
MS | Ministério da Saúde
DATASUS Departamento de Informação e Informática do Sistema Único de Saúde
<p>DF | Distrito Federal</p>
Graziella Cervo Santana
MCID | Ministério das Cidades
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Lucas Mendes dos Santos
MCOM | Ministério das Comunicações
SPTI Subsecretaria de Planejamento e Tecnologia da Informação
DF | Distrito Federal
Gustavo Henrique de Souto Silva
MMULHERES | Ministério das Mulheres
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Brasília
Clelson Salles Rodrigues
MRE | Ministério das Relações Exteriores
DTIC Departamento de Tecnologia e Gestão da Informação
DF | Distrito Federal
Maria Clara de Abreu Rada
MME | Ministério de Minas e Energia
SE Secretaria-Executiva
DF | Brasília
Arthur Cerqueira Valerio
MPOR | Ministério de Portos e Aeroportos
CGTEC Coordenação-Geral de Inovação e Tecnologias da Informação e Comunicação
DF | Distrito Federal
Cristiano Gontijo Silva
MDA | Ministério do Desenvolvimento Agrário e Agricultura Familiar
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Pamela Santiago Hilário
MDS | Ministério do Desenvolvimento e Assistência Social, Família e Combate à Fome
STI Subsecretaria de Tecnologia da Informação
DF | Distrito Federal
Avelino Medeiros da Silva Filho
MDIC | Ministério do Desenvolvimento, Indústria, Comércio e Serviços
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Goudim Alvarenga Carneiro
MEMP | Ministério do Empreendedorismo, da Microempresa e da Empresa de Pequeno Porte
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Brasília
Jose Antonio Lima e Silva
MESP | Ministério do Esporte
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Brasília
Guilherme Augusto Silva Ribeiro
MMA | Ministério do Meio Ambiente e Mudança do Clima
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Jonas Jeske
MPO | Ministério do Planejamento e Orçamento
COTIC Coordenação de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Alvaro Jose de Andrade Carneiro
MTE | Ministério do Trabalho e Emprego
DTI Diretoria de Tecnologia da Informação
DF | Distrito Federal
Heber Fialho Maia Junior
MTur | Ministério do Turismo
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Mario Ruda Pontes de Andrade
MDHC | Ministério dos Direitos Humanos e da Cidadania
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Hugo da Luz Silva
MPI | Ministério dos Povos Indígenas
COTEC Coordenação de Tecnologia da Informação
DF | Distrito Federal
Vilson da Silva Santos Junior
MT | Ministério dos Transportes
SGETI Subsecretaria de Gestão Estratégica, Tecnologia e Inovação
DF | Brasília
Diogo Fonseca Tabalipa
Órgãos Seccionais (170)
Órgão Geral ↵ Orgão SISP
UF | Município
Gestor
AEB | Agência Espacial Brasileira
CTI Coordenação de Tecnologia da Informação
DF | Distrito Federal
Kaio da Silva Pontes
ANA | Agência Nacional de Águas e Saneamento Básico
STI Superintendência de Tecnologia da Informação
DF | Distrito Federal
Mosar Rodrigues Rabelo Junior
ANAC | Agência Nacional de Aviação Civil
STD Superintendência de Tecnologia e Transformação Digital
DF | Distrito Federal
Fernando Andre Coelho Mitkiewicz
ANATEL | Agência Nacional de Telecomunicações
SGI Superintendência de Gestão Interna da Informação
DF | Distrito Federal
Gustavo Nery e Silva
ANCINE | Agência Nacional do Cinema
GTI Gerência de Tecnologia da Informação
RJ | Rio de Janeiro
Bruno Schneider
ANEEL | Agência Nacional de Energia Elétrica
SGI Superintendência de Gestão Técnica da Informação
DF | Distrito Federal
Adriana de Carvalho Drummond Vivan
ANM | Agência Nacional de Mineração
STI-ANM Superintendência de Tecnologia da Informação e Inovação
DF | Distrito Federal
Fabio Fernando Borges
ANP | Agência Nacional do Petróleo, Gás Natural e Biocombustíveis
STI Superintendência de Tecnologia da Informação
RJ | Rio de Janeiro
Adriana Marcilio
ANPD | Autoridade Nacional de Proteção de Dados
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Igor de Moura Leite Moreira
ANS | Agência Nacional de Saúde Suplementar
GETI Gerência de TecnoIogia de Informação
RJ | Rio de Janeiro
Luciene Pinheiro Capra
ANTAQ | Agência Nacional de Transportes Aquaviários
GTGI Gerência de Tecnologia e Gestão da Informação
DF | Distrito Federal
Alexandre Ferreira de Alencar
ANTT | Agência Nacional de Transportes Terrestres
SUTEC Superintendência de Tecnologia da Informação
DF | Distrito Federal
Klaymer Alves de Amorim Paz
ANVISA | Agência Nacional de Vigilância Sanitária
GGTIN Gerência-Geral de Tecnologia da Informação
DF | Distrito Federal
Jorge Carvalho de Oliveira
BCB | Banco Central do Brasil
Deinf Departamento de Tecnologia da Informação
DF | Distrito Federal
Haroldo Jayme Martins Froes Cruz
CADE | Conselho Administrativo de Defesa Econômica
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Vinicius Eloy dos Reis
CAPES | Fundação Coordenação de Aperfeiçoamento de Pessoal de Nível Superior
DTI Diretoria de Tecnologia da Informação
DF | Distrito Federal
Gustavo Jardim Portella
CDP | Companhia Docas do Pará
GTI Gerência de Tecnologia da Informação
PA | Pará
Fábio Gonçalves
CEAGESP | Companhia de Entrepostos e Armazéns Gerais de São Paulo
DTI Diretoria de Tecnologia da Informação
SP | São Paulo
Eduardo Faula de Almeida
CEFET-MG | Centro Federal de Educação Tecnológica de Minas Gerais
DTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Sandro Dias
CEFET-RJ | Centro Federal de Educação Tecnológica - Celso Suckow da Fonseca
DTINF Departamento de Tecnologia da Informação
RJ | Rio de Janeiro
Enoch Cezar Pimentel Lins da Silva
CNEN | Comissão Nacional de Energia Nuclear
CGTI Coordenação-Geral de Ciência e Tecnologia da Informação
RJ | Rio de Janeiro
Emerson Antunes Coimbra
CNPq | Conselho Nacional de Desenvolvimento Científico e Tecnológico
CGETI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Geraldo Sorte
CODEBA | Companhia das Docas do Estado da Bahia
GTI Gerência de Tecnologia da Informação
BA | Bahia
Fabíola Alves de Castro
CP II | Colégio Pedro II
DTI Diretoria de Tecnologia da Informação
RJ | Rio de Janeiro
Felipe de Lima dos Santos Medeiros
CVM | Comissão de Valores Mobiliários
STI Superintendência de Tecnologia da Informação
RJ | Rio de Janeiro
Carlos Cesar Valentim Alves
DNIT | Departamento Nacional de Infraestrutura de Transportes
CGTI-DAF Coordenação-Geral de Tecnologia da Informação-DAF
DF | Distrito Federal
Andre Luis Albernaz Martinez
DNOCS | Departamento Nacional de Obras Contra as Secas
DA/DRL/STI Serviço de Tecnologia da Informação
CE | Ceará
Antonio Gutemberg Ferreira Maia
EBC | Empresa Brasil de Comunicação S.A.
GXTIN Gerência Executiva de Tecnologia da Informação
DF | Distrito Federal
Jorge Luis de Lima Varella
EMGEPRON | Empresa Gerencial de Projetos Navais
DTI Departamento de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Luiz Cláudio Malafaia Pacheco
Enap | Fundação Escola Nacional de Administração Pública
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Frank James da Silva Pires
FCP | Fundação Cultural Palmares
NTIC Núcleo de Tecnologia da Informação
DF | Distrito Federal
Ivanildo Feliciano da Silva
FCRB | Fundação Casa de Rui Barbosa
STIC Serviço de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Vitor Silveira Pereira
FIOCRUZ | Fundação Oswaldo Cruz
COGETIC Coordenação-Geral de Gestão de Tecnologia de Informação
RJ | Rio de Janeiro
Misael Sousa de Araujo
FNDE | Fundo Nacional de Desenvolvimento da Educação
DIRTI Diretoria de Tecnologia e Inovação
DF | Distrito Federal
Delson Pereira da Silva
FUFOP | Fundação Universidade Federal de Ouro Preto
NTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Abelard Ramos Fernandes
FUNAG | Fundação Alexandre de Gusmão
DTI Divisão de Tecnologia da Informação
DF | Distrito Federal
Victor Davi Pereira Goncalves
FUNAI | Fundação Nacional dos Povos Indígenas
CGTic Coordenação-Geral de Tecnologia da Informação e Comunicações
DF | Distrito Federal
Matheus Filipe Silva Araújo
FUNARTE | Fundação Nacional de Artes
COTIC Coordenação de Tecnologia da Informação e Conectividade
RJ | Rio de Janeiro
Ronaldo Lucena de Marins
FUNASA | Fundação Nacional de Saúde
Cgmti Coordenação-Geral de Modernização e Tecnologia da Informação
DF | Distrito Federal
Rodney Lawson Marques Zica (interino)
FUNDACENTRO | Fundação Jorge Duprat Figueiredo, de Segurança e Medicina do Trabalho
CTIC Coordenação de Tecnologia da Informação e Comunicação
SP | São Paulo
Diego Ricardi dos Anjos
FUNDAJ | Fundação Joaquim Nabuco
CTINFO Coordenação de Tecnologia da Informação
PE | Pernambuco
Stenio Correia de Barros
FUNRei | Fundação Universidade Federal de São João Del Rei
NTINF Núcleo de Tecnologia da Informação
MG | Minas Gerais
Rodrigo de Carvalho Santos
FURG | Fundação Universidade Federal do Rio Grande
CGTI Centro de Gestão da Tecnologia da Informação
<p>RS | Rio Grande do Sul</p>
Diogo Paludo de Oliveira
HCPA | Hospital de Clínicas de Porto Alegre
CGTIC Coordenação de Gestão da Tecnologia da Informação e Comunicação
RS | Rio Grande do Sul
Andre Mena Avila
IBAMA | Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Elias Marques Cotrim
IBGE | Fundação Instituto Brasileiro de Geografia e Estatística
DTI Diretoria de Tecnologia da Informação
RJ | Rio de Janeiro
Marcos Vinicius Ferreira Mazoni
IBRAM | Instituto Brasileiro de Museus
CTINF Coordenação de Tecnologia e Informação
DF | Distrito Federal
Marcos Sigismundo da Silva
ICMBio | Instituto Chico Mendes de Conservação da Biodiversidade
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Renata Cesario de Oliveira Gomes
IF BAIANO | Instituto Federal de Educação, Ciência e Tecnologia Baiano
DGTI Diretoria de Gestão de Tecnologia da Informação
BA | Bahia
Robson Cordeiro Ramos
IF-GOIANO | Instituto Federal de Educação, Ciência e Tecnologia Goiano
DTI/REI Diretoria de Tecnologia da Informação
GO | Goiás
Douglas de Franca Alves
IFAC | Instituto Federal de Educação, Ciência e Tecnologia do Acre
DSGTI Diretoria Sistêmica de Tecnologia da Informação
AC | Acre
Djameson Oliveira da Silva
IFAL | Instituto Federal de Educação, Ciência e Tecnologia de Alagoas
DTI/PRDI Diretoria de Tecnologia da Informação
AL | Alagoas
Fernando Antonio Corado Carneiro
IFAM | Instituto Federal de Educação, Ciência e Tecnologia do Amazonas
DGTI Diretoria de Gestão de Tecnologia da Informação
AM | Amazonas
Joao Luiz Cavalcante Ferreira
IFAP | Instituto Federal de Educação, Ciência e Tecnologia do Amapá
DITI Diretoria de Tecnologia da Informação
AP | Amapá
Robson Luiz Silva Souza
IFB | Instituto Federal de Educação, Ciência e Tecnologia de Brasília
DTIC Diretoria de Tecnologia da Informação e Comunicação
DF | Distrito Federal
Joao Victor de Araujo Oliveira
IFBA | Instituto Federal de Educação, Ciência e Tecnologia da Bahia
DGTI Diretoria de Gestão da Tecnologia da Informação
BA | Bahia
Marcio Melo de Oliveira
IFC | Instituto Federal de Educação, Ciência e Tecnologia Catarinense
DTI Diretoria de Tecnologia da Informação
SC | Santa Catarina
Tiago Heineck
IFCE | Instituto Federal de Educação, Ciência e Tecnologia do Ceará
DGTI-REI Diretoria de Gestão da Tecnologia da Informação
CE | Ceará
Danilo Reis de Vasconcelos
IFES | Instituto Federal de Educação, Ciência e Tecnologia do Espírito Santo
DRTI Diretoria de Tecnologia da Informação
ES | Espírito Santo
Johnathan Dezan Vago
IFF | Instituto Federal de Educação, Ciência e Tecnologia Fluminense
DGTIREIT Diretoria de Gestão de Tecnologia da Informação
RJ | Rio de Janeiro
Ronaldo Amaral Santos
IFFAR | Instituto Federal de Educação, Ciência e Tecnologia Farroupilha
DTI Diretoria de Tecnologia da Informação
RS | Rio Grande do Sul
Juliano Rossato da Silva
IFG | Instituto Federal de Educação, Ciência e Tecnologia de Goiás
REI-DTI Diretoria de Tecnologia da lnformaçäo
GO | Goiás
Daniel Rosa Canedo
IFMA | Instituto Federal de Educação, Ciência e Tecnologia do Maranhão
DIGTI-PROPLADI Diretoria de Gestão de Tecnologia da Informação
MA | Maranhão
William Correa Mendes
IFMG | Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais
RE-DTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Adriano Olimpio Tonelli
IFMS | Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso do Sul
Dirti Diretoria de Gestão de Tecnologia da Informação
MS | Mato Grosso do Sul
Carlitos Fioravante Vieira de Oliveira
IFMT | Instituto Federal de Educação, Ciência e Tecnologia de Mato Grosso
DSTI Diretoria de Tecnologia da Informação
MT | Mato Grosso
Rafael Bezerra Scarselli
IFNMG | Instituto Federal de Educação, Ciência e Tecnologia do Norte de Minas Gerais
DGTI Diretoria de Gestão de Tecnologia da Informação
MG | Minas Gerais
Alisson Rodrigo Vieira
IFPA | Instituto Federal de Educação, Ciência e Tecnologia do Pará
REITORIA/DTI Diretoria de Tecnologia da Informação
PA | Pará
Gracielly Costa Fontes Cardoso
IFPB | Instituto Federal de Educação, Ciência e Tecnologia da Paraíba
DGTI-RE Diretoria Geral de Tecnologia e Informação
PB | Paraíba
Fabio de Albuquerque Silva
IFPE | Instituto Federal de Educação, Ciência e Tecnologia de Pernambuco
DTI/REI Diretoria de Tecnologia da Informação
PE | Pernambuco
Jobson Tenório do Nascimento
IFPI | Instituto Federal de Educação, Ciência e Tecnologia do Piauí
DTI Diretoria de Tecnologia da Informação
PI | Piauí
Diego Cordeiro de Oliveira
IFPR | Instituto Federal de Educação, Ciência e Tecnologia do Paraná
DGTI/IFPR Diretoria de Gestão de Tecnologia da Informação
PR | Paraná
Giovanni Mori
IFRJ | Instituto Federal de Educação, Ciência e Tecnologia do Rio de Janeiro
DGTIC Diretoria de Gestão de Tecnologia da Informação e Comunicação
RJ | Rio de Janeiro
Fabio Carlos Macedo
IFRN | Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte
DIGTI Diretoria de Gestão de Tecnologia da Informação
RN | Rio Grande do Norte
Tarso Latorraca Casadei
IFRO | Instituto Federal de Educação, Ciência e Tecnologia de Rondônia
DGTI Diretoria de Gestão da Tecnologia da Informação
RO | Rondônia
Bruce Fabian Reis Albuquerque
IFRR | Instituto Federal de Educação, Ciência e Tecnologia de Roraima
DTI Diretoria de Tecnologia da Informação
RR | Roraima
Diogo Rocha Ferreira Maia
IFRS | Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Sul
DTI-REI Diretoria de Tecnologia da Informação
RS | Rio Grande do Sul
Cesar Germano Eltz
IFS | Instituto Federal de Educação, Ciência e Tecnologia de Sergipe
DTIREI Diretoria de Tecnologia da Informação
SE | Sergipe
Marcos Pereira dos Santos
IFSC | Instituto Federal de Educação, Ciência e Tecnologia de Santa Catarina
DTIC-REI Diretoria de Tecnologias da Informação e Comunicação
SC | Santa Catarina
Benoni de Oliveira Pires
IFSP | Instituto Federal de Educação, Ciência e Tecnologia de São Paulo
DTI-SPO Diretoria de Tecnologia da Informação
<p>SP | S&atilde;o Paulo</p>
Leonardo Menzani Silva
IFSUDMG | Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas Gerais
DTIC Diretoria de Tecnologia da Informação e Comunicação
MG | Minas Gerais
Igor Meneguitte Avila
IFSULMG | Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas Gerais
DTI Diretoria de Tecnologia da Informação
MG | Minas Gerais
Ramon Gustavo Teodoro Marques da Silva
IFSertaoPE | Instituto Federal de Educação, Ciência e Tecnologia do Sertão Pernambucano
RT.DGTI Diretoria de Gestão de Tecnologia de Informação
PE | Pernambuco
Francisco Hamilton de Freitas Junior
IFSul | Instituto Federal de Educação, Ciência e Tecnologia Sul-Rio-Grandense
IF-DTI Diretoria de Tecnologia da Informação
RS | Rio Grande do Sul
Carla Simone Guedes Pires
IFTM | Instituto Federal de Educação, Ciência e Tecnologia do Triângulo Mineiro
DTIC-REI Diretoria de Tecnologia da Informação e Comunicação
MG | Minas Gerais
Lídia Paiva Tomaz
IFTO | Instituto Federal de Educação, Ciência e Tecnologia do Tocantins
REI-DTI Diretoria de Tecnologia da Informação
TO | Tocantins
Kleyton Matos Moreira
INCRA | Instituto Nacional de Colonização e Reforma Agrária
DOT Coordenação-Geral de Tecnologia e Gestão da Informação
DF | Distrito Federal
Thiago Varanda Barbosa
INEP | Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
CETIC Centro de Tecnologia, Inovação e Ciência de Dados
DF | Brasília
Fernando Szimanski
INFRA-SA | INFRA S.A.
STI Superintendência de Tecnologia da Informação
DF | Distrito Federal
Renato Ricardo Alves
INFRAERO | Empresa Brasileira de Infraestrutura Aeroportuária
DATI Superintendência de Tecnologia da Informação
DF | Distrito Federal
José Renato Couto de Pontes
INMETRO | Instituto Nacional de Metrologia, Qualidade e Tecnologia
CTINF Coordenação-Geral de Tecnologia da Informação
RJ | Rio de Janeiro
Edna Paula Peixoto da Mota
INPI | Instituto Nacional da Propriedade Industrial
CGTI Coordenação-Geral de Tecnologia da Informação
RJ | Rio de Janeiro
Marcus Vinicius da Motta Vieira
INSS | Instituto Nacional do Seguro Social
DTI Diretoria de Tecnologia da Informação
DF | Distrito Federal
Mario Galvao de Souza Soria
IPEA | Instituto de Pesquisa Econômica Aplicada
CGDTI Coordenação-Geral de Ciência de Dados e Tecnologia da Informação
DF | Distrito Federal
Lucas Ferreira Mation
IPHAN | Instituto do Patrimônio Histórico e Artístico Nacional
CGTI Coordenação-Geral de Tecnologia da Informação
DF | Distrito Federal
Americo Arantes Ferreira Nogueira
ITI | Instituto Nacional de Tecnologia da Informação
CGTIC Coordenação-Geral de Tecnologia da Informação e Comunicação
DF | Brasília
Ingrid Palma Araujo
JBRJ | Instituto de Pesquisas Jardim Botânico do Rio de Janeiro
CTIC Coordenação de Tecnologia da Informação e Comunicação
DF | Brasília
Laura Estela Madeira de Carvalho
MEC | Ministério da Educação
DTI Departamento de Tecnologia da Informação
MG | Minas Gerais
Mario Roberto Ferreira
MPOR | Ministério de Portos e Aeroportos
CODERN Companhia Docas do Rio Grande do Norte
DF | Brasília
Sérgio Kleber Matias de Lima"""

df = parse_text_to_table(raw_text)

# Gerar um arquivo CSV com os dados
df.to_csv("dados_sisp.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'dados_sisp.csv' gerado com sucesso!")
