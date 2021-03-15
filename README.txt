ANTES DE COMEÇAR:

+  É necessário fotos dos vários participantes em ângulos variados
   (Observar as fotos de exemplo na pasta img-altered)

-+ Não é necessário ter 20 fotos, 10 fotos por indivíduo é suficiente, mas quanto mais fotos melhor.

-+ TODAS as fotos deverão ter as mesmas dimensões, as dos exemplos na pasta 
   img-altered são de 180 x 135

-+ TODAS as fotos deverão ser convertidas para escala de cinza, o script
   image_converter faz isso para vocês, basta colocar todas as imagens na
   pasta img-original e executar o script, ele gerará as fotos em escala
   de cinza na pasta img-altered

-+ O script utiliza os nomes das imagens como rótulo, ou seja, é necessário
   que o nome da foto seja o nome da pessoa, exemplo: joao1.jpg, joao2.jpg, etc.
   Ao executar o image_converter ele gerará as fotos em escala de cinza e adicionará
   um 'a' de alterada a frente de cada foto, exemplo: joao1a.jpg, joao2a.jpg, etc.

INSTRUÇÕES PARA COMEÇAR:

1 - Remover ou recortar as fotos de exemplo da pasta img-altered
2 - Adicionar as fotos na pasta img-original e executar o script image_converter.py
3 - Criar ambiente virtual na raiz da pasta do projeto (utilizando: 'python -m venv .')
4 - Instalar os seguintes pacotes: (utilizando: 'python -m pip install -U nomedopacote')
4.1 - scikit-learn
4.2 - pandas
4.3 - pillow
5 - Abrir o arquivo 'run.py' e alterar a linha 14 para as dimensões das imagens
    (os valores hardcoded no script correspondem aos valores das imagens de teste que
     que estão no zip)
6 - Executar o script run.py
7 - Coletar o desempenho do sistema impresso no terminal