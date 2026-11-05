# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter | Values | Notes |
|-----------|--------|-------|
| `weight_kg` | positive float | parcel weight |
| `zone` | `"local"`, `"regional"` | delivery zone |
| `service` | `"standard"` (default), `"express"` | express adds $7.00 |

Unknown zones or service levels raise `ValueError`.

**CLI usage:**

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
python -m warehouse.cli 2 local                   # $8.00  (standard)
python -m warehouse.cli 2 local --service express  # $15.00 (express)
python -m warehouse.cli 2 regional --service express  # $18.00
```
