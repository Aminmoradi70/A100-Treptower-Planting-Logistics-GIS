"""Transparent access-classification helpers.

These functions encode operational rules as readable decision logic.
They are intentionally simple and auditable.
"""


def classify_path_width(width_m: float | None) -> str:
    """Return the physical path-width class used by the case-study workflow."""
    if width_m is None:
        return "width/access unverified"
    if width_m > 5:
        return "truck candidate"
    if width_m >= 4:
        return "conditional"
    if width_m > 0:
        return "compact vehicle"
    return "manual / small equipment"


def access_status(
    vehicle_allowed: bool | None,
    permission_required: bool = False,
) -> str:
    """Classify the operational access status.

    Legal access and physical path width should be evaluated separately.
    """
    if vehicle_allowed is None:
        return "Verification required"
    if not vehicle_allowed:
        return "No vehicle access"
    if permission_required:
        return "Permission / key required"
    return "Directly accessible"


def final_transport_mode(
    path_width_m: float | None,
    vehicle_allowed: bool | None,
) -> str:
    """Provide a simple last-segment logistics recommendation."""
    if vehicle_allowed is False:
        return "manual / small equipment"
    if path_width_m is None:
        return "verification required"
    if path_width_m > 5:
        return "truck candidate"
    if path_width_m >= 4:
        return "conditional vehicle access"
    if path_width_m > 0:
        return "compact vehicle / mini-truck"
    return "manual / small equipment"
