# TextReader

* [Usage](#usage)

## <a href="usage"></a> Usage

If you want to use this repository in your work you need to set up environment.

1. First of all, you need to *<a href="https://git-scm.com/docs/git-clone">git clone</a>* this repository to your local file system or download project's archive.
2. You need to install required libriries from *<a href="https://pip.pypa.io/en/stable/user_guide/#requirements-files">requirements.txt</a>* file. 

Script works as CLI and uses *<a href="https://pypi.org/project/fire/">fire</a>* library.
1. Reading text from local image file.
    ```commandline
    python3 main.py TextReader read_local 'path_to_image.png'
    ```

2. Reading text from local directory files.
    ```commandline
    python3 main.py TextReader read_local_map 'path_to_dir'
    ```
