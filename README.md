# bin_tool

bin_to_hex 基于intelhex库

cli 基于 click库



## 切换conda环境为32位

```powershell
$Env:CONDA_FORCE_32BIT=1
```





## install env

```shell
pip install -r pipEnv.txt
```



## run

```shell
python bin_tool.py version
```

 convert:

```shell
python bin_tool.py bin-to-hex --bin=`bin_path` --hex=`hex_path` --start=0x08000000
```





## build

```shell
pyinstaller -F bin.tool
```



