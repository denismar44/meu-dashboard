#openai.api_key = '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'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import openai

# Configuração do driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Chave da API OpenAI
openai.api_key = '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'

def resumir_mensagens(mensagens):
    """
    Função para resumir mensagens usando a API da OpenAI.
    """
    try:
        resposta = openai.Completion.create(
            model="text-davinci-003",
            prompt="Resuma as seguintes mensagens:\n" + "\n".join(mensagens),
            max_tokens=50
        )
        return resposta.choices[0].text.strip()
    except Exception as e:
        print("Erro ao usar a OpenAI:", e)
        return "Erro ao gerar resumo."

try:
    # Acessa o WhatsApp Web
    print("Abrindo o WhatsApp Web...")
    driver.get('https://web.whatsapp.com')
    time.sleep(15)  # Aguarde o usuário escanear o QR Code

    # Localizar a barra de pesquisa
    print("Tentando localizar a barra de pesquisa...")
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1n2onr6 xh8yej3 lexical-rich-text-input')]"))
    )
    print("Barra de pesquisa encontrada. Garantindo visibilidade...")

    # Verifique se o elemento está clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x1n2onr6 xh8yej3 lexical-rich-text-input')]"))
    )

    # Use JavaScript para focar no elemento
    print("Forçando foco no elemento...")
    driver.execute_script("arguments[0].focus();", search_box)
    time.sleep(1)

    # Envie o texto diretamente
    print("Inserindo o nome do grupo...")
    search_box.send_keys("CONCURSO /SEFAZ / GERAL")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Localiza e seleciona o grupo
    print("Tentando localizar o grupo...")
    group = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[@title='🏛️ CONCURSO /SEFAZ / GERAL']"))
    )
    group.click()
    print("Grupo localizado e selecionado.")

    # Coleta as mensagens do grupo
    print("Coletando mensagens...")
    messages = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
    mensagens = [message.text for message in messages]
    print(f"Mensagens coletadas: {mensagens}")

    # Gera o resumo das mensagens
    print("Gerando resumo das mensagens...")
    resumo = resumir_mensagens(mensagens)
    print("Resumo gerado:", resumo)

except Exception as e:
    print("Erro durante a execução do script:", e)

finally:
    print("Finalizando o driver...")
    driver.quit()
