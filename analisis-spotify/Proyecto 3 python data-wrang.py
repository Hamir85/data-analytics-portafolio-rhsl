#!/usr/bin/env python
# coding: utf-8

# # ¡Hola  !🙋🏻‍♂️
# 
# Te escribe Lisandro Saez, soy revisor de código en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberías hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma (no te preocupes, no es obligatorio):
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión.
# </div>
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[1]:


# Importar pandas
import pandas as pd 


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[2]:


# Leer el archivo y almacenarlo en df
df = pd.read_csv('/datasets/music_project_en.csv')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Bien hecho! Siempre es importante que pasemos el set de datos que estamos usando a `DataFrame`!</div>
# 

# Muestra las 10 primeras filas de la tabla:

# In[3]:


# Obtener las 10 primeras filas de la tabla df
print(df.head(10))


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[4]:


# Obtener la información general sobre nuestros datos
print(df.info())


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Tenemos valores ausentes y el tipo de datos en  la variable "time"`.
# 
# 
# 

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`R= Tenemos una base de datos con la información de las canciones reproducidas en dos ciudades. Buestros datos son de tipo no numericos, que nos proporciona la información de cada canción reproducida. Cada que se reproduce una canción, se guardan los datos correspondientes en nuestras columnas.
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`
# R= Si contamos con la mayoria de los datos para poder tener un buen analisis.
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# R= Si, contamos con 3 columnas con valores ausentes(Track, artist y genre), todos los datos son de timpo objet y vienen los nombres de las columnas con espación y letras mayusculas y minusculas. 

# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Gran trabajo! Es importante que antes de encarar cualquier problema que queramos resolver con Python, nos paremos a pensar bien en qué consisten los datos con los que vamos a trabajar!
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[5]:


# Muestra los nombres de las columnas
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[6]:


new_col = []
for col in df:
    lower = col.lower()
    new_col.append(lower)

df.columns = new_col
print (df.columns)

   


# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[7]:


new_col_espa = []
for col_esp in df:
    strip = col_esp.strip()
    new_col_espa.append(strip)
    # Bucle en los encabezados eliminando los espacios
df.columns = new_col_espa
print (df.columns)


# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[8]:


new_col_us = []
for col_us in df:
    replace = col_us.replace('userid','user_id')
    new_col_us.append(replace)# Cambiar el nombre de la columna "userid"
df.columns = new_col_us
print (df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[9]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[10]:


df.isna().sum()# Calcular el número de valores ausentes


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[11]:


rem_columns =df[['track','artist','genre']]
for colu in rem_columns:
    colu = rem_columns.fillna('unknown')
    

df[['track','artist','genre']]= colu
print(df.info)# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'


# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[12]:


# Contar valores ausentes
df.isna().sum()


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por haber eliminado los NaNs! Es una parte fundamental del análisis de datos!
# </div>
# 

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[13]:


# Contar duplicados explícitos
df.duplicated().sum()


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[14]:


# Eliminar duplicados explícitos
df= df.drop_duplicates()


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[15]:


df.duplicated().sum()# Comprobar de nuevo si hay duplicados


# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[16]:


df['genre'].sort_values().unique()# Inspeccionar los nombres de géneros únicos


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[47]:


def replace_wrong_genres(df,wrong_genres,correct_genre):
    for colum in wrong_genres:
        df['genre'].replace(colum,correct_genre,inplace = True)
        

# Función para reemplazar duplicados implícitos


# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[48]:


replace_wrong_genres(df,['hip','hop','hip-hop'],'hiphop')# Eliminar duplicados implícitos


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[50]:


# Comprobación de duplicados implícitos
print(df['genre'].sort_values().unique())


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Te felicito por haber eliminado los duplicados! Es una parte fundamental del análisis de datos!
# </div>
# 

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`
# Realizamos las correcciónes de los nombres de las columnas en la primera parte. Tambien nos dimos cuenta que había valores ausentes o nulos y porocedimos a llenarlos con "unknown" para los valores que no aparcen en el dataframe. Posteriormente nos dimos cuenta que la base de datos contenia erres en los nombres de del genero hiphop y se reemplazaron todos homogeneamente para su analisis.

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[51]:


df.groupby('city')['track'].count()
# Contar las canciones reproducidas en cada ciudad


# `Comenta tus observaciones aquí` La ciudad de Springfield reproduce más del doble de canciones que Shelbyville.

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[62]:


df.groupby('day')['track'].count()# Calcular las canciones reproducidas en cada uno de los tres días


# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Gran trabajo utilizando `groupby()`!</div>
# 
# 

# `Comenta tus observaciones aquí`Nos dimos cuenta que el día que se reproduce más musica en el día Viernes. 

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[65]:


def number_tracks(df, city, day ):
# Declara la función number_tracks() con dos parámetros: day= y city=.    
    df_day = df[df['day'] == day]
# Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=
    df_city = df_day[df_day['city'] == city ]
    # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=
    result = df_city['user_id'].count()
    # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()
    return result  # Devolve el número de valores de la columna 'user_id'


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[66]:


number_tracks(df,'Springfield','Monday')# El número de canciones reproducidas en Springfield el lunes


# In[67]:


# El número de canciones reproducidas en Shelbyville el lunes
number_tracks(df,'Shelbyville','Monday')


# In[68]:


# El número de canciones reproducidas en Springfield el miércoles
number_tracks(df,'Springfield','Wednesday')


# In[69]:


# El número de canciones reproducidas en Shelbyville el miércoles
number_tracks(df,'Shelbyville','Wednesday')


# In[70]:


# El número de canciones reproducidas en Springfield el viernes
number_tracks(df,'Springfield','Friday')


# In[72]:


# El número de canciones reproducidas en Shelbyville el viernes
number_tracks(df,'Shelbyville','Friday')


# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.` Se acepta la hipotesis, difiere tanto el día como la ciudad la cantidad de canciones reporducidas. 

# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Grandísimo trabajo con el análisis de hipótesis. Felicitaciones!</div>
# 

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`
# Dado que hay el doble de ususarios que escuchan musica en Springfield, tenemos que el viernes y lunes son los días que más canciones escuchan. El Mircoles podemos ver como en Shelbyville hay un incremento en las reproducciónes a comparación de Springfield que es el día que menos canciones escuchan.

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Felicitaciones por el excelente trabajo que hiciste durante todo el sprint!</div>
# 
# 
# 

# [Volver a Contenidos](#back)
