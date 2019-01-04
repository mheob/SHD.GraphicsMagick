class TerminalUtilities:
    @staticmethod
    def query_yes_no(question, default=True):
        valid = {"yes": True, "y": True, "ye": True, "ja": True, "j": True,
                 "no": False, "n": False, "nein": False, "nee": False}

        if default is None:
            prompt = " [j/n] "
        elif default is True:
            prompt = " [J/n] "
        elif default is False:
            prompt = " [j/N] "
        else:
            raise ValueError("\tinvalid default answer: '%s'" % default)

        while True:
            print(question + prompt)
            choice = input().lower()

            if default is not None and choice == '':
                return default
            elif choice in valid:
                return valid[choice]
            else:
                print("\tBitte mit 'ja' oder 'nein' antworten (oder einfach 'j' bzw. 'n').\n")
