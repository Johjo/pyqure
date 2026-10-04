# pyqure — Kanban

Une carte = un commit. Limite WIP : 1 à 2 cartes en cours.

## En cours

### Corriger les métadonnées de `pyproject.toml`

- [ ] Renseigner `description`
- [ ] Classifiers alignés avec `requires-python = ">=3.10"`
- [ ] Ajouter une licence (fichier + champ)

## Backlog

Par ordre de priorité — la première carte est la prochaine à faire.

### 1. Ajouter mypy aux dev dependencies

- [ ] `mypy` dans le groupe `dev`
- [ ] `uv lock` mis à jour
- [ ] `mypy .` passe en strict

### 2. Nettoyer le dépôt

- [ ] Supprimer `README_sample.md` (contenu fusionné dans le README)
- [ ] `git rm --cached` sur `.idea/`

### 3. Protocole typé pour `provide` / `inject`

- [ ] Remplacer `Callable[[Key[Any]], Any]` par des `Protocol` génériques
- [ ] Typage préservé de bout en bout côté appelant
- [ ] `mypy strict` passe avec les nouveaux types

### 4. Fournisseurs paresseux (factory)

- [ ] `provide_factory(key, factory)` : la valeur n'est créée qu'à l'`inject`
- [ ] Tests : appel unique, mise en cache éventuelle

## Terminé

- pyqure peut fournir et injecter une valeur (`d193c0d`)
- Écrire le README (`19be81f`, PR #2)
