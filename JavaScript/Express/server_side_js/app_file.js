// 이거 다 이해하기!!!!
// 이거 다 이해하기!!!!
// 이거 다 이해하기!!!!
// 이거 다 이해하기!!!!

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');
const { send, title } = require('process');
app.use(bodyParser.urlencoded({extended:false}));
app.locals.pretty = true;
app.set('views', './views_file');
app.set('view engine', 'jade');


app.get('/topic/new', function(req, res){
    fs.readdir('data', function(err, files){
        if(err){
            console.log(err);
            res.status(500).send('error!');
        }
    res.render('new', {topics:files});
    });
});
app.get(['/topic', '/topic/:id'], function(req, res){
    fs.readdir('data', function(err, files){
        if(err){
            console.log(err);
            res.status(500).send('error!');
        }
        const id = req.params.id;
        // when id exists
        if (id){
        fs.readFile('data/'+id, 'utf8', function(err, data){
            if(err){
                console.log(err);
                res.status(500).send('server err');
            }
            res.render('view', {title:id, topics:files, description:data});
        });
        }
        // no id
        else {
        res.render('view', {topics:files, title:'welcome', description:'hello javascript'});
        }
    });
});

app.post('/topic', function(req,res){
    const title = req.body.title;
    const description = req.body.description;
    fs.writeFile('data/'+title,description,function(err){
        if(err){
            console.log(err);
            res.status(500).send('server err');
        }
        res.redirect('/topic/'+title);

    });
});


app.listen(3000, function(){
    console.log('connected, 3000 port');
});