const express = require('express');
const app = express();
const Port = 3000;
app.use(express.json());
app.get('/user',(req,res)=>{res.json(user);});
app.get('/user/:id', (req,res)=>{
    const user = users.find(u => u.id === parseInt(req.params.id));
    if(!user) return res.status(404).json({error:'user not found'});
});
app.post('/user',(req,res)=>{
    const {name,email} = req.body;
    if(!name||!email){return res.status(404).json({error:'Name and Email are required'});}
    const user ={id: nextID++,name,email};
    users.push(user);
    res.status(201).json(user);
});
app.put('/user/:id', (req,res)=>{
    const user = users.find(u => u.id === parseInt(req.params.id));
    if(!user) return res.status(404).json({error:'user not found'});
    const{name,email}=req.body;
    if (name) user.name = name;
    if (email) user.email = email;
    res.json(user);
});
app.delete('/user/:id', (req,res)=>{
    const user = users.find(u => u.id === parseInt(req.params.id));
    if(user === -1) return res.status(404).json({error:'user not found'});
    users.splice(user, 1);
    res.status(204).send();

});

app.listen(Port,()=>{console.log(`server running at http://localhost:${Port}`);});
