
class Utility:

    def log(self, level, msg):
        """
        :param level: variable level can be any of error, warning, info, debug
        :param msg: it will be printed
        :return:
        """
        try:
            print(msg)
        except Exception as e:
            print(str(e))