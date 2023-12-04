class Schemas:
    store_inventory_schema = {
        "properties": {
            "sold": {"type": "number"},
            "inactive": {"type": "number"},
            "string": {"type": "number"},
            "unavailable": {"type": "number"},
            "pending": {"type": "number"},
            "available": {"type": "number"},
            "active": {"type": "number"}
        },
        "additionalProperties": True
    }
