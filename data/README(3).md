# Data

This folder contains a **public-display sample** derived only from records visible in the live demo.

The complete operational dataset is intentionally not bundled here.

## Files

- `tree_inventory_sample.csv` – tree IDs and species visible in the live application.
- `access_points_schema.csv` – schema for access-point data without invented locations.

## Expected spatial fields in the full workflow

A working source dataset can contain fields such as:

- `tree_id`
- `species_de`
- `botanical_name`
- `easting`
- `northing`
- `planting_area`
- `recommended_entrance`
- `vehicle_type`
- `permission_required`
- `mini_truck_required`
- `manual_final_transport`
- `access_verification`

Source tree coordinates are expected in **EPSG:25833** unless explicitly configured otherwise.
