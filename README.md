# TianSemi Operating System (TSOS)

TSOS est le système de gestion des connaissances de TianSemi.

Site cible : [http://tiansemi.github.io/](http://tiansemi.github.io/)

Il centralise :

* les connaissances techniques ;
* les labs ;
* les références ;
* les templates ;
* les prompts ;
* les assets ;
* le moteur de publication.

## Architecture

* `01 Domains` : connaissances techniques par domaine.
* `02 Projects` : projets TianSemi.
* `03 Content` : contenus générés.
* `04 Assets` : images, labs, vidéos, PDF.
* `05 References` : sources.
* `06 Templates` : modèles Obsidian/Templater.
* `07 Automation` : scripts, prompts, exports.
* `08 Glossary` : glossaire technique.
* `09 Dashboards` : tableaux de bord Dataview.

## Workflow

1. Créer ou enrichir une note technique.
2. Relier la note aux prérequis et concepts associés.
3. Vérifier la note.
4. Générer les contenus via la Prompt Library.
5. Exporter les contenus pour [http://tiansemi.github.io/](http://tiansemi.github.io/).
6. Publier sur le site et le blog.
7. Mettre à jour les métadonnées `blog`, `site_url`, `publication_status`.

## Commandes utiles

Exporter l'index :

```bash
python "07 Automation/Scripts/export_index.py"
```

Générer des notes depuis le blueprint :

```bash
python "07 Automation/Scripts/generate_notes.py"
```
