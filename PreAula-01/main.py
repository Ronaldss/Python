import pandas as pd
from twilio.rest import Client

## Twilio - autenticando na minha conta
# Your Account SID from twilio.com/console
account_sid = "ACcbf53e982a1389a388280492041d7f93"
# Your Auth Token from twilio.com/console
auth_token  = "226fb98fc1c5a29e8d862dc0047dc1ba"
client = Client(account_sid, auth_token)


## Passo a passo de solução
# abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():        # .any()  para considerar o 'conteudo/valor' de dentro da coluna.
        # vendedor = tabela_vendas.loc[linha, coluna]
        # O .loc vai retornar uma tabela, isso é coisa do pandas.
        # então para conseguir o valor de dentro da celula usa .value[0]
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês {mes}. Alguem bateu a meta! Vendedor: {vendedor}, Vendas: {vendas}')
        ## Twilio - enviar msg
        message = client.messages.create(
            to="+512121212121",
            from_="+12121212121212",
            body="Hi!")
        print(message.sid)




# Para cada arquivo:
# Verificar se algum valor na coluna VENDAS é maior que 55.000
# Se for maior que 55.000, enviar SMS com o nome, mês e vendas dovendedor.
# Caso não seja que 55.000, nao fazer nada.