# pyqure — Kanban

Une carte = un commit. Limite WIP : 1 à 2 cartes en cours.

## En cours

### Écrire le README

- [ ] Description courte de pyqure (DI par clés typées)
- [ ] Exemple minimal `provide` / `inject`
- [ ] Instructions d'installation (`uv`/`pip`)
- [ ] Commandes de dev (tests, mypy)

### 1. Corriger les métadonnées de `pyproject.toml`

- [ ] Renseigner `description`
- [ ] Classifiers alignés avec `requires-python = ">=3.10"`
- [ ] Ajouter une licence (fichier + champ)

### 2. Ajouter mypy aux dev dependencies

- [ ] `mypy` dans le groupe `dev`
- [ ] `uv lock` mis à jour
- [ ] `mypy .` passe en strict

### 3. Nettoyer le dépôt

- [ ] Supprimer `README_sample.md` (contenu fusionné dans le README)
- [ ] `git rm --cached` sur `.idea/`

### 4. Protocole typé pour `provide` / `inject`

- [ ] Remplacer `Callable[[Key[Any]], Any]` par des `Protocol` génériques
- [ ] Typage préservé de bout en bout côté appelant
- [ ] `mypy strict` passe avec les nouveaux types

### 5. Fournisseurs paresseux (factory)

- [ ] `provide_factory(key, factory)` : la valeur n'est créée qu'à l'`inject`
- [ ] Tests : appel unique, mise en cache éventuelle

## Terminé

- pyqure peut fournir et injecter une valeur (`d193c0d`)
