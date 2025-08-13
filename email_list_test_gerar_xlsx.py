import pandas as pd

# Define the data for the test email messages and attachments
data = {
    "De": ["MGI/Programa de Privacidade e Segurança da Informação <ppsi.sgd@gestao.gov.br>"] * 4,
    "Para": [
        "denis.oliveira@gestao.gov.br",
        "denismar@gmail.com.br",
        "denisma@hotmail.com",
        "annacfv@hotmail.com"
    ],
    "Assunto": ["Indicadores do Ciclo 1 do Programa de Privacidade e Segurança da Informação"] * 4,
    "Mensagem": [
        "Cumprimentando-as(os) cordialmente, refiro-me à Portaria SGD/MGI nº 852, de 28 de março de 2023, que dispõe sobre o Programa de Privacidade e Segurança da Informação PPSI e instituiu-se o Framework de Privacidade e Segurança da Informação.\n"
        "A Secretaria de Governo Digital (SGD) entende que a privacidade e a segurança da informação são temas relevantes que devem ser tratados como tópicos relacionados aos riscos estratégicos das organizações integrantes do SISP. Dessa forma, com o avanço do Governo Digital Brasileiro, é importante continuarmos o aprimoramento dos nossos controles e medidas de privacidade e segurança da informação em nossa superfície digital. Neste contexto, a SGD tem empreendido uma série de iniciativas no âmbito do Programa de Privacidade e Segurança da Informação (PPSI), em matéria de governança, maturidade, metodologia, pessoas e tecnologia.\n"
        "Eventos regionalizados do Programa de Apoio ao Diagnóstico do PPSI foram realizados de 8 a 15 de abril do corrente ano para apresentar estatísticas do Ciclo 1 do PPSI, sugestões para aumento da maturidade, atualizar informações do catálogo de serviços e comunidades regionalizadas de privacidade e segurança da informação e sanar dúvidas gerais.\n"
        "O Ciclo 1 do PPSI encerrou-se em 31/12/2023, sendo as respostas atualizadas dos diagnósticos dos órgãos nos enviadas nos meses subsequentes, as quais processamos e trazemos informações relevantes para auxiliar seu órgão em melhorias internas, planejamentos, avanços e tomadas de decisões relacionadas aos temas de privacidade e segurança da informação.\n\n"
        "Atenciosamente,\n\n"
        "Coordenação Geral de Privacidade\n"
        "Coordenação de Maturidade\n"
        "DEPSI - SGD"
    ] * 4,
    "Anexo": [
        "C:\\Users\\denis\\Downloads\\NuvemTim\\SEI_19974.002126_2024_15_pdf\\[001]-45982694_Oficio_152325.pdf",
        "C:\\Users\\denis\\Downloads\\NuvemTim\\SEI_19974.002126_2024_15_pdf\\[002]-45982700_Oficio_152326.pdf",
        "C:\\Users\\denis\\Downloads\\NuvemTim\\SEI_19974.002126_2024_15_pdf\\[003]-45982705_Oficio_152327.pdf",
        "C:\\Users\\denis\\Downloads\\NuvemTim\\SEI_19974.002126_2024_15_pdf\\[004]-45982708_Oficio_152328.pdf"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel file
output_path = "C:/Users/denis/OneDrive/Documentos/python/email_list_test.xlsx"
df.to_excel(output_path, index=False)

output_path
