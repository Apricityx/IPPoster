import requests

# 尝试使用不同的编码解码数据
def try_decoding(data):
    encodings = ['utf-8', 'ascii', 'latin-1', 'cp1252', 'iso-8859-1', 'utf-16', 'utf-32']
    for encoding in encodings:
        try:
            print(f"Trying encoding: {encoding}")
            print(data.decode(encoding))
            print("\n")
        except UnicodeDecodeError:
            print(f"Failed to decode with {encoding}\n")

# 发起对 URL 的请求
response = requests.get('https://www.devtool.top/api/qq/info?qq=2022784837')

# 尝试使用不同的编码解码响应内容
try_decoding(response.content)

# 请注意，用户需要在运行此代码之前安装 'requests' 库。
# 可以使用以下命令安装它：pip install requests

# 由于我无法执行此代码，因此无法提供输出。
