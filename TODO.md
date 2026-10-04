# pyqure — Kanban

Une carte = un commit. Limite WIP : 1 à 2 cartes en cours.

## En cours

### Nettoyer le dépôt

- [ ] Supprimer `README_sample.md` (contenu fusionné dans le README)
- [x] `.idea/` : déjà ignoré, non tracké — rien à faire

## Backlog

Par ordre de priorité — la première carte est la prochaine à faire.

### 1. Protocole typé pour `provide` / `inject`

- [ ] Remplacer `Callable[[Key[Any]], Any]` par des `Protocol` génériques
- [ ] Typage préservé de bout en bout côté appelant
- [ ] `mypy strict` passe avec les nouveaux types

### 2. Fournisseurs paresseux (factory)

- [ ] `provide_factory(key, factory)` : la valeur n'est créée qu'à l'`inject`
- [ ] Tests : appel unique, mise en cache éventuelle

## Terminé

- pyqure peut fournir et injecter une valeur (`d193c0d`)
- Écrire le README (`19be81f`, PR #2)
- Corriger les métadonnées de `pyproject.toml` (`552635c`, PR #3)
- Ajouter mypy aux dev dependencies (`c5cbf13`, PR #4)
