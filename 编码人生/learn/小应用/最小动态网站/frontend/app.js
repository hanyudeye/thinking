const apiUrl = "http://localhost:3000/api/users";

async function fetchUsers() {

    const res = await fetch(apiUrl);
    const users = await res.json();
    const list = document.getElementById('userList');
    list.innerHTML = '';
    users.forEach(u => {
        const li = document.createElement('li');
        li.textContent = u.name;
        list.appendChild(li);
    });
}

async function addUser() {

    const name = document.getElementById('userName').value;
    if (!name) return alert("请输入用户名");
    await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name })
    });
    document.getElementById('userName').value = '';
    fetchUsers();
}

//初始加载
fetchUsers();
