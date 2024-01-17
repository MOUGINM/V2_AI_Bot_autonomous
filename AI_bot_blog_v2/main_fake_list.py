import tweepy
import openai
from key import *
# --- Paramètres Twitter API ---
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
openai.api_key = openai_key

# --- Authentification Twitter API ---
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# --- Récupération des Tendances Twitter ---
faux_tendances_twitter = [
    "Intelligence Artificielle",
    "Nouvelles Technologies",
    "Développement Durable",
    "Économie Numérique",
    "Santé et Innovation",
    "Espace et Exploration",
    "Changement Climatique",
    "Cryptomonnaies",
    "Réalité Virtuelle",
    "Jeux Olympiques"
]

def generate_article(topic):
    prompt = f"Écris un article détaillé et engageant sur {topic}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Utilise un modèle de chat
            messages=[{"role": "system", "content": "Vous êtes un assistant très compétent."}, 
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'appel à l'API OpenAI: {e}")

# Exemple d'utilisation
topics = ["Intelligence Artificielle", "Nouvelles Technologies", "Développement Durable", "Économie Numérique", "Santé et Innovation"]
for topic in topics:
    print(f"Génération d'un article sur: {topic}")
    article = generate_article(topic)
    print(article)