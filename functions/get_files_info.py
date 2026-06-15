import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_dir_path = os.path.abspath(working_directory)
    target_path = os.path.join(abs_working_dir_path,directory)
    target_dir_path = os.path.normpath(target_path)
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    if  not os.path.commonpath([abs_working_dir_path, target_dir_path]) == abs_working_dir_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    return f'Success: "{directory}" is within the working directory'
    

