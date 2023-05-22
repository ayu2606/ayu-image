import webbrowser
import openai
import os
openai.api_key = "Your Token"

l = """
░█████╗░██╗  ██╗███╗░░░███╗░█████╗░░██████╗░███████╗
██╔══██╗██║  ██║████╗░████║██╔══██╗██╔════╝░██╔════╝
███████║██║  ██║██╔████╔██║███████║██║░░██╗░█████╗░░
██╔══██║██║  ██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░
██║░░██║██║  ██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗
╚═╝░░╚═╝╚═╝  ╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝

                                        █▄▄ █▄█   ▄▀█ █▄█ █░█ █▀ █░█
                                        █▄█ ░█░   █▀█ ░█░ █▄█ ▄█ █▀█                           

\n"""

while True:
    print(l)
    p = input("Enter new prompt: ")
    os.system("cls")
    response = openai.Image.create(
    prompt=f"{p}",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    if 'exit' in p or 'quit' in p:
        break
    webbrowser.open(image_url)
