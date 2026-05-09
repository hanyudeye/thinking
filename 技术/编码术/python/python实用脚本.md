4.2通过电子邮件发送文件附件
``` py
# Python script to send emails with file attachments
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def send_email_with_attachment(sender_email,sender_password, recipient_email, subject, body, file_path):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {file_path}")
        message.attach(part)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
```
说明：

此 Python 脚本允许您发送带有文件附件的电子邮件。只需提供发件人的电子邮件、密码、收件人的电子邮件、主题、正文以及要附加的文件的路径。



4.3自动邮件提醒
```
# Python script to send automatic email reminders
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
def send_reminder_email(sender_email, sender_password, recipient_email, subject, body, reminder_date):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    now = datetime.now()
    reminder_date = datetime.strptime(reminder_date, '%Y-%m-%d')
    if now.date() == reminder_date.date():
        message = MIMEText(body, 'plain')
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
```
说明：

此Python脚本根据指定日期发送自动电子邮件提醒。它对于设置重要任务或事件的提醒非常有用，确保您不会错过最后期限。

5.自动化Excel电子表格
5.1Excel读&写
``` py
# Python script to read and write data to an Excel spreadsheet
import pandas as pd
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df
def write_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
```
说明：

此Python脚本使用pandas库从Excel电子表格读取数据并将数据写入新的Excel文件。它允许您通过编程处理Excel文件，使数据操作和分析更加高效。

5.2数据分析和可视化
```
# Python script for data analysis and visualization with pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
def analyze_and_visualize_data(data):
# Your code here for data analysis and visualization
    pass
```
说明：

此Python脚本使用pandas和matplotlib库来进行数据分析和可视化。它使您能够探索数据集、得出结论并得到数据的可视化表示。

5.3合并多个工作表
```
# Python script to merge multiple Excel sheets into a single sheet
import pandas as pd
def merge_sheets(file_path, output_file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.DataFrame()
    for sheet_name in xls.sheet_names:
        sheet_df = pd.read_excel(xls, sheet_name)
        df = df.append(sheet_df)
        df.to_excel(output_file_path, index=False)
```
说明：

此Python脚本将Excel文件中多个工作表的数据合并到一个工作表中。当您将数据分散在不同的工作表中但想要合并它们以进行进一步分析时，这会很方便。

6.与数据库交互
6.1连接到一个数据库
```
# Python script to connect to a database and execute queries
import sqlite3
def connect_to_database(database_path):
    connection = sqlite3.connect(database_path)
    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
```


说明：

此Python脚本允许您连接到SQLite数据库并执行查询。您可以使用适当的Python数据库驱动程序将其调整为与其他数据库管理系统（例如MySQL或PostgreSQL）配合使用。

6.2执行SQL查询
```
# Python script to execute SQL queries on a database
import sqlite3
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
```
说明：

此Python脚本是在数据库上执行SQL查询的通用函数。您可以将查询作为参数与数据库连接对象一起传递给函数，它将返回查询结果。

6.3数据备份与恢复
```
import shutil
def backup_database(database_path, backup_directory):
    shutil.copy(database_path, backup_directory)
def restore_database(backup_path, database_directory):
    shutil.copy(backup_path, database_directory)
```
说明：

此Python 脚本允许您创建数据库的备份并在需要时恢复它们。这是预防您的宝贵数据免遭意外丢失的措施。

7.社交媒体自动化
7.1发送个性化电子邮件
```
# Python script to automate posting on Twitter and Facebook
from twython import Twython
import facebook
def post_to_twitter(api_key, api_secret, access_token, access_token_secret, message):
    twitter = Twython(api_key, api_secret, access_token, access_token_secret)
    twitter.update_status(status=message)
def post_to_facebook(api_key, api_secret, access_token, message):
    graph = facebook.GraphAPI(access_token)
    graph.put_object(parent_object='me', connection_name='feed', message=message)
```
说明：

此 Python 脚本利用Twython和facebook-sdk库自动在Twitter和Facebook上发布内容。您可以使用它将 Python 脚本中的更新、公告或内容直接共享到您的社交媒体配置文件。

7.2社交媒体自动共享
```
# Python script to automatically share content on social media platforms
import random
def get_random_content():
# Your code here to retrieve random content from a list or database
pass
def post_random_content_to_twitter(api_key, api_secret, access_token, access_token_secret):
content = get_random_content()
post_to_twitter(api_key, api_secret, access_token, access_token_secret, content)
def post_random_content_to_facebook(api_key, api_secret, access_token):
content = get_random_content()
post_to_facebook(api_key, api_secret, access_token, content)
```
说明：

此Python 脚本自动在Twitter和Facebook上共享随机内容。您可以对其进行自定义，以从列表或数据库中获取内容并定期在社交媒体平台上共享。

7.3 抓取社交媒体数据
```
# Python script for scraping data from social media platforms
import requests
def scrape_social_media_data(url):
    response = requests.get(url)
# Your code here to extract relevant data from the response
```
说明：

此Python脚本执行网页抓取以从社交媒体平台提取数据。它获取所提供URL的内容，然后使用BeautifulSoup等技术来解析HTML并提取所需的数据。

8.自动化系统任务
8.1管理系统进程
```
# Python script to manage system processes
import psutil
def get_running_processes():
return [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
def kill_process_by_name(process_name):
for p in psutil.process_iter(['pid', 'name', 'username']):
if p.info['name'] == process_name:
p.kill()
```
说明：

此Python 脚本使用 psutil 库来管理系统进程。它允许您检索正在运行的进程列表并通过名称终止特定进程。

8.2使用 Cron 安排任务
```
# Python script to schedule tasks using cron syntax
from crontab import CronTab
def schedule_task(command, schedule):
cron = CronTab(user=True)
job = cron.new(command=command)
job.setall(schedule)
cron.write()
```
说明：

此Python 脚本利用 crontab 库来使用 cron 语法来安排任务。它使您能够定期或在特定时间自动执行特定命令。

8.3自动邮件提醒
```
# Python script to monitor disk space and send an alert if it's low
import psutil
def check_disk_space(minimum_threshold_gb):
disk = psutil.disk_usage('/')
free_space_gb = disk.free / (230) # Convert bytes to GB
if free_space_gb < minimum_threshold_gb:
# Your code here to send an alert (email, notification, etc.)
pass
```
说明：

此Python 脚本监视系统上的可用磁盘空间，并在其低于指定阈值时发送警报。它对于主动磁盘空间管理和防止由于磁盘空间不足而导致潜在的数据丢失非常有用。

9.自动化图像编辑
9.1图像大小调整和裁剪
```
# Python script to resize and crop images
from PIL import Image
def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(output_path)
def crop_image(input_path, output_path, left, top, right, bottom):
    image = Image.open(input_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)
```
说明：

此Python脚本使用Python图像库(PIL)来调整图像大小和裁剪图像。它有助于为不同的显示分辨率或特定目的准备图像。

9.2为图像添加水印
```
# Python script to add watermarks to images
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
def add_watermark(input_path, output_path, watermark_text):
image = Image.open(input_path)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', 36)
draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)
image.save(output_path)
```
说明：

此Python 脚本向图像添加水印。您可以自定义水印文本、字体和位置，以实现您图像的个性化。

9.3创建图像缩略图

```
# Python script to create image thumbnails
from PIL import Image
def create_thumbnail(input_path, output_path, size=(128, 128)):
image = Image.open(input_path)
image.thumbnail(size)
image.save(output_path)
```
说明：

此Python 脚本从原始图像创建缩略图，这对于生成预览图像或减小图像大小以便更快地在网站上加载非常有用。

结论


以上是本文为您介绍的9个可以用于工作自动化的最佳Python脚本。在下篇中，我们将为您介绍网络自动化、数据清理和转换、自动化 PDF 操作、自动化GUI、自动化测试、自动化云服务、财务自动化、自然语言处理。

自动化不仅可以节省时间和精力，还可以降低出错风险并提高整体生产力。通过自定义和构建这些脚本，您可以创建定制的自动化解决方案来满足您的特定需求。

还等什么呢？立即开始使用Python 实现工作自动化，体验简化流程和提高效率的力量。


作者：Abdul Hannan Hassan
在现代职场中，重复性和耗时的任务常常占据大量时间，影响工作效率。Python作为一种高效、易用的编程语言，提供了丰富的库和工具，能够帮助打工人自动化处理日常任务，提升工作效率。以下是5个必备的Python自动化脚本：

一、文件批量重命名脚本
在日常工作中，可能需要对大量文件进行重命名操作。手动操作既耗时又容易出错。使用Python脚本，可以实现文件的批量重命名，提高效率。

   import os
    def batch_rename(directory, old_ext, new_ext):
        for filename in os.listdir(directory):
            if filename.endswith(old_ext):
                new_filename = filename.replace(old_ext, new_ext)
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

    # 示例：将目录中所有“.txt”扩展名的文件改为“.md”
    batch_rename('/path/to/directory', '.txt', '.md')

此脚本遍历指定目录下的所有文件，将符合条件的文件扩展名进行替换。这种方法比手动操作更为高效，特别是在文件数量庞大的情况下。

二、数据清洗脚本
处理大型数据集时，数据清洗是不可避免的步骤。编写一个Python脚本，自动进行常见的数据清洗操作，例如去重、缺失值处理等。

    import pandas as pd
    
    def data_cleaning(data_path):
        df = pd.read_csv(data_path)
    
        # 去重
        df = df.drop_duplicates()
    
        # 处理缺失值
        df = df.dropna()
    
        # 其他数据清洗操作...
    
        df.to_csv('cleaned_data.csv', index=False)
    
    # 示例：对数据集进行清洗并保存
    data_cleaning('/path/to/data.csv')

此脚本使用了pandas库，能够高效地对数据进行清洗操作，确保数据质量，为后续分析奠定基础。

三、网络请求脚本
与网络交互时，编写一个能够发送HTTP请求的脚本是非常有用的。使用requests库可以轻松实现。

    import requests
    
    def make_request(url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    # 示例：向GitHub API发送请求
    github_data = make_request('https://api.github.com/users/octocat')
    print(github_data)
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
通过此脚本，可以方便地与各种API进行交互，获取所需的数据，应用范围广泛。

四、日志分析脚本
日志分析对于了解系统运行状况至关重要。编写一个脚本，能够解析和分析日志文件，提取关键信息。

    import re
    
    def analyze_logs(log_path):
        with open(log_path, 'r') as file:
            logs = file.readlines()
    
        error_count = 0
        for log in logs:
            if re.search('error', log, re.IGNORECASE):
                error_count += 1
    
        print(f"Total errors: {error_count}")
    
    # 示例：分析日志文件中的错误数量
    analyze_logs('/path/to/logs.txt')
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
此脚本能够快速统计日志中的错误数量，帮助及时发现和解决问题，确保系统稳定运行。

五、批量处理图像脚本
图像处理是许多工作中的重要一环。编写一个脚本，可以批量处理图像，例如缩放、旋转等。

    from PIL import Image
    import os
    
    def batch_process_images(input_dir, output_dir, size=(300, 300)):
        for filename in os.listdir(input_dir):
            img_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
    
            img = Image.open(img_path)
            img.thumbnail(size)
            img.save(output_path)
    
    # 示例：批量处理图像，将其缩放至300x300像素
    batch_process_images('/path/to/input_images', '/path/to/output_images')
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
使用PIL库，可以方便地对图像进行各种处理，满足不同的需求。