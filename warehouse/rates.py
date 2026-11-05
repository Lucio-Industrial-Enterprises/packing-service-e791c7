"""Shipping rate calculations."""

_EXPRESS_SURCHARGE = 7.0
_BASE_RATES = {"local": 5.0, "regional": 8.0}
_SERVICES = {"standard", "express"}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: Service level — ``"standard"`` (default) or ``"express"``.
            Express adds $7.00 to the standard rate.

    Returns:
        Total shipping cost rounded to two decimal places.

    Raises:
        ValueError: If weight is non-positive, zone is unknown, or service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _BASE_RATES:
        raise ValueError("unknown zone")
    if service not in _SERVICES:
        raise ValueError(f"unknown service: {service!r}")
    surcharge = _EXPRESS_SURCHARGE if service == "express" else 0.0
    return round(_BASE_RATES[zone] + 1.5 * weight_kg + surcharge, 2)
