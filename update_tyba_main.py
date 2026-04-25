import re

def update_main_js():
    with open('src/main.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add import at the top
    if "import tybaData from './tybaData.json'" not in content:
        content = content.replace("import { gsap } from 'gsap'", "import { gsap } from 'gsap'\nimport tybaData from './tybaData.json'")

    # 2. Update DOMContentLoaded
    content = content.replace("initTybaModuleNavigation();", "initTybaNeuralMap();\n  initTybaSearch();")

    # 3. Replace initTybaModuleNavigation function
    old_func = """function initTybaModuleNavigation() {
  const menuItems = document.querySelectorAll('.tyba-menu-item');
  const sections = document.querySelectorAll('.tyba-section');

  menuItems.forEach(item => {
    item.addEventListener('click', () => {
      // Remove active from all items
      menuItems.forEach(i => i.classList.remove('active'));
      // Add active to clicked item
      item.classList.add('active');

      // Hide all sections
      sections.forEach(sec => {
        sec.classList.remove('active');
        sec.classList.add('hidden');
      });

      // Show target section
      const targetId = item.getAttribute('data-target');
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        targetSection.classList.remove('hidden');
        targetSection.classList.add('active');
      }
    });
  });
}"""

    new_funcs = """function initTybaSearch() {
  const searchInput = document.getElementById('tyba-search-input');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const nodes = document.querySelectorAll('.tyba-node');

    nodes.forEach(node => {
      const label = node.querySelector('.brain-label').innerText.toLowerCase();
      const cat = node.querySelector('h3').innerText.toLowerCase();
      
      if (label.includes(query) || cat.includes(query)) {
        node.style.display = 'flex';
      } else {
        node.style.display = 'none';
      }
    });
  });
}

function initTybaNeuralMap() {
  const nodes = document.querySelectorAll('.tyba-node');
  const modal = document.getElementById('tyba-course-modal');
  const closeBtn = document.getElementById('tyba-modal-close');
  
  const modalTitle = document.getElementById('tyba-modal-title');
  const modalSubtitle = document.getElementById('tyba-modal-subtitle');
  const modalBody = document.getElementById('tyba-modal-body');

  if (!modal) return;

  closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
  });

  nodes.forEach(node => {
    node.addEventListener('click', () => {
      const caseId = node.getAttribute('data-case');
      if (!caseId || !tybaData[caseId]) return;

      const data = tybaData[caseId];
      const cat = node.querySelector('h3').innerText;

      modalSubtitle.innerText = cat;
      modalTitle.innerText = data.title;
      
      // Generate steps HTML
      let stepsHtml = '';
      if (data.desc) {
         stepsHtml += `<p style="color: var(--text-dim); margin-bottom: 20px; font-size: 1.05rem; line-height: 1.5;">${data.desc}</p>`;
      }

      if (data.steps && data.steps.length > 0) {
        data.steps.forEach((step, index) => {
          stepsHtml += `
            <div class="tyba-course-step">
              <span class="tyba-course-step-num">PASO ${index + 1}</span>
              <h3 class="tyba-course-step-title">${step.title}</h3>
              <p class="tyba-course-step-text">${step.text}</p>
              <div class="tyba-course-step-tip">
                <p>${step.tip}</p>
              </div>
            </div>
          `;
        });
      } else {
        stepsHtml += `<p style="color: var(--accent-cyan);">Datos del paso a paso no encontrados para este módulo.</p>`;
      }

      modalBody.innerHTML = stepsHtml;
      modal.classList.remove('hidden');
    });
  });
}"""

    if old_func in content:
        content = content.replace(old_func, new_funcs)
        with open('src/main.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated main.js successfully")
    else:
        print("Could not find old_func in main.js. Let's try replacing just the name and appending.")
        # Fallback if whitespace is different
        content = content.replace("function initTybaModuleNavigation() {", "function oldInitTyba() {")
        content += "\n\n" + new_funcs
        with open('src/main.js', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated main.js with fallback successfully")

if __name__ == '__main__':
    update_main_js()
