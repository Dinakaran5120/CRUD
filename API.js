const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

let users = [];
let nextID = 1;

app.get('/user', (req, res) => {
    res.json(users);
});

app.get('/user/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
});

app.post('/user', (req, res) => {
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).json({ error: 'Name and Email are required' });
    }
    const newUser = {
        id: nextID++,
        name,
        email
    };
    users.push(newUser);
    res.status(201).json(newUser);
});

app.put('/user/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({ error: 'User not found' });
    }
    const { name, email } = req.body;
    if (name) user.name = name;
    if (email) user.email = email;
    res.json(user);
});

app.delete('/user/:id', (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    if (index === -1) {
        return res.status(404).json({ error: 'User not found' });
    }
    users.splice(index, 1);
    res.status(204).send();
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
