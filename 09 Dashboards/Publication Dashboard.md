# Publication Dashboard

## Notes non publiées sur le site TianSemi

```dataview
TABLE id, title, domain, vendor, site_url, publication_status
FROM "01 Domains"
WHERE site_url = null OR site_url = ""
SORT file.name ASC
```

---

## Notes prêtes à transformer en contenu

```dataview
TABLE id, title, domain, vendor, status, reviewed
FROM "01 Domains"
WHERE reviewed = true AND status = "reviewed"
SORT updated DESC
```

---

## Contenus exportés pour le site

```dataview
TABLE title, category, date
FROM "03 Content/Blog/Exported"
SORT file.mtime DESC
```
