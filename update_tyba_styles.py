import re

def update_css():
    with open('src/style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    new_styles = """
/* =============================================
   APRENDE TYBA NEURAL MAP STYLES
   ============================================= */
#view-tyba {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  overflow: hidden;
}

.tyba-search-container {
  padding: 20px 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  background: rgba(10, 15, 25, 0.85);
  border-bottom: 1px solid rgba(0, 245, 255, 0.2);
  z-index: 10;
}

.tyba-search-bar {
  width: 100%;
  max-width: 600px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(0, 245, 255, 0.4);
  border-radius: 30px;
  padding: 15px 25px 15px 50px;
  color: #fff;
  font-family: var(--font-main);
  font-size: 1.1rem;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(0, 245, 255, 0.1);
}

.tyba-search-bar:focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 25px rgba(0, 245, 255, 0.3);
  background: rgba(0, 20, 30, 0.8);
}

.tyba-search-icon {
  position: absolute;
  left: calc(50% - 280px); /* Approx position */
  font-size: 1.2rem;
  pointer-events: none;
}
@media (max-width: 768px) {
  .tyba-search-icon {
    left: 60px;
  }
}

.tyba-brain-grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 30px;
  padding: 40px;
  overflow-y: auto;
  align-content: flex-start;
}

.tyba-brain-grid::-webkit-scrollbar {
  width: 8px;
}
.tyba-brain-grid::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}
.tyba-brain-grid::-webkit-scrollbar-thumb {
  background: var(--accent-cyan);
  border-radius: 4px;
}

/* Modal Curso TYBA */
.tyba-course-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 5, 10, 0.9);
  backdrop-filter: blur(8px);
  z-index: 3000;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 1;
  transition: opacity 0.3s ease;
}

.tyba-course-modal.hidden {
  opacity: 0;
  pointer-events: none;
}

.tyba-modal-content {
  width: 90%;
  max-width: 800px;
  max-height: 85vh;
  background: rgba(10, 15, 25, 0.95);
  border: 1px solid rgba(0, 245, 255, 0.3);
  border-radius: 16px;
  box-shadow: 0 0 40px rgba(0, 245, 255, 0.15);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transform: scale(1);
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.tyba-course-modal.hidden .tyba-modal-content {
  transform: scale(0.9);
}

.tyba-modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  color: var(--text-dim);
  font-size: 1.5rem;
  cursor: pointer;
  transition: color 0.2s;
  z-index: 10;
}
.tyba-modal-close:hover {
  color: var(--accent-cyan);
}

.tyba-modal-header {
  padding: 30px;
  background: linear-gradient(180deg, rgba(0, 245, 255, 0.1), transparent);
  border-bottom: 1px solid rgba(0, 245, 255, 0.2);
  display: flex;
  align-items: center;
  gap: 20px;
}

.tyba-modal-icon {
  font-size: 3rem;
  filter: drop-shadow(0 0 15px var(--accent-cyan));
}

.tyba-modal-subtitle {
  display: block;
  font-family: var(--font-main);
  color: var(--accent-green);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 2px;
  margin-bottom: 5px;
}

.tyba-modal-title {
  font-family: var(--font-header);
  color: #fff;
  font-size: 1.8rem;
  text-shadow: 0 0 15px rgba(0, 245, 255, 0.5);
  line-height: 1.2;
}

.tyba-modal-body {
  padding: 30px;
  overflow-y: auto;
  flex: 1;
}

.tyba-modal-body::-webkit-scrollbar {
  width: 6px;
}
.tyba-modal-body::-webkit-scrollbar-track {
  background: transparent;
}
.tyba-modal-body::-webkit-scrollbar-thumb {
  background: var(--accent-cyan);
  border-radius: 3px;
}

.tyba-course-step {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-left: 4px solid var(--accent-cyan);
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 25px;
}

.tyba-course-step-num {
  font-family: var(--font-header);
  color: var(--accent-cyan);
  font-size: 1.1rem;
  margin-bottom: 10px;
  display: block;
}

.tyba-course-step-title {
  color: #fff;
  font-family: var(--font-main);
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 15px;
}

.tyba-course-step-text {
  color: var(--text-dim);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

.tyba-course-step-tip {
  background: rgba(255, 170, 0, 0.1);
  border: 1px solid rgba(255, 170, 0, 0.3);
  padding: 12px 15px;
  border-radius: 6px;
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.tyba-course-step-tip::before {
  content: '💡';
  font-size: 1.2rem;
}

.tyba-course-step-tip p {
  color: #ffaa00;
  font-size: 0.9rem;
  margin: 0;
  line-height: 1.4;
}
"""

    start_str = '/* =============================================\n   APRENDE TYBA STYLES'
    
    start_idx = content.find(start_str)

    if start_idx != -1:
        new_content = content[:start_idx] + new_styles
        with open('src/style.css', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated style.css successfully")
    else:
        print("Could not find TYBA styles start string in style.css")

if __name__ == '__main__':
    update_css()
