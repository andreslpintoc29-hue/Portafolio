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
  padding: 30px 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  background: rgba(10, 15, 25, 0.95);
  border-bottom: 2px solid rgba(0, 245, 255, 0.2);
  z-index: 10;
  box-shadow: 0 4px 20px rgba(0,0,0,0.5);
}

.tyba-search-bar {
  width: 100%;
  max-width: 800px;
  background: rgba(0, 0, 0, 0.6);
  border: 2px solid rgba(0, 245, 255, 0.5);
  border-radius: 40px;
  padding: 20px 30px 20px 60px;
  color: #fff;
  font-family: var(--font-main);
  font-size: 1.3rem;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 20px rgba(0, 245, 255, 0.15);
}

.tyba-search-bar:focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 35px rgba(0, 245, 255, 0.4);
  background: rgba(0, 20, 30, 0.9);
}

.tyba-search-bar::placeholder {
  color: rgba(255,255,255,0.4);
}

.tyba-search-icon {
  position: absolute;
  left: calc(50% - 370px);
  font-size: 1.8rem;
  pointer-events: none;
  color: var(--accent-cyan);
}
@media (max-width: 768px) {
  .tyba-search-icon {
    left: 60px;
  }
}

.tyba-dashboard {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 40px;
  overflow-y: auto;
  align-items: center;
  background: rgba(5, 10, 15, 0.8);
}

.tyba-dashboard::-webkit-scrollbar {
  width: 10px;
}
.tyba-dashboard::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}
.tyba-dashboard::-webkit-scrollbar-thumb {
  background: var(--accent-cyan);
  border-radius: 5px;
}

/* Tarjetas de Registro */
.tyba-card {
  width: 100%;
  max-width: 900px;
  background: linear-gradient(135deg, rgba(20, 30, 45, 0.9), rgba(10, 15, 25, 0.9));
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-left: 5px solid var(--accent-cyan);
  border-radius: 12px;
  padding: 25px 35px;
  display: flex;
  align-items: center;
  gap: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.tyba-card:hover {
  transform: translateX(10px) translateY(-2px);
  border-color: rgba(0, 245, 255, 0.5);
  box-shadow: 0 10px 30px rgba(0, 245, 255, 0.2);
  background: linear-gradient(135deg, rgba(30, 45, 65, 0.9), rgba(15, 25, 40, 0.9));
}

.tyba-card-icon {
  font-size: 3.5rem;
  filter: drop-shadow(0 0 10px var(--accent-cyan));
  flex-shrink: 0;
}

.tyba-card-content {
  flex: 1;
}

.tyba-card-cat {
  display: inline-block;
  background: rgba(0, 255, 136, 0.15);
  color: var(--accent-green);
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.tyba-card-title {
  color: #fff;
  font-family: var(--font-header);
  font-size: 1.6rem;
  margin-bottom: 10px;
  text-shadow: 0 0 10px rgba(0, 245, 255, 0.3);
}

.tyba-card-desc {
  color: var(--text-dim);
  font-size: 1.05rem;
  line-height: 1.5;
}

.tyba-card-action {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  color: var(--accent-cyan);
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 1px;
}

.tyba-arrow {
  font-size: 2rem;
  transition: transform 0.3s;
}

.tyba-card:hover .tyba-arrow {
  transform: translateX(10px);
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
  max-width: 900px;
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
  font-size: 3.5rem;
  filter: drop-shadow(0 0 15px var(--accent-cyan));
}

.tyba-modal-subtitle {
  display: block;
  font-family: var(--font-main);
  color: var(--accent-green);
  font-size: 1rem;
  font-weight: 800;
  letter-spacing: 2px;
  margin-bottom: 5px;
}

.tyba-modal-title {
  font-family: var(--font-header);
  color: #fff;
  font-size: 2.2rem;
  text-shadow: 0 0 15px rgba(0, 245, 255, 0.5);
  line-height: 1.2;
}

.tyba-modal-body {
  padding: 40px;
  overflow-y: auto;
  flex: 1;
}

.tyba-modal-body::-webkit-scrollbar {
  width: 8px;
}
.tyba-modal-body::-webkit-scrollbar-track {
  background: transparent;
}
.tyba-modal-body::-webkit-scrollbar-thumb {
  background: var(--accent-cyan);
  border-radius: 4px;
}

.tyba-course-step {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-left: 4px solid var(--accent-cyan);
  border-radius: 8px;
  padding: 25px;
  margin-bottom: 25px;
}

.tyba-course-step-num {
  font-family: var(--font-header);
  color: var(--accent-cyan);
  font-size: 1.2rem;
  margin-bottom: 10px;
  display: block;
}

.tyba-course-step-title {
  color: #fff;
  font-family: var(--font-main);
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 15px;
}

.tyba-course-step-text {
  color: var(--text-dim);
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 20px;
}

.tyba-course-step-tip {
  background: rgba(255, 170, 0, 0.1);
  border: 1px solid rgba(255, 170, 0, 0.3);
  padding: 15px 20px;
  border-radius: 6px;
  display: flex;
  gap: 15px;
  align-items: flex-start;
}

.tyba-course-step-tip::before {
  content: '💡';
  font-size: 1.5rem;
}

.tyba-course-step-tip p {
  color: #ffaa00;
  font-size: 1rem;
  margin: 0;
  line-height: 1.5;
}
"""

    start_str = '/* =============================================\n   APRENDE TYBA NEURAL MAP STYLES'
    
    start_idx = content.find(start_str)

    if start_idx != -1:
        new_content = content[:start_idx] + new_styles
        with open('src/style.css', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated style.css successfully with cards styles.")
    else:
        print("Could not find TYBA styles start string in style.css")

if __name__ == '__main__':
    update_css()
