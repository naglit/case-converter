import time, os, re
import stringcase
import utility.filecontrol as filecontrol

unique_output_dir = ""

def convert_files():
    """
    This converts any cases into pascal cases in specified files
    and generates new ones in "output" directory.
    """
    
    # make directory for output
    __make_dir_for_output()

    # get file paths
    files = [file.replace("\n", "") for file in filecontrol.read_file("files.txt")]

    # case conversion
    list(map(__convert, files))

def __make_dir_for_output():
    global unique_output_dir
    unique_output_dir = __create_unique_output_dir_path()
    filecontrol.make_dir(unique_output_dir)

def __create_unique_output_dir_path():
    dir_name = f"{str(int(time.time()))}"
    return os.path.join("output", dir_name)

def __convert(filepath: str):

    # read a file
    lines = filecontrol.read_file(filepath)

    # convert cases in lines
    filename = os.path.basename(filepath)
    convert_func = __convert_cs if filename.endswith("xml") == False else __convert_xml
    pascalcase_lines = convert_func(lines)

    # write a file
    output_path = os.path.join(unique_output_dir, filename)
    filecontrol.write_file(output_path, pascalcase_lines)


def __convert_cs(lines: list):
    """ Converts cases in a cs file """

    # to lowercase
    lowercase_lines = list(map(__to_lowercase, lines))

    # to pascalcase
    return list(map(__to_pascalcase, lowercase_lines))

def __convert_xml(lines: list):
    """ Converts cases in an xml file """

    return list(map(__to_pascalcase_xml, lines))

def __to_pascalcase_xml(line: str):
    """ Converts cases of a line in an xml file """
    
    matches = re.finditer(r"(\<\/?)(\w+)(\>)", line)
    newline = line
    for match in matches:
        tag = match.group(2)
        newline = newline.replace(tag, stringcase.pascalcase(tag.lower()))
    return newline

def __to_lowercase(line: str): return line.lower() if re.search(r"^[\t\s]*\/\/[\/ ]", line) is None else line
def __to_pascalcase(line: str): return "\t" + stringcase.pascalcase(line) if re.search(r"^[\t\s]*\/\/[\/ ]", line) is None else line
    

    