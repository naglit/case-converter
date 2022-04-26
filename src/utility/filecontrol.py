import sys, os

def read_file(file_name):
    """ read a file and return liens """
    
    with open(file_name, encoding="utf-8") as fin:
        lines = []
        for line in fin.readlines():
            lines.append(line.replace("\r\n", "\n"))
        return lines

def write_file(file_name, lines):
    """ write liens into a file """

    file_path = file_name
    data = "".join(lines)
    if "-d" in sys.argv:
        print("\nDEBUG MODE:")
        print(data)
        return

    with open(file_path, "w", encoding="utf-8") as fout:
        print(f"Create {file_path}")        
        fout.write(data)

def make_dir(dir_path):
    if "-d" not in sys.argv:
        if not os.path.isdir(dir_path): os.makedirs(dir_path)
    else:
        print("\nDEBUG MODE:")
        print(dir_path)

