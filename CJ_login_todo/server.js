const express = require("express");
const sqlite3 = require("sqlite3");
const path = require("path");

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
	res.redirect('/register.html');
});

const db = new sqlite3.Database("./database.db", (err) => {
	if (err) {
		return console.error("Database connection error:", err.message);
	}
	console.log("Connected to SQLite database.");
});

db.run(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  password TEXT NOT NULL
)`);

db.run(`CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  todo TEXT NOT NULL,
  isComplete INTEGER NOT NULL DEFAULT 0
)`);

app.post("/register", (req, res) => {
	const { name, password } = req.body;
	if (!name || !password) {
		return res.status(400).json({ error: "Please provide both name and password." });
	}
  	const query = "INSERT INTO users (name, password) VALUES (?, ?)";
  	db.run(query, [name, password], function (err) {
    	if (err) {
		console.error("Error inserting user:", err.message);
      		return res.status(500).json({ error: "Database error." });
	}
		console.log("User registered:", { id: this.lastID, name });
    		res.json({ message: "Registration successful", userId: this.lastID });
	});
});

app.post("/login", (req, res) => {
	const { name, password } = req.body;
  	if (!name || !password) {
		return res.status(400).json({ error: "Please provide both name and password." });
	}
	const query = "SELECT * FROM users WHERE name = ? AND password = ?";
  	db.get(query, [name, password], (err, row) => {
    	if (err) {
      		console.error("Error querying user:", err.message);
      		return res.status(500).json({ error: "Database error." });
	}
		if (row) {
			res.json({ message: "Login successful", user: row });
		} else {
      			res.status(401).json({ error: "Invalid credentials." });
		}
	});
});

app.get("/todos", (req, res) => {
	const query = "SELECT * FROM todos";
	db.all(query, [], (err, rows) => {
		if (err) {
			console.error("Error fetching todos:", err.message);
			return res.status(500).json({ error: "Database error." });
		}
		res.json(rows);
	});
});

app.post("/todos", (req, res) => {
	if (req.body.id && typeof req.body.isComplete !== "undefined") {
		const { id, isComplete } = req.body;
    		const query = "UPDATE todos SET isComplete = ? WHERE id = ?";
    		db.run(query, [isComplete ? 1 : 0, id], function (err) {
			if (err) {
				console.error("Error updating todo:", err.message);
        			return res.status(500).json({ error: "Database error." });
			}
			res.json({ message: "Todo updated" });
		});
	} else {
		const { todo, isComplete } = req.body;
		if (!todo) {
			return res.status(400).json({ error: "Please provide a todo text." });
		}
		const query = "INSERT INTO todos (todo, isComplete) VALUES (?, ?)";
    		db.run(query, [todo, isComplete ? 1 : 0], function (err) {
			if (err) {
				console.error("Error inserting todo:", err.message);
				return res.status(500).json({ error: "Database error." });
			}
			res.json({ message: "Todo added", todoId: this.lastID });
		});
	}
});

app.listen(port, () => {
	console.log(`Server is running on http://localhost:${port}`);
});
