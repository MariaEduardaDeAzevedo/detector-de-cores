# Detector de cores
Programa com Python e OpenCV que identifica e mostra cores em imagens e vídeos.

### Detalhes
- Ao rodar, o programa abre a webcam e consegue identificar as cores azul, amarelo e verde, pois são as únicas máscaras que estão configuradas até o momento.

- No arquivo mask.py existe um script feito para configuração de máscaras. Quando executado, ele também abrirá a webcam e, com a caixa de botões 
de trilha, você poderá encontrar uma máscara para uma cor específica. Utilize objetos para capturar as cores, ou passe um caminho para um vídeo no 
método VideoCapture, se for de sua preferência.

- As máscaras configuradas foram postas em um arquivo JSON, localizado na pasta files, que é importado dentro no script principal, main.py.

- Também existem algumas imagens que podem ser utilizadas para configurar as máscaras.

#### Executando o Programa

Para executar o programa, você deve clonar este repositório, instalar as dependências e executar o arquivo principal (main):

```bash
# Clonar o repositório.
$ git clone https://github.com/MariaEduardaDeAzevedo/detector-de-cores.git
$ cd detector-de-cores

# Opcional: Crie e ative um ambiente Python isolado para a aplicação.
$ pip install virtualenv # Com --user se não tiver permissões de administrador.
$ virtualenv -p python3 venv
$ source venv/bin/activate

# Instalar as dependências e executar o programa.
$ python -m pip install -r requirements.txt
$ python detector_de_cores/main.py
```

#### Para contribuir adicionando máscaras, olhe o arquivo CONTRIBUTING.md
