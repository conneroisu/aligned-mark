import os
import constants

"""This class is used to represent the Mark model. 
"""


class Mark:
    """Initialize/Constructor the Mark object.
    """

    def __init__(self):
        self.data = None
        self.name = "Aligned Mark"

    """Prints the name of the model.
    """

    def print_name(self):
        print(self.name)

    """Gets the data from the data folder.
    """

    def get_data(self):
        # get the list of files in the data folder
        files = os.listdir("../" + constants.data_path)
        # get just the markdown files
        files = [file for file in files if file.endswith(".md")]
        # get the full path to the files
        files = [os.path.join("../" + constants.data_path, file) for file in files]
        # for each file in file extract "Instruction", "Prompt", "Response"
        instructions = self.get_subdivision("### Instruction:")
        prompts = self.get_subdivision("### Prompt:")
        responses = self.get_subdivision("### Response:")
        data = [open(file, encoding="utf8").read() for file in files]
        print(data)

    """Gets the "Instruction", "Prompt", "Response" for a given subdivision indicated by the string parameter "subdivision". 
    :param subdivision: The subdivision to get the data for represented by a string(e.g. "### Instruction:", "### Prompt:", "### Response:").
    """

    @staticmethod
    def get_subdivision(subdivision):
        files = os.listdir("../" + constants.data_path)
        files = [file for file in files if file.endswith(".md")]
        for file in files:
            with open(file, encoding="utf8") as f:
                data = f.read()
                files = [os.path.join("../" + constants.data_path, file) for file in files]
                result = data[data.find(subdivision + "\n") + len(subdivision + "\n"):data.find(subdivision + "\n")]
                return result

