# importando a Biblioteca pytube
from pytube import YouTube
# importando a função argv da Biblioteca sys  
from sys import argv    

# definindo uma variável pra receber os Links pra download e
# definindo um objeto YouTube
link = argv[1]  
yt = YouTube(link)  

# Fazendo o Terminal mostrar o Nome e a Quantidade de Views
# do vídeo em questão
print("Title: ", yt.title)
print("Views: ", yt.views)

# Baixando o Vídeo na maior resolução possível e salvando na pasta 
# Downloaded Videos
yd = yt.streams.get_highest_resolution()
yd.download('./Downloaded Videos')

# Sinal do Fim do Download
print("Download Complete")