Descripcion
Motor de calculo vectorial en Python que resuelve y visualiza tres problemas del parcial final de Calculo Multivariado usando integrales de linea, el Teorema de Green, campos conservativos y el Teorema de Stokes.

Estructura del repositorio
campos-vectoriales/
├── README.md
├── requirements.txt
├── src/
│ ├── vector_engine.py
│ └── visualizacion.py
├── tests/
│ └── test_engine.py
├── output/
│ ├── fig_green.png
│ ├── fig_potencial.png
│ └── fig_stokes.png
└── docs/
└── informe.pdf

Requisitos previos

Python 3.10 o superior
pip actualizado
Para ver el informe PDF en VS Code instalar la extension: vscode-pdf

Instalacion
bashgit clone https://github.com/johanqu/campos-vectoriales.git
cd parcialCalculo
pip install -r requirements.txt

Uso
Ejecutar el motor de calculo:
bashpython src/vector_engine.py
Generar las visualizaciones:
bashpython src/visualizacion.py
Correr las pruebas unitarias:
bashpytest tests/test_engine.py -v

Resultados analiticos vs numericos
EjercicioAnaliticoNumericoError1 - Green24pi = 75.39822475.3982240.0000%2 - Conservativo3.0000 J3.000000 J0.0000%3 - Stokes4pi = 12.56637112.5663710.0000%
Todos los errores son menores al 1% requerido.

Johan Quintero
