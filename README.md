# To-Do List Application

A modern, minimalist to-do list application with both a desktop GUI (Tkinter) and a web-based frontend.

## Features

- ✅ **Add/Delete Tasks** - Create and manage your daily tasks
- 🎯 **Task Tracking** - Monitor total, completed, and pending tasks
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 💾 **Persistent Storage** - Your tasks are saved locally (browser localStorage or JSON file)
- 🎨 **Modern UI** - Clean, attractive minimalist design
- 🏷️ **Filter Tasks** - View all, active, or completed tasks
- ⌨️ **Keyboard Support** - Press Enter to add tasks, Delete to remove selected tasks

## Installation & Usage

### Web Frontend (HTML/CSS/JavaScript)

Simply open `index.html` in your web browser. No server or installation needed!

**Features:**
- Tasks stored in browser localStorage
- Automatic filtering and statistics
- Beautiful gradient background
- Smooth animations and transitions

### Desktop Application (Tkinter)

**Requirements:**
```bash
python 3.x (tkinter is included with Python)
```

**Run the application:**
```bash
python ToDoList.py
```

**Features:**
- Professional desktop GUI
- Persistent storage in JSON format
- Double-click to toggle task completion
- Delete key to remove selected tasks
- Real-time statistics

## Files Description

- `index.html` - Web frontend HTML structure
- `style.css` - Web frontend styling with gradients and modern design
- `script.js` - Web frontend functionality and localStorage management
- `ToDoList.py` - Desktop application using Tkinter GUI

## Usage Tips

### Web Version
1. Type your task in the input field
2. Press Enter or click the + button to add
3. Click the checkbox to mark as completed
4. Use filter buttons (All, Active, Completed) to organize
5. Click the trash icon to delete individual tasks
6. Use "Clear Completed" to remove all completed tasks

### Desktop Version
1. Enter a task and press Enter or click "Add"
2. Double-click a task to mark it as completed
3. Select a task and press Delete or click "Delete Selected"
4. Click "Clear Completed" to remove all completed tasks
5. Tasks are automatically saved to `tasks.json`

## Design Highlights

- **Color Scheme:** Purple gradient background with modern UI elements
- **Typography:** Clean, readable system fonts
- **Spacing:** Comfortable padding and margins for easy reading
- **Icons:** Font Awesome integration for visual clarity
- **Animations:** Smooth transitions and slide effects
- **Mobile Friendly:** Responsive layout adapts to all screen sizes

## Browser Compatibility

The web version works on:
- Chrome/Chromium
- Firefox
- Safari
- Edge
- All modern mobile browsers

## License

Free to use and modify.

## Author

Created as a task management solution with minimalist design principles.
