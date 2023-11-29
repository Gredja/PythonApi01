from Configuration.Models.Configuration import Configuration


class TestBaseClass:
    configuration = Configuration.get_configuration(Configuration)

    def setup_method(self, method):
        print("Setup before each test method", method.__name__)

    def teardown_method(self, method):
        print("Teardown after each test method", method.__name__)
