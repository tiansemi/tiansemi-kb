# Content Dashboard

## Notes sans article de blog

```dataview
TABLE id, title, domain, vendor, blog
FROM "01 Domains"
WHERE blog = null OR blog = ""
SORT file.name ASC
```

---

## Notes sans publication LinkedIn

```dataview
TABLE id, title, domain, vendor, linkedin
FROM "01 Domains"
WHERE linkedin = null OR linkedin = ""
SORT file.name ASC
```

---

## Contenus Blog

```dataview
TABLE status, created, updated
FROM "03 Content/Blog"
SORT file.mtime DESC
```
