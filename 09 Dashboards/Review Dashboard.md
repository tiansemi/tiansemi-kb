# Review Dashboard

## À relire

```dataview
TABLE id, title, domain, vendor, last_review
FROM "01 Domains"
WHERE reviewed = false
SORT updated ASC
```

---

## Notes sans références

```dataview
TABLE id, title, domain, vendor
FROM "01 Domains"
WHERE length(references) = 0
SORT file.name ASC
```

---

## Notes sans prérequis

```dataview
TABLE id, title, domain, vendor
FROM "01 Domains"
WHERE length(prerequisites) = 0
SORT file.name ASC
```
