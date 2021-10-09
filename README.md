# Discord Bot

Esse bot do discord está sendo feito com o intuito de aprendizado e futuramente uso em servidor próprio.


## Como usar
**Requisitos:** 

 - Python 3.9.7 (versão que estou utilizando, talvez funcione em versões um pouco mais baixas)
 - Conta no Discord (caso não tenha, crie uma)
 
 **Configurando a aplicação e o bot:**
 Recomendo que siga o tutorial do [Real Python](https://realpython.com/how-to-make-a-discord-bot-python/) para fazer a configuração da aplicação e do bot.
 
 **Após configurar o bot e a aplicação você deve ativar as seguintes configurações no seu bot:**
 
![](https://lh3.googleusercontent.com/QzUxKV_uuEBX9_1KvErZCcKTModzJxcBfD5JsoEwpKBjPteiZpMmEi1i24aZ_f4nzK_u5fMIjOyrLi6fQtIOtvl2IwkoQkY5cePh5HyL5XibOPjCvgftWtixVGpmB8S-Nd5UNkpx6dCgL99iODHdwQY7sH8NGQhL43rgPbV4Qvb7ns53k4Z-Kdv7vv2U9_38o2BHk9lL_q7uGw1RYaFd5Jfi_bOE2w1OBH-mWRi_Ge-zHFz4HEEjenBwr9YKWYbKrevbx71ysRc4aULermDJbbNQLYm7nNZ2WwqWR27LrSWKTmsvAXK12E-HgSXx6UEmN-dbzmAlEOFzL9AaDxJcKSrCeYTpd35E_5Tvr7KTQ70YHVjbekaaZjhRFdOd3ZWMfFQ332LFDXk4BbTWjH1ZnaM7lKlDaKAYiJ_BtOhr5FUxFhExVL3yaN-Hi1u_nE37cOvzGRJFRYg8AWk3Fii3v2ioxfVkLLJ1EEpQUuUNaXk6BTWEeAeIqydx_pg8lyCFX3tfrI7SswHtNmDwscfpzJtiAhrLed1NN65Mj90lrkL80JUELX3Elg3kX4P0fp3sWbX6KCugpX_Q8v4W-FZ81Fi9rhhUWU0BwPBfHuMCN6h7L3G02lEUqOUZLR7NzLHDqzZY7VvTg3rQHk512YqU94RWebg1p-5iwEaZiuA_7tLSMDaLM1KES6tFPOjQPulV_my1BEl8cFTcla00JJHcccIi=w1417-h428-no)

**Configurando o ambiente**

Clone o repositório:

``` git clone https://github.com/fernandogfleite/discord-bot.git```

Se tiver o git flow instalado ([como instalar o git flow](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Gitflow-Windows-Install-Git-Flow-Installation)), inicialize ele:

```git flow init```

Vá até o terminal de comando e crie uma virtualenv:

```python -m venv venv```

Após isso ative a sua virtualenv:
 - Linux: ```source venv/bin/activate```
 - Windows: ```.\venv\Scripts\activate.bat```

Após ativar a sua virtualenv, instale os requirements.txt:
```pip install -r requirements.txt```

Crie  um arquivo .env com os dados necessários:

    DISCORD_TOKEN=

Após isso a aplicação está pronta para rodar:

```python bot.py```
