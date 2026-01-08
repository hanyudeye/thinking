const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const ADMIN_USER = 'admin';
const ADMIN_PASS = '123456';
const TOKEN = 'fixed-token';

// 模拟数据库
let forms = [];

// 登录接口
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === ADMIN_USER && password === ADMIN_PASS) {
        return res.json({ success: true, token: TOKEN });
    }
    res.status(401).json({ success: false, message: '账号或密码错误' });
});

// 提交表单
app.post('/form/add', (req, res) => {
    const { name, phone, message } = req.body;
    if (!name || !phone) {
        return res.status(400).json({ success: false, message: '姓名和电话必填' });
    }
    const newForm = { id: Date.now(), name, phone, message: message || '' };
    forms.push(newForm);
    res.json({ success: true, data: newForm });
});

// 获取表单列表
app.get('/form/list', (req, res) => {
    if (req.headers.authorization !== `Bearer ${TOKEN}`) {
        return res.status(403).json({ success: false, message: '未授权' });
    }
    res.json({ success: true, data: forms });
});

// 删除表单
app.delete('/form/delete/:id', (req, res) => {
    if (req.headers.authorization !== `Bearer ${TOKEN}`) {
        return res.status(403).json({ success: false, message: '未授权' });
    }
    const id = parseInt(req.params.id);
    forms = forms.filter(f => f.id !== id);
    res.json({ success: true });
});

app.listen(3000, () => console.log('✅ 后端服务运行中：http://localhost:3000'));
