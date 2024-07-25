
class File_operate:

    # open and write a file
    def write_file(file_path: str, write_content: str):
        with open(file_path, mode='w') as f1:
            f1.write(write_content)

    # read a file
    def read_file(file_path: str):
        with open(file_path, mode='r') as f1:
            cur_content = f1.read()
            print(cur_content)

            # read and write a file

    def read_write_file(file_path: str, write_content: str):
        with open(file_path, mode='r+') as f1:
            cur_content = f1.read()
            print(cur_content)
            f1.write(write_content)

    # write and read a file
    def write_read_file(file_path: str, write_content: str):
        with open(file_path, mode='w+') as f1:
            f1.write(write_content)
            cur_content = f1.read()
            print(cur_content)


if __name__ == '__main__':
    path1 = r'e:\test.txt'
    content1 = 'this is my another test file!'
    content2 = 'this is my second test file!'
    # File_operate.create_file(path1)

    # File_operate.read_file(path1)

    # File_operate.read_write_file(path1, content1)
    File_operate.read_file(file_path=path1)




