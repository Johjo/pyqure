# pyqure — Kanban

Une carte = un commit. Limite WIP : 1 à 2 cartes en cours.

## En cours

### Protocole typé pour `provide` / `inject`

- [x] Remplacer `Callable[[Key[Any]], Any]` par des `Protocol` génériques
- [x] Typage de bout en bout côté appelant via souscription `Key[T](...)`
- [x] Pattern abstrait sans friction (pas de `# type: ignore`, pas de `type-abstract`)
- [x] `mypy strict` passe avec les nouveaux types

## Backlog

Par ordre de priorité — la première carte est la prochaine à faire.

### 1. Fournisseurs paresseux (factory)

- [ ] `provide_factory(key, factory)` : la valeur n'est créée qu'à l'`inject`
- [ ] Tests : appel unique, mise en cache éventuelle

## Terminé

- pyqure peut fournir et injecter une valeur (`d193c0d`)
- Écrire le README (`19be81f`, PR #2)
- Corriger les métadonnées de `pyproject.toml` (`552635c`, PR #3)
- Ajouter mypy aux dev dependencies (`c5cbf13`, PR #4)
- Nettoyer le dépôt (`c84ec7e`, PR #5)
