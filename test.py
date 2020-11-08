import acoustid

API_CLAVE = 'IIaL0o3GfC'
API_USUARIO = 'Tdbm29rwWq'
ARCHIVO = 'test4.mp3'
URL = 'https://rhythm-practice.database.windows.net'

# Se establece el servidor de base de datos para la plataforma de Rhythm Practice
# donde se almacenarán los archivos de audio
# acoustid.set_base_url(URL)

# Busca entre todas las huellas digitales dentro de la base de datos que exista
# el archivo, si encuentra posibles resultados devuelve tuplas con información
# de dichos resultados
'''resultados = acoustid.match(API_CLAVE, ARCHIVO)

for coincidencia, recording_id, titulo, artista in resultados:
    print(f'Artista: {artista} \tCanción/título: {titulo}')
    print(f'Coincidencia: {int(coincidencia * 100)}%')'''

# Devuelve la huella digital y la duración del archivo utilizando la línea de 
# comandos de fpcalc
duracion, fp = acoustid.fingerprint_file(path=ARCHIVO, force_fpcalc=True)
print(f'Duración: {duracion} seg')
print(f'Huella digital: {fp}')

# Envía una nueva huella digital a la base de datos
'''nueva_fp = {'fingerprint':fp, 'duration':duracion, 'track':'Move Your Body', 
    'artist':'Sia', 'album':'This is acting'}

respuesta = acoustid.submit(apikey=API_CLAVE, userkey=API_USUARIO, data=nueva_fp)

print(respuesta)'''

# Estado del envío de la huella digital a la base de datos
'''estado = acoustid.get_submission_status(apikey=API_CLAVE, submission_id=respuesta['submissions'][0]['id'])

print(estado)'''
