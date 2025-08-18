import zipfile

def main():
    count=0 #试验次数
    cyber_chars=['0','2','3','4','5','6','7','8','9','1','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    zfile = zipfile.ZipFile('./3+4.zip')
    for c1 in ['0','2','3','4','5','6','7','8','9','1','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']: #猜测密码为数字7开头
        for c2 in range(len(cyber_chars)):
            for c3 in range(len(cyber_chars)):
                for c4 in range(len(cyber_chars)):
                    for c5 in range(len(cyber_chars)):#暴力生成五位测试密码
                        password=c1+cyber_chars[c2]+cyber_chars[c3]+cyber_chars[c4]+cyber_chars[c5]
                        try:
                            zfile.extractall(pwd=bytes(password, "utf8"))
                            print("文件解压密码为: ", password)
                            print("累计测试密码次数：",count)
                            return password #找到密码，结束
                        except:  # 解压失败，开始下一次解压
                            count+=1
if __name__ == "__main__":
    main()