import logging

import jsonschema


class JsonSchemaValidator:
    @classmethod
    def validate(cls, json_data: dict, schema: dict):
        validator = jsonschema.Draft7Validator(schema)
        errors = validator.iter_errors(json_data)
        err_list = []
        for error in errors:
            logging.error(f"The JSON data is not valid: {error=}")
            err_list.append(error)
        return err_list
