# Pour la CI/CD, configurez ces secrets dans votre dépôt GitHub :
# - SFTP_HOST : adresse du serveur SFTP
# - SFTP_USERNAME : nom d'utilisateur SFTP
# - SFTP_PASSWORD : mot de passe SFTP
# - SFTP_PORT : port SFTP (par défaut 22)
# - SFTP_DAGS_PATH : chemin distant où copier les DAGs

# Les tests sont lancés avec pytest et le lint avec ruff.
# Les DAGs du dossier src/ sont copiés sur le serveur SFTP après validation des tests.
