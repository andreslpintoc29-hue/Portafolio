js_content = """
// ==========================================================================
// APRENDE TYBA - STUDY PROJECTS LOGIC
// ==========================================================================

window.openTybaProject = function(type, url) {
  const overlay = document.getElementById('tyba-viewer-overlay');
  const contentContainer = document.getElementById('tyba-viewer-content');
  const title = document.getElementById('tyba-viewer-title');
  
  if (!overlay || !contentContainer) return;
  
  // Clear previous content
  contentContainer.innerHTML = '';
  
  if (type === 'slides') {
    title.textContent = 'VISOR DE DIAPOSITIVAS (PDF)';
    contentContainer.innerHTML = `<iframe src="${url}" class="tyba-pdf-frame"></iframe>`;
  } else if (type === 'video') {
    title.textContent = 'REPRODUCTOR DE VIDEO (SIN MARCA DE AGUA)';
    contentContainer.innerHTML = `
      <div class="video-cropper-wrapper">
        <video src="${url}" controls autoplay controlsList="nodownload"></video>
      </div>
    `;
  }
  
  // Show overlay
  overlay.classList.remove('hidden');
};

// Handle close button
const closeTybaViewerBtn = document.getElementById('tyba-viewer-close');
if (closeTybaViewerBtn) {
  closeTybaViewerBtn.addEventListener('click', () => {
    const overlay = document.getElementById('tyba-viewer-overlay');
    const contentContainer = document.getElementById('tyba-viewer-content');
    
    // Hide overlay
    overlay.classList.add('hidden');
    
    // Stop video/audio by clearing content
    setTimeout(() => {
      if (contentContainer) contentContainer.innerHTML = '';
    }, 300);
  });
}
"""

with open('src/main.js', 'a', encoding='utf-8') as f:
    f.write(js_content)

print("main.js updated successfully!")
