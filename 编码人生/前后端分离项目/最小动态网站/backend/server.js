const express=require('express');
const sqlite3=require('sqlite3').verbose();
const cors=require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const db=new sqlite3.Database('./backend/database.db');

//创建表
db.run(`CREATE TABLE IF NOT EXISTS users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT
	)`);

//获取用户列表
app.get('/api/users',(req,res)=>{
	db.all("SELECT * FROM users",(err,rows)=>{
		if(err) return res.status(500).send(err);
		res.json(rows);
	});
});

//添加用户
app.post('/api/users',(req,res)=>{
	const {name}=req.body;
	db.run("insert into users (name) values (?)",[name],function(err){
		if(err) return res.status(500).send(err);
		res.json({id:this.lastID,name});
	});
	
});

app.listen(3000,()=>console.log('Server running at http://localhost:3000'));
