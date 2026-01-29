# GitLab CI/CD Component Template : Airflow DAG Deployment

Ce composant CI/CD permet d'automatiser la qualité et le déploiement de DAGs Airflow via SFTP, avec gestion d'environnements (dev, staging, production) selon le workflow GitFlow.

## Utilisation

Dans votre `.gitlab-ci.yml` principal, incluez le composant :

```yaml
include:
  - local: 'template/component.yml'
```

## Variables à définir dans votre projet
- `SFTP_HOST` : hôte SFTP
- `SFTP_USERNAME` : utilisateur SFTP
- `SFTP_PASSWORD` : mot de passe SFTP
- `SFTP_PORT` : port SFTP
- `SFTP_DAGS_PATH` : chemin distant pour les DAGs
- `GITLAB_TOKEN` : token d'API GitLab (pour la création automatique de tag en production)

## Stages et jobs inclus
- `ruff`, `mypy`, `bandit`, `ty` : qualité et sécurité du code
- `publish` : déploiement des DAGs sur le SFTP
- `tag_production` : création automatique d'un tag sur la branche production après merge

## Environnements
- dev : merge request vers main
- staging : merge request de main vers production
- production : tag sur la branche production

---

*Ce composant est prêt à être inclus dans tout projet Airflow compatible GitLab CI/CD.*
