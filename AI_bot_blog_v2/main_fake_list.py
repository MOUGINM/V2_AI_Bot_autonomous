import openai
from key import *
openai.api_key = openai_key

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
