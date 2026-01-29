# template_airflow_deployment (exemple)

Ce dossier contient un exemple industriel prêt à l'emploi pour le déploiement de DAGs Airflow.

## Structure du projet

- `src/` : Contient les DAGs d'exemple :
  - `training_pipeline.py` : pipeline d'entraînement
  - `inference_pipeline.py` : pipeline d'inférence
  - `model_monitoring_pipeline.py` : pipeline de monitoring de modèle

## Prérequis
- Python 3.8+
- Apache Airflow

## Utilisation

Placez les fichiers du dossier `src/` dans le dossier `dags/` de votre instance Airflow.

Lancez Airflow :
```bash
airflow standalone
```

## À personnaliser
- Remplacez les opérateurs `EmptyOperator` par vos tâches réelles.
- Ajoutez des dépendances et de la logique métier selon vos besoins.

## Exemple d'inclusion du composant CI/CD

Ajoutez dans votre `.gitlab-ci.yml` principal :

```yaml
include:
  - component: $CI_SERVER_FQDN/my-org/template_airflow_deployment/template/component@1.0.0
    inputs:
      SFTP_HOST: "sftp.example.com"
      SFTP_USERNAME: "user"
      SFTP_PASSWORD: "password"
      SFTP_PORT: "22"
      SFTP_DAGS_PATH: "/remote/dags"
```

Adaptez les variables selon votre environnement et votre organisation.

---

*Ce dossier sert d'exemple pour l'utilisation du composant CI/CD fourni dans `template/`.*
