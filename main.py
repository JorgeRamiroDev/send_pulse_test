# -*-coding:utf8-*-

"""
Aplicação SendPulse SMS

Documentação:
    https://sendpulse.com/api
"""

from pysendpulse.pysendpulse import PySendPulse
import os 

def initialize_sendpulse(api_id, api_secret):
    """
    Inicializa a instância do PySendPulse com as credenciais fornecidas.
    
    :param api_id: Seu REST API ID do SendPulse
    :param api_secret: Seu REST API Secret do SendPulse
    :return: Instância do PySendPulse
    """
    TOKEN_STORAGE = 'memcached'  # Pode ser 'file', 'memcached', etc.
    MEMCACHED_HOST = '127.0.0.1:11211'  # Ajuste conforme sua configuração
    return PySendPulse(api_id, api_secret, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

def add_phone_numbers(api_proxy, addressbook_id, phone_numbers):
    """
    Adiciona números de telefone a um addressbook específico.
    
    :param api_proxy: Instância do PySendPulse
    :param addressbook_id: ID do addressbook onde os números serão adicionados
    :param phone_numbers: Lista de números de telefone (strings)
    """
    try:
        response = api_proxy.sms_add_phones(addressbook_id, phone_numbers)
        print(f"Números adicionados com sucesso: {response}")
    except Exception as e:
        print(f"Erro ao adicionar números: {e}")

def create_and_send_sms_campaign(api_proxy, sender_name, addressbook_id, message_text, campaign_name):
    """
    Cria e envia uma campanha de SMS.
    
    :param api_proxy: Instância do PySendPulse
    :param sender_name: Nome do remetente (deve estar cadastrado no SendPulse)
    :param addressbook_id: ID do addressbook com os destinatários
    :param message_text: Texto da mensagem a ser enviada
    :param campaign_name: Nome da campanha
    """
    try:
        response = api_proxy.sms_add_campaign_by_addressbook_id(sender_name, addressbook_id, message_text, campaign_name)
        print(f"Campanha criada e enviada com sucesso: {response}")
    except Exception as e:
        print(f"Erro ao criar/enviar campanha: {e}")

def main():
    
    # Insira suas credenciais aqui
    REST_API_ID = '40133a190b2ea23df5e111f666881802'
    REST_API_SECRET = '005fb5c2663d84fe030b5692f2a8b8bc'
    
    # Inicializa a API do SendPulse
    api_proxy = initialize_sendpulse(REST_API_ID, REST_API_SECRET)
    
    # ID do Addressbook (substitua pelo seu ID)
    ADDRESSBOOK_ID = 0
    
    # Números de telefone a serem adicionados
    phone_numbers = [
        '5586999214555',
        '5586988927212',
        '5586994661837'
    ]
    
    # Adiciona os números ao addressbook
    add_phone_numbers(api_proxy, ADDRESSBOOK_ID, phone_numbers)
    
    # Detalhes da campanha SMS
    SENDER_NAME = 'SeuNome'  # Deve estar cadastrado no SendPulse
    MESSAGE_TEXT = 'Olá! Esta é uma mensagem de teste enviada via SendPulse API.'
    CAMPAIGN_NAME = 'Campanha de Teste API'
    
    # Cria e envia a campanha SMS
    create_and_send_sms_campaign(api_proxy, SENDER_NAME, ADDRESSBOOK_ID, MESSAGE_TEXT, CAMPAIGN_NAME)

if __name__ == "__main__":
    main()
