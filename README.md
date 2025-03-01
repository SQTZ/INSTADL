# Instagram Profile Downloader

Ce script Python permet de télécharger automatiquement toutes les photos et vidéos d'un profil Instagram.

## Prérequis

- Python 3.6 ou supérieur
- Les packages Python suivants :
  - instaloader
  - fake-useragent

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers
2. Installez les dépendances requises :
```bash
pip install instaloader fake-useragent
```

## Configuration

1. Ouvrez le fichier `instagram_downloader.py`
2. Modifiez les variables suivantes avec vos identifiants Instagram :
```python
INSTAGRAM_LOGIN = "YOUR_USERNAME"  # Votre nom d'utilisateur Instagram
INSTAGRAM_PASSWORD = "YOUR_PASSWORD"  # Votre mot de passe Instagram
```

## Utilisation

1. Exécutez le script :
```bash
python instagram_downloader.py
```

2. Lorsque le script vous le demande, entrez l'URL du profil Instagram dont vous souhaitez télécharger le contenu.
   Exemple : `https://www.instagram.com/username`

3. Le script va :
   - Se connecter à Instagram avec vos identifiants
   - Créer un dossier `data` s'il n'existe pas
   - Télécharger toutes les photos et vidéos du profil dans ce dossier

## Fonctionnalités

- Téléchargement de photos et vidéos
- Gestion automatique des timeouts et des erreurs
- Délais aléatoires entre les téléchargements pour éviter les blocages
- Utilisation d'User-Agents aléatoires
- Sauvegarde des métadonnées

## Notes importantes

- Utilisez ce script de manière responsable et dans le respect des conditions d'utilisation d'Instagram. Je me tiendrais aucunement responsable de l'acte commis.
- Un téléchargement trop intensif peut entraîner des limitations temporaires de votre compte
- Le script inclut des délais aléatoires pour minimiser les risques de blocage

## Structure des fichiers

```
.
├── instagram_downloader.py
├── README.md
└── data/
    └── [nom_utilisateur]/
        ├── photos
        └── vidéos
```

## Dépannage

Si vous rencontrez des erreurs :
1. Vérifiez vos identifiants Instagram
2. Assurez-vous que le profil cible est accessible
3. Attendez quelques minutes si vous recevez des erreurs de limitation
4. Vérifiez votre connexion internet
