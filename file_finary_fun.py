import os


class File_finary_test:

    @staticmethod
    def Find_files_func1(file_path: str):
        # os.walk()
        for cur_dir, file_documents, files in os.walk(file_path):
            print("current_path:")
            print(f"  {cur_dir}")

            print("file_documents_current_path:")
            for file_document_name in file_documents:
                print(file_document_name)

            print("file_name_current_path:")
            for file in files:
                print(file)

    @staticmethod
    def Find_files_func2(target_path: str):
        # os.dirlist() 返回该路径下所有的子目录组成的列表
        for dir_name in os.listdir(target_path):
            print(dir_name)
            child_path = os.path.join(target_path, dir_name)
            print(f" {child_path}")
            assert os.path.exists(child_path), "child_path not exist"


if __name__ == "__main__":
    path1 = r"E:\AutoTest_learning"

    # File_finary_test.Find_files_func1(path1)
    File_finary_test.Find_files_func2(path1)
