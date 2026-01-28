# template_airflow_deployment


Ce projet est un exemple industriel prêt à l'emploi pour le déploiement de DAGs Airflow.
Toutes les opérations de qualité, de test et de déploiement des DAGs sont automatisées via CI/CD (GitHub Actions ou GitLab CI).

## Structure du projet

- `src/` : Contient les DAGs d'exemple :
  - `training_pipeline.py` : pipeline d'entraînement
  - `inference_pipeline.py` : pipeline d'inférence
  - `model_monitoring_pipeline.py` : pipeline de monitoring de modèle

## Prérequis
- Python 3.8+
- Apache Airflow


## Utilisation

### Déploiement et qualité via CI/CD

Le projet est conçu pour être utilisé avec une chaîne CI/CD :

- **Qualité et sécurité** : Linting (ruff), typage (ty), sécurité (bandit) sont exécutés automatiquement.
- **Déploiement** : Les DAGs du dossier `src/` sont publiés automatiquement sur un serveur SFTP après validation, via GitHub Actions ou GitLab CI.

### Lancement local (optionnel)

Pour tester localement :

1. Placez les fichiers du dossier `src/` dans le dossier `dags/` de votre instance Airflow.
2. Lancez Airflow :
  ```bash
  airflow standalone
  ```


## À personnaliser
- Remplacez les opérateurs `DummyOperator` par vos tâches réelles.
- Ajoutez des dépendances et de la logique métier selon vos besoins.

---


*Projet généré pour servir de base à des déploiements industriels de pipelines Airflow avec automatisation CI/CD (GitHub Actions ou GitLab CI).* 
