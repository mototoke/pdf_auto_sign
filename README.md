# pdf_auto_sign
PDFを画像に変換後、4分割して一番白色領域の大きいところに文字列挿入

# command
host:git clone this repositoroy
host:cd pdf_auto_sign/
// Image Build & Run
host:docker-compose up -d --build
// Enter a container
host:docker exec -it pdf_auto_sign_pdf_1 bash
// move dir pdf_auto_sign
pdf@f57d38aee057:~$ ls
Dockerfile  README.md  docker-compose.yml  pdf_auto_sign
pdf@f57d38aee057:~$ cd pdf_auto_sign/
// Execute this app
pdf@f57d38aee057:~$ python main.py

![App Image](https://github.com/mototoke/pdf_auto_sign/images/app.png)
