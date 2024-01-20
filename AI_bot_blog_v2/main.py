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
def get_trending_topics():
    # Récupère les tendances pour un lieu spécifique (ici, id 1 pour le monde entier)
    trends = api.get_place_trends(id=1)
    trending_topics = [trend['name'] for trend in trends[0]['trends']]
    return trending_topics[:5]  # Retourne les 5 premiers sujets tendance

def generate_article(topic):
    prompt = f"Écris un article engageant et détaillé sur {topic}."
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Utilise un modèle de complétion standard
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'appel à l'API OpenAI: {e}")

# Utilisation de la fonction pour récupérer les tendances et générer des articles
trending_topics = get_trending_topics()
for topic in trending_topics:
    print(f"Génération d'un article sur: {topic}")
    article = generate_article(topic)
    print(article)
