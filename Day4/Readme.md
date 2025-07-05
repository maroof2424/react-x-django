# Day 4

### 🧠 1. What is Git & GitHub? (10 min)

* **Git** = Local version control system
* **GitHub** = Cloud platform to host and collaborate on Git repositories
* Helps you track changes, collaborate, and manage code.

---

### 🛠️ 2. Git Installation (10 min)

* [Download Git](https://git-scm.com/downloads)
* After installing, run:

  ```bash
  git --version
  ```

---

### ⚙️ 3. Git Configuration (5 min)

```bash
git config --global user.name "Maroof"
git config --global user.email "your_email@example.com"
```

---

### 📂 4. Initialize Git Repo (10 min)

```bash
mkdir my-project
cd my-project
git init
```

---

### 📌 5. Git Commands: First Commit (20 min)

```bash
touch index.html
git status            # see changes
git add index.html    # stage changes
git commit -m "First commit"  # save snapshot
```

---

### 🌐 6. Create GitHub Repository (5 min)

* Go to [https://github.com](https://github.com)
* Click **"New Repository"**
* Name: `my-project`, keep it public, no README (you’ll push from local)

---

### 🔗 7. Connect Local Repo to GitHub (10 min)

```bash
git remote add origin https://github.com/your_username/my-project.git
git branch -M main
git push -u origin main
```

---

### 🔄 8. Everyday Git Commands (10 min)

```bash
git add .
git commit -m "Your message"
git push
```

---

### 📚 9. Learn GitHub README & .gitignore (Optional but useful)

* `README.md` – Write project description
* `.gitignore` – Ignore files (e.g., `*.env`, `__pycache__/`, `node_modules/`)

---

### 📦 Bonus: Use GitHub in VS Code (Optional)

* Install **GitHub Pull Requests** and **GitLens** extensions

