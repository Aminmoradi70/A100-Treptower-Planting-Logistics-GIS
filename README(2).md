# A100 Treptower Park – Planting Logistics GIS

A GIS-based operational planning case study for replacement tree planting in **Treptower Park, Berlin**.

**Live demo:** https://a100-treptower-tree-gis.sara7674.chatgpt.site/

## Project overview

The project converts a conventional tree planting inventory into an interactive **spatial logistics and decision-support workflow**.

Instead of only showing planting points on a map, the tool brings together:

- tree planting locations;
- tree species and IDs;
- vehicle access points;
- mapped park paths;
- path-width / vehicle suitability classes;
- permission and access-verification status;
- route suggestions between entrances and planting locations;
- operational filters for vehicle and final-transport requirements;
- batch selection for planting work;
- CSV and GeoJSON export.

The live application currently represents **28 planting locations, 23 species and 5 access points**.

## Problem

Tree planting in a large urban park is not only a location problem. Crews also need to understand:

1. Which entrance can be used?
2. Which internal paths may physically accommodate a vehicle?
3. Is permission, a key or separate verification required?
4. Can a truck reach the planting area directly?
5. Is a compact vehicle or manual final transport required?
6. How can planting locations be grouped into practical work packages?

The project translates these operational questions into a GIS workflow.

## Spatial workflow

```text
Tree inventory
    │
    ▼
Data validation + CRS check
    │
    ▼
EPSG:25833 source coordinates
    │
    ▼
Geospatial preprocessing / GeoJSON export
    │
    ▼
Vehicle access + park path information
    │
    ▼
Access and path classification
    │
    ▼
Route / unloading-node logic
    │
    ▼
Interactive map + filters + work list
    │
    ▼
CSV / GeoJSON operational outputs
```

## Main functions in the live tool

### 1. Planting-location GIS
The map visualizes the replacement planting locations and allows the user to search and filter by tree-related and logistics-related attributes.

### 2. Operational filtering
Users can filter records by criteria such as:

- tree species;
- tree ID;
- planting area;
- recommended entrance;
- vehicle type;
- permission requirement;
- mini-truck requirement;
- manual final transport;
- access-verification status.

### 3. Vehicle-access assessment
Access points are evaluated with an operational status such as:

- directly accessible;
- permission / key required;
- no vehicle access;
- verification required.

### 4. Path-width classification
Mapped park paths are classified as a **physical suitability indicator**:

- `> 5 m` → truck candidate;
- `4–5 m` → conditional;
- `< 4 m` → compact vehicle;
- manual / small-equipment segment;
- unverified width/access.

Physical path suitability is treated separately from legal vehicle access.

### 5. Route-support logic
For a selected planting location, the application compares usable entrances and follows mapped park paths toward an unloading node. The result supports field logistics planning rather than general public navigation.

### 6. Batch planning and export
Multiple planting locations can be selected as a work package and exported as CSV or GeoJSON for further GIS or field-planning workflows.

## Coordinate reference system

The source tree coordinates use:

`EPSG:25833 – ETRS89 / UTM zone 33N`

For web mapping, coordinates can be transformed to:

`EPSG:4326 – WGS 84`

The sample Python preprocessing code in `src/` demonstrates this workflow.

## Repository structure

```text
A100-Treptower-Planting-Logistics-GIS/
│
├── README.md
├── data/
│   ├── README.md
│   ├── tree_inventory_sample.csv
│   └── access_points_schema.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── prepare_tree_data.py
│   └── access_rules.py
├── notebooks/
│   └── 01_data_quality_and_species_summary.ipynb
├── outputs/
│   ├── README.md
│   └── workflow_diagram.md
├── requirements.txt
└── .gitignore
```

## Python example

Convert a tree inventory containing UTM coordinates to GeoJSON:

```bash
python src/prepare_tree_data.py \
  --input path/to/tree_inventory.xlsx \
  --output outputs/trees_wgs84.geojson \
  --x-column easting \
  --y-column northing
```

The script:

1. reads CSV or Excel input;
2. checks required coordinate fields;
3. removes records without usable coordinates;
4. creates point geometry using EPSG:25833;
5. transforms the data to EPSG:4326;
6. exports a GeoJSON file.

## Why this is a GeoAI-relevant project

The current project is primarily **GIS, spatial analysis and decision support**, not a machine-learning project.

Its relevance to a GeoAI workflow is that it establishes the geospatial data pipeline needed before AI can be meaningfully added:

- structured spatial data;
- coordinate-system management;
- route and access attributes;
- operational classifications;
- reproducible preprocessing;
- machine-readable outputs.

Possible future research extensions could include learned travel-cost models, automated path-access classification from imagery, prioritization models for work packages, or predictive logistics. These are future extensions and are **not claimed as current functionality**.

## Tools represented by this repository

- Python
- Pandas
- GeoPandas
- Shapely
- PyProj
- GIS / spatial data processing
- GeoJSON
- Jupyter
- OpenStreetMap-based spatial context

## Interview summary

A concise way to describe the project:

> “This project started from a practical landscape-construction problem: we had a set of replacement tree locations in Treptower Park, but the planting team also needed to understand how each location could actually be reached. I transformed the inventory into a GIS-based logistics workflow that combines planting locations, park access points, path conditions and operational constraints. The tool can filter trees, assess access conditions, support route selection from an entrance toward an unloading point, group planting locations into work packages, and export the results as CSV or GeoJSON. The important part for me is that it connects spatial data analysis with a real operational decision.”

## Scope note

This repository documents the geospatial preprocessing and decision logic supporting the case study. It does **not** claim to contain the full production source code of the deployed web application.
