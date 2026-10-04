# pyqure — Kanban

Une carte = un commit. Limite WIP : 1 à 2 cartes en cours.

## En cours

### Ajouter mypy aux dev dependencies

- [ ] `mypy` dans le groupe `dev`
- [ ] `uv lock` mis à jour
- [ ] `mypy .` passe en strict

## Backlog

Par ordre de priorité — la première carte est la prochaine à faire.

### 1. Nettoyer le dépôt

- [ ] Supprimer `README_sample.md` (contenu fusionné dans le README)
- [ ] `git rm --cached` sur `.idea/`

### 2. Protocole typé pour `provide` / `inject`

- [ ] Remplacer `Callable[[Key[Any]], Any]` par des `Protocol` génériques
- [ ] Typage préservé de bout en bout côté appelant
- [ ] `mypy strict` passe avec les nouveaux types

### 3. Fournisseurs paresseux (factory)

- [ ] `provide_factory(key, factory)` : la valeur n'est créée qu'à l'`inject`
- [ ] Tests : appel unique, mise en cache éventuelle

## Terminé

- pyqure peut fournir et injecter une valeur (`d193c0d`)
- Écrire le README (`19be81f`, PR #2)
- Corriger les métadonnées de `pyproject.toml` (`552635c`, PR #3)
