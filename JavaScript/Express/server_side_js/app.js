const bodyParser = require('body-parser');
const express = require('express');
const { get } = require('underscore');
const app = express();

app.locals.pretty = true;
app.set('view engine', 'jade');
app.set('views', './views');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:false}));
app.get('/topic/:id', function(req, res){
    const topics = [
    'javascript is ...', 
    'nodejs is ...', 
    'express is ...'
    ];
    const output = `
    <a href="/topic/0">JavaScript</a><br>
    <a href="/topic/1">NodeJs</a><br>
    <a href="/topic/2">Express</a><br>
    ${topics[req.params.id]}
    `
    res.send(output);
});
app.get('/form', function(req, res){
    res.render('form');
});
app.get('/form_reciever', function(req, res){
    const title = req.query.title;
    const description = req.query.description;
    res.send(title+','+description);
})
app.post('/form_reciever', function(req, res){
    const title = req.body.title;
    const description = req.body.description;
    res.send(title+','+description);
})
app.get('/topic/:id/:mode', function(req, res){
    res.send(req.params.id+','+req.params.mode);
});
app.get('/template', function(req, res){
    res.render('temp', {time:Date(), title:'Jade'});
});
app.get('/', function(req, res){
    res.send("Hello homepage");
});
app.get('/login', function(req, res){
    res.send("Log in please");
});
app.get('/route', function(req, res){
    res.send('Hello router, <img src = "/1.jpg">');
});
app.get('/dynamic', function(req, res){
    const output = `
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
        </head>
        <body>
            hello, dynamic
        </body>
        </html>
    `
    res.send(output);
})
app.listen(3000, function(){
    console.log("connected 3000 port!");
});
