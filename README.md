# Prueba Talana Kombat JRPG
Proyecto no tiene dependencias de librerias. Python 3.9

Por defecto corre el juego 1 (de ejemplo) para cambiar el archivo editar archivo main
y guardar los archivos json en la carpeta json_files

```python 
data = read_json_file(ROOT_JSON_PATH + 'your_filename_here.json')
```

el game loop principal puede correr en modo rapido o lento (con pausas)

```python 
game_loop(starting_player, second_player, False) # Modo normal con pausas
game_loop(starting_player, second_player, True) # Modo rapido
```

para ejecutar simplemente

```sh
python main.py
```