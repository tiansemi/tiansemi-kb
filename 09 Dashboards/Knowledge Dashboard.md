# Knowledge Dashboard

## Notes techniques en brouillon

```dataview
TABLE id, domain, vendor, difficulty, status, reviewed
FROM "01 Domains"
WHERE status = "draft"
SORT file.name ASC
```

---

## Notes Cisco CCNA

```dataview
TABLE id, difficulty, reviewed, site_url, publication_status
FROM "01 Domains/Cisco"
WHERE ccna = true
SORT id ASC
```

---

## Notes non revues

```dataview
TABLE id, title, domain, vendor, status
FROM "01 Domains"
WHERE reviewed = false
SORT file.name ASC
```
