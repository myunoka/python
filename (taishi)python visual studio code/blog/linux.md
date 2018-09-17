# Linux命令总结
## 用户命令
>useradd -m -s /bin/bash -G sudo,adm lzm  （-m创建新的主目录（也可以用-d指定其他目录） -s 指定用户登录的shell，默认是/bin/sh。一定要修改成为/bin/bash -G 指定用户组的附加组 -g 可以指定主组。lzm是用户）
usermod -g xxx lzm 更改用户所属主组 usermod -G xxx lzm 更改用户所属的附加群组(这种会把用户从其他组中去掉，只属于该附组)。usermod -a -G xxx lzm 添加附组不影响会修改原有的附组<font color=#0099ff size=2 face="黑体">"黑体"</font>
## tmux分屏:
>tmux ls 查看  
tmux at -t 1 进入第一个  快捷键是ctrl+b+s  
ctrl+b+d (ctrl+b是同时按，然后松开在按d) 脱离当前会话，返回shell  
tmux new -s xxx 新建会话并指定会话名称  
tmux new 新建会话(不指定会话名称)  
tmux a 接入上一个会话 tmux detach 断开当前会话（还可以使用快捷键：control+b，再按d)(会保存会话)  
tmux kill-session -t session-name 关闭指定会话            
(上下分屏：ctrl + b  再按)  
tmux kill-session -a -t session-name 关闭除指定会话外的所有会话	     (切换屏幕：ctrl + b  再按o  关闭一个终端：ctrl + b  再按x)  
在会话中切换  
ctrl+b，再按s 显示会话列表，再进行会话切换       
(上下分屏与左右分屏切换： ctrl + b  再按空格键)  
tmux kill-server 销毁所有会话并停止tmux
## liux查看服务是否自动开启启动:
>systemctl is-enabled test.service #查询服务是否开机启动  
systemctl is-enabled httpd	查看某个服务是否启动了开机启动  
systemctl disable firewalld 	禁止服务开机启动  
systemctl enabled firewalld	开启服务开机启动
## systemd查看开机自启动的程序:
>ls /etc/systemd/system/multi-user.target.wants/
## linux shell替换命令:
>cat /etc/ssh/sshd_config  显示sshd内容 用^cat^vim  意思是把上条命令的cat替换成vim
## lsof命令:
>用于查看你进程开打的文件，打开文件的进程 列：lsof -i:22 查看22端口进程
## dd命令:
>dd if=1.txt of=2.txt 就是把1.txt文件内容拷贝到2.txt  可以用来备份系统。备份sda
## grep命令:
>检索工具。如cat /etc/passwd | grep root  只显示跟root有关的。-i忽略字符大小写的差别 -v 表示不输出包含的匹配规则  
grep命令查找系统某个文件关键字并输出来：grep "关键字" 目录 -r --include	*.php #-r 意思是递归的对目录下的所有文件  grep -r "$_POST" /home效果也是一样
## 管道符(|):
>“将前面的标准输出作为后面的标准输入”
## xargs命令:
>xargs是实现“将标准输入作为命令的参数”  
ls | xargs ls  xargs相当于直接从键盘输入管道符前面命令执行的结果内容在ls显示出来 。还有其他参数可选
## find删除24小时内修改的文件命令:
>find ./ -mtime -1 -type f | xargs rm -rf
## stat命令:
>查看文件的状态 如：stat /etc/passwd
## lsattr命令:
>查看文件属性 如：lsattr /etc/passwd
## last与lastb命令:
>用来列出目前与过去登录系统的用户相关信息 如：last查看登录成功的用户、lastb查看登录失败的用户记录。
## ss命令:
>ss命令用来显示处于活动状态的套接字信息：显示tcp链接 ss -t -a
## awk命令:
>awk是 linux一个分析处理工具：awk -F: '($3 == 1002) {print $1}' /etc/passwd (-F是指定分隔符，$3是第三个分隔区‘$3 == 1002)’判断条件(判断第三分隔区的内容是否为1002)如果匹配成功，‘{print $1}’输出这一行的第一个分隔符区域)这个命令是查找第三个分隔符为1002，然后输出第一个字符。
## head命令:
>head命令用于显示文件的开头的内容。在默认情况下，head命令显示文件的头10行内容。head -n3 表示显示前3行
## cut命令:
>类似于awk命令，不过这个命令比awk好用多了。  
cut命令，是一个选取命令，其功能是将文件中的每一行”字节” ”字符” ”字段” 进行剪切，选取我们需要的，并将这些选取好的数据输出至标准输出  
cut -b 1-3 1.txt 显示每行的1-3个字符（如果是汉字可以使用-nb或者-c）  
-d ：自定义分隔符，默认为制表符	-f(filed) ：与-d一起使用，指定显示哪个区域。  
列：1.txt内容为  
http://www.baidu.com  
http://www.google.com  
cut -d / -f3 1.txt (-d是指定你的分隔符 -f 是你指定的分隔符的区域(就是说你分隔符前面的字符为1区域的这样排序（如这里的3区域就是最好一个区域也就是分隔符的后一个区域))  
输出www.baidu.com  
www.google.com
## netstat命令:
>netstat -anept 显示端口  
netstat -anept|grep 25 显示指定端口  
端口问题:  
root用户执行netstat -anelp n表示不查询dns t表示tcp协议 u表示udp协议 p表示查询占用的程序 l表示查询正在监听的程序
# vim命令
>shell终端下：ctrl+a 移动到开头 catrl+e 移动到结尾  
E 移到下一个字的结尾。忽略标点符号  
B 移到前一个字的开头，忽略标点符号  
e 移到下一个字的结尾  
b 移到当前字或前一个字的开头  
vim问题：  
转到10行:在命令模式输入 10G  
删除所有内容：先用G 转到文件尾，然后使用下面命令：1,.d  
删除第10行到第20行的内容：先用20G转到第20行，然后使用下面命令：9,.d  
关于删除的一些说明：  
1、在vi中，" .  "表示当前行，“1，。”表示从第一行到当前行，“d ” 表示删除。  2、如果只是想删除某一行，那么把光标指到该行，然后输入d d 即可。  
yy复制，p粘贴 n为数字  
[yy] 复制光标所在的那一行  
[nyy] 复制光标所在的向下n行， p是粘贴  
：1,3d 删除第一行到第三行  
大写+gg 调转到最后一行  
行数+gg 调转到指定行数  
：set number 显示序号
# mysql 5.7命令:
>1、创建库:create 库名  
2、创建表:create table 表名  
3、mysql> create table name(
    id int auto_increment not null primary key ,#设置为主键
    uname char(8),
    gender char(2),
    birthday date );    
4、查询数据表的结构:desc user;或show create table; 表名 \G（二选一）\G意思是显示结果更加直观。  
5、查询表字段内容：SELECT User, Host, Password FROM mysql.user;  
6、SQL 使用单引号来环绕文本值（大部分数据库系统也接受双引号）。如果是数值，请不要使用引号。文本值：(单引号用来表示字符常量)  
7、在命令行中输入\e 打开一个vi窗口  
8、设置字段不能为空：(字段名 数据类型 NOT NULL)  
9、如果创建表时忘记为id创建主键的时可以用：lter table tb_emp1 add primary key (id) 为tb_emp1 创建主键。  
10、设置多个列为主键：lter table tb_emp1 add primary key (id，name)或者在创建时后面加上PRIMARY KEY(id,name)  
11、使用唯一性约束：就是说某一列或者多列的值不能重复(在后面指定的列后面加上UNIQUE)字段名 数据类型 UNIQUE  
12、使用默认约束：就是指定某列的默认值。（字段名 数据类型 DEFAULT）  
13、设置表的属性自动增加：字段名 数据类型 UTO_INCREMENT (这个意思就是系统自动生成字段的主键值，初始值为1，每次+1，一个表只能有一个UTO_INCREMENT，且该字段必须为主键的一部分)  
14、插入信息到指定的表中的列（字段）  
insert into tb_emp2 (id,name,salary)
                             values(1,'Lucy',1000),
                             (2,'Lura',1200),
                             (3,'Kevin',1500)#注意主键值不能为空  
15、修改数据表语句：ALTER TABLE   
16、修改表名：ALTER TABLE 旧表名 RENAME 新表名  
17、修改字段的数据类型： ALTER TABLE 表名 MODIFY 字段名 数据类型  
18、修改字段名：ALTER TABLE 表名 CHANGE 旧字段名 新字段名 新数据类型  
19、添加字段：ALTER TABLE 表名 ADD 新字段名 数据类型 [FIRST | AFTER 已存在的字段名]‘FIRST’为可选参数，其作用是将新添加的字段设置为表中第一个字段；‘AFIER’其作用是将新添加的字段指定要“已存在的字段名”后面  
20、添加无完整性约束条件字段：（就是数据Null可为空）：ALTER TABLE 表名 ADD 字段名 数据类型;  
21、添加有完整性约束条件字段：（就是数据Null不能为空）：ALTER TABLE 表名 ADD 字段名 数据类型 not null;  
22、删除字段：ALTET TABLE 表名 DROP 字段名  
23、修改字段的排列位置：ALTER TABLE 表名 字段1 数据类型 FIRST | AFTER 字段2(‘FIRST’为可选参数，其作用是将‘字段1’修改为表中第一个字段；‘AFIER’其作用是将‘字段1’指定到‘字段2’的后门)  
24、更改表的存储引擎： 查看表的引擎名show create table test111 \G	show ENGINES；查看系统支持的存储引擎。修改命令是：ALTER TABLE 表名 ENGINE=更改后的存储引擎名

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
