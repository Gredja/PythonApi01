import json
from types import SimpleNamespace

from Configuration.Models import ApiConfiguration, GeneralConfiguration, UiConfiguration


class Configuration:
    api = ApiConfiguration
    general = GeneralConfiguration
    ui = UiConfiguration
    __configuration = None

    @staticmethod
    def get_configuration(self):
        if self.__configuration is None:
            self.__configuration = self.__get_configuration_from_file(self)

        return self.__configuration

    @staticmethod
    def __get_configuration_from_file(self):
        try:
            file = open('../config.json')
        except FileNotFoundError as error:
            print(f'FileNotFoundError: {error.filename}')
        else:
            with file:
                json_configuration = json.load(file, object_hook=lambda d: SimpleNamespace(**d))

        return self.__cast_json_to_object(json_configuration)

    @staticmethod
    def __cast_json_to_object(json_conf):
        configuration = Configuration
        configuration.api.Api.baseUrl = json_conf.api.baseUrl
        configuration.api.Api.version = json_conf.api.version

        return configuration
