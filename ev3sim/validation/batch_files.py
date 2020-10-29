from ev3sim.validation.validator import Validator

class BatchValidator(Validator):

    REQUIRED_KEYS = ["preset_file", "bots"]
    AVAILABLE_KEYS = REQUIRED_KEYS + ["settings"]

    @classmethod
    def validate_json(cls, json_obj) -> bool:
        return cls.validate_dict(json_obj)
