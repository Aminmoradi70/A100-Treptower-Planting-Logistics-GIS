"""Prepare a tree inventory for web-GIS use.

Example:
    python src/prepare_tree_data.py \
        --input data/tree_inventory.xlsx \
        --output outputs/trees_wgs84.geojson \
        --x-column easting \
        --y-column northing
"""

from __future__ import annotations

import argparse
from pathlib import Path

import geopandas as gpd
import pandas as pd


SOURCE_CRS = "EPSG:25833"
WEB_CRS = "EPSG:4326"


def read_table(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported input format: {suffix}")


def prepare_points(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    source_crs: str = SOURCE_CRS,
    target_crs: str = WEB_CRS,
) -> gpd.GeoDataFrame:
    missing = [c for c in (x_column, y_column) if c not in df.columns]
    if missing:
        raise KeyError(f"Missing coordinate column(s): {', '.join(missing)}")

    work = df.copy()
    work[x_column] = pd.to_numeric(work[x_column], errors="coerce")
    work[y_column] = pd.to_numeric(work[y_column], errors="coerce")
    work = work.dropna(subset=[x_column, y_column]).copy()

    if work.empty:
        raise ValueError("No valid coordinate pairs remain after validation.")

    gdf = gpd.GeoDataFrame(
        work,
        geometry=gpd.points_from_xy(work[x_column], work[y_column]),
        crs=source_crs,
    )
    return gdf.to_crs(target_crs)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--x-column", default="easting")
    parser.add_argument("--y-column", default="northing")
    parser.add_argument("--source-crs", default=SOURCE_CRS)
    parser.add_argument("--target-crs", default=WEB_CRS)
    args = parser.parse_args()

    df = read_table(args.input)
    gdf = prepare_points(
        df=df,
        x_column=args.x_column,
        y_column=args.y_column,
        source_crs=args.source_crs,
        target_crs=args.target_crs,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    gdf.to_file(args.output, driver="GeoJSON")
    print(f"Exported {len(gdf)} features to {args.output}")


if __name__ == "__main__":
    main()
