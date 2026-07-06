from __future__ import annotations

import csv
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT = ROOT / "07 Automation" / "Blueprints" / "huawei_hcia_datacom_v2_blueprint.csv"
TOPIC_TEMPLATE = ROOT / "06 Templates" / "Templater" / "Huawei HCIA Topic Template.md"
LAB_TEMPLATE = ROOT / "06 Templates" / "Labs" / "Huawei HCIA Lab Template.md"
TODAY = date.today().isoformat()
AUTHOR = "MOULO OHOLO Jean Noel"


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def split_template_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                return "\n".join(lines[index + 1 :]).strip()
    return text.strip()


def source_material_for(row: dict[str, str]) -> list[str]:
    if row["source"] == "Training Material":
        return ["HCIA-Datacom V2.0 Training Material.pdf"]
    return []


def source_lab_for(row: dict[str, str]) -> list[str]:
    if row["source"] == "Lab Guide" or row["lab_required"].lower() == "true":
        return ["HCIA-Datacom V2.0 Lab Guide.pdf"]
    return []


def yaml_list(name: str, values: list[str]) -> list[str]:
    if not values:
        return [f"{name}: []"]
    return [f"{name}:"] + [f"  - {yaml_quote(value)}" for value in values]


def build_topic_yaml(row: dict[str, str]) -> str:
    lines = [
        "---",
        f"id: {row['id']}",
        f"title: {yaml_quote(row['title'])}",
        'category: "Huawei HCIA-Datacom Topic"',
        'domain: "Datacom"',
        'vendor: "Huawei"',
        'certification: "HCIA-Datacom"',
        'version: "V2.0"',
        f"difficulty: {yaml_quote(row['difficulty'])}",
        'status: "draft"',
        f"author: {yaml_quote(AUTHOR)}",
        "reviewed: false",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        f"module: {yaml_quote(row['module'])}",
        f"type: {yaml_quote(row['type'])}",
        f"source: {yaml_quote(row['source'])}",
        f"lab_required: {row['lab_required'].lower()}",
    ]
    lines.extend(yaml_list("source_material", source_material_for(row)))
    lines.extend(yaml_list("source_lab", source_lab_for(row)))
    lines.extend(
        [
            "official_source:",
            '  - "https://e.huawei.com/en/talent/cert/#/careerCert"',
            "tags:",
            "  - huawei",
            "  - hcia",
            "  - datacom",
            "keywords: []",
            "prerequisites: []",
            "related: []",
            "commands: []",
            "labs: []",
            "assets: []",
            'publication_status: "not-started"',
            "site_url:",
            "---",
        ]
    )
    return "\n".join(lines)


def build_lab_yaml(row: dict[str, str]) -> str:
    lines = [
        "---",
        f"id: {row['id']}",
        f"title: {yaml_quote(row['title'])}",
        'category: "Huawei HCIA-Datacom Lab"',
        'domain: "Datacom"',
        'vendor: "Huawei"',
        'certification: "HCIA-Datacom"',
        'version: "V2.0"',
        f"difficulty: {yaml_quote(row['difficulty'])}",
        'status: "draft"',
        f"author: {yaml_quote(AUTHOR)}",
        "reviewed: false",
        f"created: {TODAY}",
        f"updated: {TODAY}",
        f"module: {yaml_quote(row['module'])}",
        f"type: {yaml_quote(row['type'])}",
        f"source: {yaml_quote(row['source'])}",
        f"lab_required: {row['lab_required'].lower()}",
    ]
    lines.extend(yaml_list("source_lab", source_lab_for(row)))
    lines.extend(
        [
            "official_source:",
            '  - "https://e.huawei.com/en/talent/cert/#/careerCert"',
            "tags:",
            "  - huawei",
            "  - hcia",
            "  - datacom",
            "  - lab",
            "devices: []",
            "commands: []",
            "verification: []",
            "troubleshooting: []",
            'publication_status: "not-started"',
            "site_url:",
            "---",
        ]
    )
    return "\n".join(lines)


def render_body(row: dict[str, str], template_body: str) -> str:
    body = template_body.replace("<% tp.file.title %>", row["title"])
    body = body.replace("# Lab — Titre", f"# Lab — {row['title']}")
    body = body.replace("# Lab - Titre", f"# Lab - {row['title']}")
    if "## Source officielle" in body:
        body = body.replace(
            "## Source officielle",
            f"## Source officielle\n\n- {row['source']}",
            1,
        )
    if "## Objectifs officiels couverts\n\n-" in body:
        body = body.replace(
            "## Objectifs officiels couverts\n\n-",
            f"## Objectifs officiels couverts\n\n- À compléter depuis {row['source']}, sans reproduction massive.",
            1,
        )
    return body.strip()


def validate_row(row: dict[str, str]) -> None:
    required = ["id", "title", "module", "type", "difficulty", "source", "lab_required", "path"]
    missing = [name for name in required if not row.get(name)]
    if missing:
        raise ValueError(f"Missing fields {missing} in row {row}")
    if row["type"] not in {"topic", "lab"}:
        raise ValueError(f"Unsupported type {row['type']} for {row['id']}")


def main() -> None:
    topic_body = split_template_body(TOPIC_TEMPLATE)
    lab_body = split_template_body(LAB_TEMPLATE)

    with BLUEPRINT.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            validate_row(row)
            target = ROOT / row["path"]
            if target.exists():
                print(f"SKIP {target.relative_to(ROOT).as_posix()}")
                continue

            target.parent.mkdir(parents=True, exist_ok=True)
            if row["type"] == "topic":
                content = build_topic_yaml(row) + "\n\n" + render_body(row, topic_body)
            else:
                content = build_lab_yaml(row) + "\n\n" + render_body(row, lab_body)

            target.write_text(content.strip() + "\n", encoding="utf-8")
            print(f"CREATED {target.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
