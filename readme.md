# Equipe

Antonio Gabriel Magalhães Alves - 496218

Thiago da Costa Gadelha - 499284

# Como executar

Baixar dependencias:

    python3 -m pip install -r requirements

Executar a jogo:

    python3 src/main.py

# Como Jogar

1. Na tela de apresentação basta apertar a tecla enter para iniciar o jogo.

2. Controles direcionais esquedo e direito para girar a nave. Space para atirar

3. Jogo acaba quando for atingido por um meteoro

# Requisitos

## Tela apresentação:
- Algoritmo elipse: Usado para desenhar os "O"s de meteoros
- Algoritmo círculo: Usado para desenhar os planetas em azul
-Algoritmo FloodFill: Usado para preeencher os circulos e elipses.
- Algoritmo de Rasterização de reta: Usado para desenhar as estrelas e algumas letras de "meteoros"

## Jogo:
- Polígonos preenchidos com gradientes de cores (definidas por vértice) e texturas coloridas: Nave e meteoro
- Translação: Meteoro e Tiro 
- Rotação: Nave
- Deve ser utilizada pelo menos uma janela, e pelo menos uma viewport: As transformadas de mundo são transformadas para coordenada de dispositivo a partir de uma viewport
- A qual deve apresentar transformações de translação e escala (zoom): Quando o meteoro atinge a nave, é feito uma 
escala e uma translação a partir da viewport.