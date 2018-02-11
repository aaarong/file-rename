import os
import getopt, sys

def rename(work_dir, new_name, start_index):
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        
        newfile = new_name+str(start_index)+file_ext
        
        os.rename(
            os.path.join(work_dir, filename),
            os.path.join(work_dir, newfile)
        )
        start_index = start_index+1
            
def main():
    opts, args = getopt.getopt(sys.argv[1:], "hd:i:n:", ["help=", "work_dir=", "start_index=", "new_name="])
    work_dir = ""
    new_name = "default"
    start_index = 0
    def usage():
        print("""
        -h --help                 print the help
        -d --work_dir             work_dir
        -n --new_name             new_name
        -i --start_index           start_index
        """)
    for op, value in opts:
        if op in ("-d","--work_dir"):
            work_dir = value
        elif op in ("-i","--start_index"):
            start_index = int(value)
        elif op in ("-n","--new_name"):
            new_name = value
        elif op in ("-h"):
            usage()
            sys.exit()
            
    rename(work_dir, new_name, start_index)
if __name__ == '__main__':
        main()
