const http = require('http');


http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain;charset=utf-8' });
    // res.writeHead(200, { 'Content-Type': 'text/plain;charset=utf-8' });
    res.end('Hello World你好世界\n');
}).listen(8080, () => {
    console.log('Server running at http://xx');
})


