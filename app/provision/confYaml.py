import yaml


class ConfYaml:
    def __init__(self, conf=None, conf_model=None):
        self.__conf = conf
        self.__conf_model = conf_model

    def get_conf(self):
        return self.__conf

    def set_conf(self, setConf):
        self.__conf = setConf

    def get_conf_model(self):
        return self.__conf_model

    def set_conf_model(self, setConfModel):
        self.__conf_model = setConfModel

    def conf_model_dict(self):
        dict_conf = yaml.load(self.__conf_model, Loader=yaml.FullLoader)
        return dict_conf

    def valid_conf(self):
        if self.__conf_model is None:
            return False
        else:
            return True
