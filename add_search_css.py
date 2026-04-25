def add_css():
    css_to_add = """
/* TYBA CONTAINER & SEARCH BAR */
.tyba-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

.tyba-search-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
}

.search-box {
  position: relative;
  width: 70%;
  max-width: 800px;
}

.search-box .search-icon {
  position: absolute;
  left: 25px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.5rem;
  color: var(--accent-cyan);
  pointer-events: none;
}

#tyba-search {
  width: 100%;
  padding: 20px 30px 20px 70px;
  background: rgba(0, 40, 60, 0.6);
  border: 2px solid rgba(0, 245, 255, 0.4);
  border-radius: 50px;
  color: #fff;
  font-family: var(--font-main);
  font-size: 1.2rem;
  outline: none;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 0 30px rgba(0, 245, 255, 0.15);
}

#tyba-search:focus {
  border-color: var(--accent-cyan);
  background: rgba(0, 245, 255, 0.15);
  box-shadow: 0 0 50px rgba(0, 245, 255, 0.5);
  transform: scale(1.02);
}

#tyba-search::placeholder {
  color: rgba(255, 255, 255, 0.5);
}
"""
    with open("src/style.css", "r", encoding="utf-8") as f:
        css = f.read()
        
    if "TYBA CONTAINER" not in css:
        with open("src/style.css", "a", encoding="utf-8") as f:
            f.write(css_to_add)
        print("Search CSS added successfully.")
    else:
        print("Search CSS already exists.")

if __name__ == "__main__":
    add_css()
