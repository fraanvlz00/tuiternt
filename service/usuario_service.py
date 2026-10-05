from config_redis import config
import json

def crear_usuario(nombre_usuario, correo_electronico, edad, ciudad):
    usuario_id = config.incr("usuario:id")
    clave_usuario = f"usuario:{usuario_id}"
    config.hset(
        clave_usuario,
        mapping={
            "nombre_usuario": nombre_usuario,
            "correo_electronico": correo_electronico,
            "edad": edad,
            "ciudad": ciudad
        }
    )

    print("Usuario creado correctamente")

def siguiendo_usuario(usuario_id, usuario_seguido_id):
    clave_siguiendo = f"usuario:{usuario_id}:siguiendo"

    config.sadd(
        clave_siguiendo,
        usuario_seguido_id
    )

    print(f"Usuario {usuario_id} ahora sigue a {usuario_seguido_id}")

def eliminar_siguiendo_usuario(usuario_id, usuario_seguido_id):
    clave_siguiendo = f"usuario:{usuario_id}:siguiendo"

    config.srem(
        clave_siguiendo,
        usuario_seguido_id
    )

    print(f"Usuario {usuario_id} dejo de seguir a {usuario_seguido_id}")

def listar_tweets_siguiendo(usuario_id):
    clave_siguiendo = f"usuario:{usuario_id}:siguiendo"
    usuarios_seguidos = config.smembers(clave_siguiendo)
    tweets_siguiendo = []

    for siguiendo_id in usuarios_seguidos:
        clave_tweets_siguiendo = f"usuario:{siguiendo_id}:tweets"
        tweets = config.lrange(clave_tweets_siguiendo, 0, -1)

        for tweet_json in tweets:
            tweet = json.loads(tweet_json)
            tweet["usuario_id"] = siguiendo_id
            tweets_siguiendo.append(tweet)

    tweets_siguiendo.sort(
        key=lambda tweet: tweet["fecha"]
    )
    return tweets_siguiendo

def listar_tweets_propios(usuario_id):
    clave_tweets_propios = f"usuario:{usuario_id}:tweets"
    tweets_json = config.lrange(clave_tweets_propios, 0, -1)
    tweets_propios = []

    for tweet_json in tweets_json:
        tweet = json.loads(tweet_json)
        tweets_propios.append(tweet)

    tweets_propios.sort(
        key=lambda tweet: tweet["fecha"]
    )

    for tweet in tweets_propios:
        print(
            f'ID: {tweet["id"]} | '
            f'{tweet["mensaje"]} | '
            f'{tweet["fecha"]}'
        )

    return tweets_propios

def obtener_usuario_por_nombre(nombre_usuario):
    for clave in config.scan_iter("usuario:*"):

        if config.type(clave) != "hash":
            continue

        usuario = config.hgetall(clave)

        if usuario.get("nombre_usuario") == nombre_usuario:
            usuario_id = clave.split(":")[1]
            usuario["id"] = usuario_id
            return usuario

    return None


def crear_usuario(nombre_usuario, correo_electronico, edad, ciudad):
    usuario_id = config.incr("usuario:id")

    clave_usuario = f"usuario:{usuario_id}"

    config.hset(
        clave_usuario,
        mapping={
            "nombre_usuario": nombre_usuario,
            "correo_electronico": correo_electronico,
            "edad": edad,
            "ciudad": ciudad
        }
    )

    usuario = config.hgetall(clave_usuario)
    usuario["id"] = str(usuario_id)

    return usuario


def listar_usuarios():
    usuarios = []

    for clave in config.scan_iter("usuario:*"):

        if config.type(clave) != "hash":
            continue

        usuario = config.hgetall(clave)

        usuario_id = clave.split(":")[1]

        usuario["id"] = usuario_id

        usuarios.append(usuario)

    return usuarios


def esta_siguiendo(usuario_id, usuario_seguido_id):
    clave_siguiendo = f"usuario:{usuario_id}:siguiendo"

    return config.sismember(
        clave_siguiendo,
        usuario_seguido_id
    )


