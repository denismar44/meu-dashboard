import pdfkit
import os

# Caminho do executável wkhtmltopdf
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
pdfkit_config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Caminho da pasta com os arquivos HTML
pasta_html = r'C:\Users\denis\Downloads\NuvemTim\SEI_19974.002126_2024_15'
# Caminho para salvar os PDFs
pasta_pdf = r'C:\Users\denis\Downloads\NuvemTim\SEI_19974.002126_2024_15_pdf'

# Certifique-se que a pasta para salvar os PDFs existe
os.makedirs(pasta_pdf, exist_ok=True)

# Lista todos os arquivos na pasta
arquivos = os.listdir(pasta_html)

# Converte cada arquivo HTML em PDF
for arquivo in arquivos:
    if arquivo.endswith('.html'):
        caminho_html = os.path.join(pasta_html, arquivo)
        caminho_pdf = os.path.join(pasta_pdf, arquivo.replace('.html', '.pdf'))
        pdfkit.from_file(caminho_html, caminho_pdf, configuration=pdfkit_config)
        print(f"Convertido: {arquivo} para PDF")
