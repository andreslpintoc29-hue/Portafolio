import re

def update_main_js():
    with open('src/main.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new search and neural map logic
    new_logic = """
function initTybaSearch() {
  const searchInput = document.getElementById('tyba-search-input');
  if (!searchInput) return;

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const cards = document.querySelectorAll('.tyba-card');

    cards.forEach(card => {
      const title = card.querySelector('.tyba-card-title').innerText.toLowerCase();
      const desc = card.querySelector('.tyba-card-desc').innerText.toLowerCase();
      const cat = card.querySelector('.tyba-card-cat').innerText.toLowerCase();
      
      if (title.includes(query) || desc.includes(query) || cat.includes(query)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  });
}

function initTybaNeuralMap() {
  const cards = document.querySelectorAll('.tyba-card');
  const modal = document.getElementById('tyba-course-modal');
  const closeBtn = document.getElementById('tyba-modal-close');
  
  const modalTitle = document.getElementById('tyba-modal-title');
  const modalSubtitle = document.getElementById('tyba-modal-subtitle');
  const modalBody = document.getElementById('tyba-modal-body');

  if (!modal) return;

  closeBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
  });

  // Close on background click
  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.add('hidden');
  });

  cards.forEach(card => {
    card.addEventListener('click', () => {
      const caseId = card.getAttribute('data-case');
      if (!caseId || !tybaData[caseId]) return;

      const data = tybaData[caseId];
      const cat = card.querySelector('.tyba-card-cat').innerText;

      modalSubtitle.innerText = cat;
      modalTitle.innerText = data.title;
      
      let stepsHtml = '';
      if (data.desc) {
         stepsHtml += `<p style="color: var(--text-dim); margin-bottom: 25px; font-size: 1.1rem; line-height: 1.6;">${data.desc}</p>`;
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
      }

      modalBody.innerHTML = stepsHtml;
      modal.classList.remove('hidden');
      modalBody.scrollTop = 0;
    });
  });
}
"""

    # We need to find the old initTybaNeuralMap and initTybaSearch functions and replace them.
    # Since they were just added, let's look for them.
    
    # First, let's find the range to replace. 
    # We look for "function initTybaSearch()" and go until the end of "initTybaNeuralMap()".
    
    start_pattern = "function initTybaSearch()"
    # Find where it ends. It's likely followed by initTybaNeuralMap.
    # Let's just replace the whole block if found.
    
    if start_pattern in content:
        # Simple string replacement for the newly added functions
        content = re.sub(r"function initTybaSearch\(\) \{[\s\S]*?\}\s*\}", new_logic, content)
        # Wait, the above regex might be too greedy or not match correctly. 
        # Let's try a safer approach: find the start and end of the block.
        
        # Let's find the index of the start
        idx_start = content.find(start_pattern)
        # Find the last closing brace of initTybaNeuralMap
        # We know initTybaNeuralMap follows it.
        idx_end_func = content.find("initTybaNeuralMap() {", idx_start)
        if idx_end_func != -1:
            # Find the closing brace of that function
            brace_count = 0
            found_first = False
            for i in range(idx_end_func, len(content)):
                if content[i] == '{':
                    brace_count += 1
                    found_first = True
                elif content[i] == '}':
                    brace_count -= 1
                if found_first and brace_count == 0:
                    idx_final = i + 1
                    content = content[:idx_start] + new_logic + content[idx_final:]
                    break

    with open('src/main.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated main.js successfully.")

if __name__ == '__main__':
    update_main_js()
