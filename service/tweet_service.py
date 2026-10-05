from config_redis import config
from datetime import datetime
import json

def publicar_tweet(usuario_id, mensaje):
    fecha = datetime.now().isoformat()
    tweet_id = config.incr("tweet:id")
    clave_tweet = f"usuario:{usuario_id}:tweets"
    

    tweet = {
        "id": tweet_id,
        "mensaje": mensaje,
        "fecha": fecha
    }

    config.rpush(
        clave_tweet,
        json.dumps(tweet)
    )

    print("tuit creado")


def eliminar_tweet(usuario_id, tweet_id):
    clave_tweet = f"usuario:{usuario_id}:tweets"
    llamar_tweets = config.lrange(clave_tweet, 0, -1)

    for tweet_json in llamar_tweets:
        tweet = json.loads(tweet_json)

        if tweet["id"] == tweet_id:
            config.lrem(clave_tweet, 1, tweet_json)
            return print("tuit eliminado")

    print("tuit no encontrado")
 
