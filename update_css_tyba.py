css_content = """
/* ==========================================================================
   APRENDE TYBA - STUDY PROJECTS DASHBOARD
   ========================================================================== */

.tyba-project-dashboard {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 1rem;
  height: 100%;
}

.tyba-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(0, 240, 255, 0.2);
  padding-bottom: 1rem;
}

.tyba-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.tyba-icon {
  font-size: 2.5rem;
  filter: drop-shadow(0 0 10px var(--accent-blue));
}

.tyba-title {
  color: var(--text-bright);
  font-family: 'Outfit', sans-serif;
  font-size: 1.5rem;
  margin: 0 0 0.2rem 0;
  letter-spacing: 2px;
}

.tyba-subtitle {
  color: var(--text-dim);
  font-size: 0.9rem;
  margin: 0;
}

.tyba-projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
  overflow-y: auto;
  padding-right: 10px;
}

.tyba-project-card {
  background: rgba(10, 25, 47, 0.6);
  border: 1px solid rgba(0, 240, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.tyba-project-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent-blue), transparent);
  transform: translateX(-100%);
  transition: transform 0.5s ease;
}

.tyba-project-card:hover {
  transform: translateY(-5px);
  border-color: rgba(0, 240, 255, 0.5);
  box-shadow: 0 10px 30px -15px rgba(0, 240, 255, 0.3);
}

.tyba-project-card:hover::before {
  transform: translateX(100%);
}

.tyba-project-card.disabled {
  opacity: 0.5;
  filter: grayscale(1);
  pointer-events: none;
}

.tyba-project-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.tyba-project-info h3 {
  color: var(--text-bright);
  font-size: 1.2rem;
  margin: 0 0 0.5rem 0;
}

.tyba-project-info p {
  color: var(--text-dim);
  font-size: 0.9rem;
  line-height: 1.4;
  margin: 0;
}

.tyba-project-actions {
  display: flex;
  gap: 1rem;
  margin-top: auto;
}

.tyba-btn {
  flex: 1;
  padding: 0.8rem;
  border: none;
  border-radius: 6px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.tyba-btn-slides {
  background: rgba(0, 240, 255, 0.1);
  color: var(--accent-blue);
  border: 1px solid rgba(0, 240, 255, 0.3);
}

.tyba-btn-slides:hover {
  background: rgba(0, 240, 255, 0.2);
  box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
}

.tyba-btn-video {
  background: rgba(255, 0, 102, 0.1);
  color: #ff0066;
  border: 1px solid rgba(255, 0, 102, 0.3);
}

.tyba-btn-video:hover {
  background: rgba(255, 0, 102, 0.2);
  box-shadow: 0 0 15px rgba(255, 0, 102, 0.3);
}

/* ==========================================================================
   VIEWER OVERLAY (PDF / VIDEO)
   ========================================================================== */

.tyba-viewer-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(2, 10, 24, 0.95);
  backdrop-filter: blur(10px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  opacity: 1;
  transition: opacity 0.3s ease;
}

.tyba-viewer-overlay.hidden {
  opacity: 0;
  pointer-events: none;
}

.tyba-viewer-container {
  width: 100%;
  max-width: 1200px;
  height: 90%;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

.tyba-viewer-header {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(10, 25, 47, 0.8);
}

#tyba-viewer-title {
  color: var(--text-bright);
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  letter-spacing: 1px;
}

.tyba-btn-close {
  background: transparent;
  border: none;
  color: var(--text-dim);
  font-size: 1.2rem;
  cursor: pointer;
  transition: color 0.3s;
}

.tyba-btn-close:hover {
  color: #ff3366;
}

.tyba-viewer-content {
  flex: 1;
  position: relative;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* CSS HACK TO HIDE NOTEBOOK LM WATERMARK */
/* The watermark is usually at the bottom or corners. 
   We wrap the video in a hidden overflow container and scale it slightly. */
.video-cropper-wrapper {
  width: 100%;
  height: 100%;
  overflow: hidden; /* This hides what overflows */
  display: flex;
  align-items: center;
  justify-content: center;
  background: #000;
}

.video-cropper-wrapper video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* Scale up by 10% to push the edges (and the watermark) outside the visible area */
  transform: scale(1.1); 
  /* Shift slightly up if the watermark is at the bottom */
  transform-origin: center top; 
}

.tyba-pdf-frame {
  width: 100%;
  height: 100%;
  border: none;
  background: #fff; /* PDFs usually need white bg */
}
"""

with open('src/style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

print("style.css updated successfully!")
