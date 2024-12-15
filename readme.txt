En este documento se explica brevemente qué es cada fichero:

    - scripts: directorio que contiene distintos scripts de bash y python para el preprocesado de los datos, así como
        - filter.py: filtra las secuencias de colocación.
        - oversampling: realiza el oversampling sobre la clase negativa.
        - preclasificado.sh: etiqueta todas las secuencias como positivas.
        - process_ball_anotations: procesa las anotaciones del balón del segundo dataset.
        - split_lines: procesa el resutado de process_bal_anotations para adaptar el formato a YOLO
        - split_videos: separa las sencuencias en directorios por clases.
        - YOLO_2class: contiene el modelo para 2 clases, así como los scripts para entrenarlo.
        - YOLO_3class: contiene el modelo para 3 clases, así como los scripts para entrenarlo.
        - YOLO_detection: contiene el modelo de deteccción de balón, así como los scripts para entrenarlo

    - data: directorio con las secuencias anotadas a mano.

Todos los scripts asumen la presencia de los datos de entrenamiento en un su mismo directorio.
