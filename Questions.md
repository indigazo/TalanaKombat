# Preguntas generales 

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 
De ser posible, que quede solo un commit con los cambios. 

- Si aun no he echo push:
  - simplemente puedo escribir git revert <commit> con la Id del commit, si no la recuerdo de memoria o la tengo a mano
  puedo utilizar git log para obtener la lista de commits y desde ahi obtener el commit que busco

  - luego de revertir el commit , puedo usar add <archivo> para agregar lo que se me pudo haber olvidado

  - ahora puedo usar git commit -m "mensaje" para luego git push   

- Si ya pushie 
    - es mas "peligroso" pero se puede usando git reset --hard <commit> (usando log antes incluso) para localmente revertir a un commit anterior al que quiero revertir
    - limpio el historial git clean -f -d 
    - git push -u origin +master con (+) para forzar el fix 
 

2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado? 

He trabajado con git siempre, utilizando como interfaz gogs (que utiliza mi empresa actual), el flujo de trabajo que he utilizado es el de pushear en ciertas branches para que un contenedor
automaticamente generara un deploy de aplicacion. Estoy acostumbrado al control de versiones por git 


3.¿Cuál ha sido la situación más compleja que has tenido con esto? 

En un proyecto tuve que trabajar con tecnologia algo antigua (silverlight) pero utilizando el control de versiones, ademas este era un proyecto enorme y antiguo con cientos de miles de lineas de codigo. Por lo tanto los merge solian ser caoticos y peligrosos (ya que en la empresa a la que estaba ayudando no tenia un control real de quien pusheaba cuando a que branch). Esta experiencia me ayudo a conocer mejor la interfaz de git tanto en linea de comandos como a traves de wizards (como vscode o github mismo) 


4. ¿Qué experiencia has tenido con los microservicios? 

No mucha desarrollandolos o usando ese metodos, pero si he utilizado (en baja medida) contenedores para correr solo ciertas tareas en la nube.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué? 

AWS debido a que es el que conozco como utilizar, ademas lo considero rapido y confiable. Admemas para Python al menos , comunicarse con buckets por s3 es simple.
