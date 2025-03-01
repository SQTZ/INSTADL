import instaloader
import os
import re
import time
import random
from fake_useragent import UserAgent

# Vos identifiants Instagram
INSTAGRAM_LOGIN = "YOUR_USERNAME"  # Remplacez par votre nom d'utilisateur
INSTAGRAM_PASSWORD = "YOUR_PASSWORD"  # Remplacez par votre mot de passe

def extract_username_from_url(url):
    # Extraire le nom d'utilisateur de l'URL Instagram
    pattern = r'instagram.com/([^/?]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("URL Instagram invalide")

def handle_private_profile(L, profile):
    """Gère l'accès aux profils privés"""
    if profile.is_private:
        print(f"Le profil {profile.username} est privé.")
        
        # Vérifier si on suit déjà le compte
        if profile.followed_by_viewer:
            print("Vous suivez déjà ce compte, téléchargement possible.")
            return True
            
        print("Désolé, ce compte est privé et vous ne le suivez pas.")
        print("Pour des raisons de sécurité et de respect de la vie privée,")
        print("il n'est pas possible de télécharger le contenu d'un compte privé sans le suivre.")
        return False
    return True

def download_instagram_profile(profile_url, output_dir="data"):
    try:
        # Extraire le nom d'utilisateur de l'URL
        username = extract_username_from_url(profile_url)
        
        # Créer un User-Agent aléatoire
        ua = UserAgent()
        
        # Configuration avancée de l'instance Instaloader
        L = instaloader.Instaloader(
            download_videos=True,            # Activer le téléchargement des vidéos
            download_video_thumbnails=True,  # Télécharger les miniatures des vidéos
            download_geotags=False,
            download_comments=False,
            save_metadata=True,              # Nécessaire pour certaines vidéos
            post_metadata_txt_pattern='',
            max_connection_attempts=5,
            user_agent=ua.random,
            request_timeout=30.0             # Augmenter le timeout pour les vidéos
        )

        # Créer le dossier data s'il n'existe pas
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Définir le dossier de sortie
        L.dirname_pattern = output_dir + '/{target}'
        
        # Se connecter avec vos identifiants
        print("Connexion à Instagram...")
        L.login(INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD)
        
        # Attendre un peu après la connexion
        time.sleep(3)
        
        print("Connexion réussie!")
        
        # Télécharger le profil avec plus de délai
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Vérifier si le profil est privé et le gérer
        if not handle_private_profile(L, profile):
            print("Impossible de télécharger le contenu d'un profil privé sans le suivre.")
            return
        
        print(f"Début du téléchargement des photos et vidéos de {username}...")
        
        # Télécharger toutes les publications avec un délai
        for post in profile.get_posts():
            try:
                # Attendre plus longtemps entre chaque téléchargement
                time.sleep(random.uniform(4, 7))
                L.download_post(post, target=profile.username)
                if post.is_video:
                    print(f"Vidéo téléchargée : {post.url}")
                else:
                    print(f"Photo téléchargée : {post.url}")
            except Exception as e:
                print(f"Erreur lors du téléchargement : {e}")
                time.sleep(10)  # Attendre plus longtemps en cas d'erreur
                
        print("Téléchargement terminé !")
        
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    # Demander l'URL du profil
    profile_url = input("Entrez l'URL du profil Instagram (ex: https://www.instagram.com/username) : ")
    
    # Lancer le téléchargement dans le dossier data
    download_instagram_profile(profile_url) 