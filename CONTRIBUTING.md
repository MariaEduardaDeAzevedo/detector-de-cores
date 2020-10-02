## Adicionando máscaras

Na pasta files existe um arquivo mask.json, no qual estão configuradas algumas máscaras para serem utilizadas no programa principal. 
Para adicionar uma nova máscara de cor, siga os passos:
1. Dê um fork nesse repositório e o clone
2. Rode o script mask.py. Ao fazê-lo, aparecerão algumas telas que capturam a imagem de sua webcam e também um painel de botões de arrastar.
3. Pegue um objeto da cor que você deseja criar a máscara e o mostre para a câmera. Para calibrar a cor, mova os botões até que apenas o objeto da cor desejada fique em evidência na tela.
4. Feito isso, adicione os valores da mascara ao arquivo mask.json, no formato do seguinte objeto:
  ```
  "nome_da_cor": {
        "min" : [h, s, v], //valores HSV minimos (indicados por "Min" no painel)
        "max" : [h, s, v]  //valores HSV minimos (indicados por "Max" no painel)
    },
  ```
