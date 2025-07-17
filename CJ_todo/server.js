const express = require('express');
const fs = require('fs/promises');
const path = require('path');

const app = express();
const PORT = 3000;
const csvFilePath = 'todos.csv';

const { parse, stringify } = require('csv/sync');

const initializeCSV = async () => {
	try {
		await fs.access(csvFilePath);
	} catch {
		await fs.writeFile(csvFilePath, "");
	}
};

const readTodos = async () => {
	const data = await fs.readFile(csvFilePath, "utf8");
	if (!data.trim()) return [];
	return parse(data, { columns: ["id", "todo", "isComplete"], skip_empty_lines: true })
		.map(todo => ({
			id: Number(todo.id),
			todo: todo.todo,
			isComplete: todo.isComplete === "true"
		}));
};

const writeTodos = async (todos) => {
	const todosForCSV = todos.map((todo, index) => ({
		id: index + 1,
		todo: todo.todo,
		isComplete: todo.isComplete ? "true" : "false"
	}));
	const csvContent = stringify(todosForCSV, { header: false });
	await fs.writeFile(csvFilePath, csvContent);
};

app.get('/', async (req, res) => {
	const indexFile = await fs.readFile(path.join(__dirname, 'public', 'index.html'), "utf8");
	res.type('html').send(indexFile);
});

app.get('/todos', async (req, res) => {
	const todos = await readTodos();
	res.setHeader('Content-Type', 'application/json');
	res.send(JSON.stringify(todos));
});

app.post('/todos', (req, res) => {
	let body = "";
	req.on("data", chunk => {
		body += chunk;
	});

	req.on("end", async () => {
		const data = JSON.parse(body);
		const todos = await readTodos();

		if (data.hasOwnProperty("index")) {
			const index = parseInt(data.index);
			if (index >= 0 && index < todos.length) {
				todos[index].isComplete = data.isComplete;
				await writeTodos(todos);
				res.send();
			} else {
				res.send("Invalid index");
			}
		} else {
			todos.push({
				todo: data.todo, isComplete: data.isComplete
			});
			await writeTodos(todos);
			res.send();
		}
	});
});

initializeCSV().then(() => {
	app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
});

