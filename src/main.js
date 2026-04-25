import './style.css'
import { gsap } from 'gsap'
import tybaData from './tybaData.json'

document.addEventListener('DOMContentLoaded', () => {
  initNeuralParticles();
  initBrainNodeInteractions();
  initNavigation();
  initPdfViewer();
  initGemaModal();
  animateSystemBootstrap();
  initITDashboard();
  initHoloBrain();
  initTybaNeuralMap();
  initTybaSearch();
});

function initTybaSearch() {
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
}

function initHoloBrain() {
  const canvas = document.getElementById('holo-particles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let particles = [];
  let brainPhase = 0;

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class HoloParticle {
    constructor() {
      this.angle = Math.random() * Math.PI * 2;
      this.radius = 60 + Math.random() * 100;
      this.speed = 0.008 + Math.random() * 0.015;
      this.size = 3 + Math.random() * 5;
      this.pulse = Math.random() * Math.PI * 2;
    }
    update() {
      this.angle += this.speed;
      this.pulse += 0.08;
      const wobble = Math.sin(this.pulse) * 20;
      this.x = canvas.width / 2 + Math.cos(this.angle) * (this.radius + wobble);
      this.y = canvas.height / 2 + Math.sin(this.angle + brainPhase) * (this.radius + wobble);
    }
    draw() {
      ctx.fillStyle = '#00f5ff';
      ctx.shadowBlur = 20;
      ctx.shadowColor = '#00f5ff';
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  for (let i = 0; i < 50; i++) particles.push(new HoloParticle());

  function drawBrainCore() {
    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const gradient = ctx.createRadialGradient(cx, cy, 0, cx, cy, 150);
    gradient.addColorStop(0, 'rgba(0, 245, 255, 0.3)');
    gradient.addColorStop(0.5, 'rgba(0, 119, 255, 0.15)');
    gradient.addColorStop(1, 'rgba(0, 255, 136, 0)');
    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(cx, cy, 150 + Math.sin(brainPhase) * 20, 0, Math.PI * 2);
    ctx.fill();
  }

  function animate() {
    requestAnimationFrame(animate);
    const overlay = document.getElementById('it-confirm-overlay');
    if (overlay && overlay.classList.contains('hidden')) return;

    ctx.fillStyle = 'rgba(0, 0, 0, 0.15)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    brainPhase += 0.03;

    drawBrainCore();
    ctx.globalCompositeOperation = 'lighter';
    particles.forEach(p => { p.update(); p.draw(); });
    ctx.globalCompositeOperation = 'source-over';

    ctx.strokeStyle = 'rgba(0, 245, 255, 0.2)';
    ctx.lineWidth = 1;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 60) {
          ctx.globalAlpha = (1 - dist / 60) * 0.5;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    ctx.globalAlpha = 1;
  }
  animate();
}

// --- 1. Neural Particles (Cyan Core) ---
// (omitted for brevity in replacement chunk targeting start of file)

function initNeuralParticles() {
  const canvas = document.getElementById('neural-particles');
  const ctx = canvas.getContext('2d');
  let particles = [];
  
  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.vx = (Math.random() - 0.5) * 0.4;
      this.vy = (Math.random() - 0.5) * 0.4;
      this.size = 2 + Math.random() * 2;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
      if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
    }
    draw() {
      ctx.fillStyle = 'rgba(0, 245, 255, 0.6)';
      ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2); ctx.fill();
    }
  }

  for (let i = 0; i < 40; i++) particles.push(new Particle());

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    ctx.strokeStyle = 'rgba(0, 245, 255, 0.1)';
    ctx.lineWidth = 1.5;
    for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
            const dx = particles[i].x - particles[j].x;
            const dy = particles[i].y - particles[j].y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            if (dist < 200) { ctx.beginPath(); ctx.moveTo(particles[i].x, particles[i].y); ctx.lineTo(particles[j].x, particles[j].y); ctx.stroke(); }
        }
    }
    requestAnimationFrame(animate);
  }
  animate();
}

// --- 2. Navigation Logic ---
function initNavigation() {
  const navFiscalia = document.getElementById('nav-fiscalia');
  const navJudicial = document.getElementById('nav-judicial');
  const navProfile = document.getElementById('nav-profile');
  const navIt = document.getElementById('nav-it');
  const navTyba = document.getElementById('nav-tyba');
  
  const viewFiscalia = document.getElementById('view-fiscalia');
  const viewJudicial = document.getElementById('view-judicial');
  const viewProfile = document.getElementById('view-profile');
  const viewIt = document.getElementById('view-it');
  const viewTyba = document.getElementById('view-tyba');

  // Helper to switch views with an animation
  function switchView(activeNav, activeView) {
    if (!activeNav || !activeView) return;
    
    // Reset all navs
    [navFiscalia, navJudicial, navProfile, navIt, navTyba].forEach(nav => {
      if(nav) nav.classList.remove('active')
    });
    // Set active
    activeNav.classList.add('active');

    // Hide all views instantly
    [viewFiscalia, viewJudicial, viewProfile, viewIt, viewTyba].forEach(view => {
      if (view && !view.classList.contains('hidden')) {
        view.classList.add('hidden');
        view.classList.remove('active');
      }
    });

    // Show new view instantly
    activeView.classList.remove('hidden');
    activeView.classList.add('active');
  }

  if(navFiscalia) navFiscalia.addEventListener('click', (e) => { e.preventDefault(); switchView(navFiscalia, viewFiscalia); });
  if(navJudicial) navJudicial.addEventListener('click', (e) => { e.preventDefault(); switchView(navJudicial, viewJudicial); });
  if(navProfile) navProfile.addEventListener('click', (e) => { e.preventDefault(); switchView(navProfile, viewProfile); });
  if(navIt) navIt.addEventListener('click', (e) => { e.preventDefault(); switchView(navIt, viewIt); });
  if(navTyba) navTyba.addEventListener('click', (e) => { e.preventDefault(); switchView(navTyba, viewTyba); });
}

// --- 3. PDF Viewer Logic ---
function initPdfViewer() {
  const docNodes = document.querySelectorAll('.ai-brain-node.small');
  const modal = document.getElementById('pdf-modal');
  const iframe = document.getElementById('pdf-frame');
  const closeBtn = document.getElementById('close-modal');
  const modalTitle = document.getElementById('modal-title');

  docNodes.forEach(node => {
    node.addEventListener('click', () => {
      const pdfPath = node.getAttribute('data-pdf');
      const label = node.querySelector('.brain-label').innerText;
      
      if (!pdfPath) return;

      modalTitle.innerText = `ANALIZANDO: ${label}`;
      iframe.src = `${import.meta.env.BASE_URL}${pdfPath}`;
      
      modal.classList.remove('hidden');
      gsap.fromTo('.pdf-modal-content', 
        { scale: 0.8, opacity: 0 }, 
        { scale: 1, opacity: 1, duration: 0.6, ease: 'power4.out' }
      );
    });
  });

  closeBtn.addEventListener('click', () => {
    gsap.to('.pdf-modal-content', { 
      scale: 0.8, opacity: 0, duration: 0.4, 
      onComplete: () => {
        modal.classList.add('hidden');
        iframe.src = ""; // Clear iframe to stop loading
      }
    });
  });

  // Close on backdrop click
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeBtn.click();
  });
}

// --- 4. Magnetic Effects ---
function initBrainNodeInteractions() {
  const nodes = document.querySelectorAll('.ai-brain-node');

  window.addEventListener('mousemove', (e) => {
    nodes.forEach(node => {
      const rect = node.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 300) {
        const factor = (1 - dist / 300);
        gsap.to(node, {
          x: (dx / dist) * factor * 25,
          y: (dy / dist) * factor * 25,
          scale: 1 + factor * 0.1,
          duration: 0.6,
          ease: 'power2.out'
        });
      } else {
        gsap.to(node, { x: 0, y: 0, scale: 1, duration: 1, ease: 'elastic.out(1, 0.5)' });
      }
    });
  });
}

// --- 5. System Bootstrap ---
function animateSystemBootstrap() {
  const tl = gsap.timeline();
  tl.from('.ai-core-env', { opacity: 0, duration: 0.3 })
    .from('.top-nav-bar', { y: -50, opacity: 0, duration: 0.3 }, '-=0.1');
}

// --- 6. GEMA Prompter Modal Logic ---
function initGemaModal() {
  const gemaNodes = document.querySelectorAll('.gema-action');
  const modal = document.getElementById('gema-modal');
  const closeBtn = document.getElementById('close-gema-modal');
  const openGemBtn = document.getElementById('btn-open-gem');
  
  const modalTitle = document.getElementById('gema-modal-title');
  const modalDesc = document.getElementById('gema-modal-desc');
  const modalSteps = document.getElementById('gema-modal-steps');

  const gemData = {
    cti: {
      title: "GENERADOR DE PROMPT: CTI",
      desc: "Al abrir este módulo, serás redirigido a un entorno seguro interactivo impulsado por IA y parametrizado por Andrés Pinto para informes FPJ.",
      steps: `<h4>¿Qué debes hacer en la Gema?</h4><p>1. Pega en la caja de chat el borrador de tu investigación, un testimonio en bruto o pruebas.</p><p>2. La IA estructurará la narrativa cronológica y te indicará los códigos FPJ adecuados.</p>`,
      url: "https://gemini.google.com/gem/1R99A3aCz-cy-tk2Ok77pWf7By3C0fYo1?usp=sharing",
      btnText: "INICIAR ASISTENTE CTI EN GEMINI"
    },
    law: {
      title: "ANALISTA DE JURISPRUDENCIA",
      desc: "Al abrir este módulo, accederás a un Magistrado Auxiliar de IA entrenado por Andrés Pinto para extraer la Ratio Decidendi de cualquier sentencia.",
      steps: `<h4>¿Qué debes hacer en la Gema?</h4><p>1. Pega bloques textualmente largos de una sentencia o fallo (Corte Constitucional, Suprema, etc).</p><p>2. La IA extraerá inmediatamente los Hechos Relevantes, el Problema Jurídico y la Decisión en viñetas para tu revisión rápida.</p>`,
      url: "https://gemini.google.com/gem/1WTL0E2F_hLyBe8tW_Eu4C8HAGNUL-v1O?usp=sharing",
      btnText: "INICIAR ASISTENTE JUDICIAL"
    },
    liquidador: {
      title: "LIQUIDADOR Y CONSULTOR PENAL",
      desc: "Al abrir este módulo, accederás a un Asistente Jurídico Experto de IA entrenado por Andrés Pinto especializado en la Ley 906 de 2004.",
      steps: `<h4>¿Qué debes hacer en la Gema?</h4><p>1. Escribe tu duda puntual procesal, cálculo matemático de penas o solicitud de requisitos legales.</p><p>2. La Inteligencia Artificial te arrojará la respuesta siempre fundamentada con el número del artículo en la norma colombiana.</p>`,
      url: "https://gemini.google.com/gem/1MjRqQOI2VjTSCWXJySqDuVN0eT1WYqhl?usp=sharing",
      btnText: "INICIAR ASISTENTE NORMATIVO"
    },
    cti_transcripciones: {
      title: "ANALISTA TRANSCRIPCIONES TEAMS",
      desc: "[EN CONSTRUCCIÓN] Este módulo extraerá contradicciones y líneas de tiempo cruzando testimonios de audios y transcripciones interactivamente.",
      steps: `<h4>Próximamente</h4><p>Para activar este nodo, crea la respectiva Gema en Google con el rol de Analista de Audios Forenses y vincula el enlace.</p>`,
      url: "",
      btnText: "MÓDULO CERRADO"
    },
    cti_custodia: {
      title: "AUDITOR CADENA DE CUSTODIA",
      desc: "[EN CONSTRUCCIÓN] Implementación de NotebookLM (RAG). Cruzará informes periciales directamente con el Manual Institucional.",
      steps: `<h4>Próximamente</h4><p>Crea tu libreta en Google NotebookLM, carga el Manual de Custodia en formato PDF, y pega aquí el enlace compartido.</p>`,
      url: "",
      btnText: "MÓDULO CERRADO"
    },
    cti_ordenes: {
      title: "PROYECTOR DE ÓRDENES CTI",
      desc: "[EN CONSTRUCCIÓN] Creación de órdenes legales automáticas a Policía Judicial a partir de solicitudes verbales del Fiscal.",
      steps: `<h4>Próximamente</h4><p>Falta parametrizar esta Gema en Google Gemini con plantillas de allanamiento y búsqueda selectiva.</p>`,
      url: "",
      btnText: "MÓDULO CERRADO"
    },
    law_citaciones: {
      title: "GENERADOR DE CITACIONES",
      desc: "[EN CONSTRUCCIÓN] Agente IA diseñado para Secretarios de Juzgados. Automatiza citaciones, emplazamientos y autos de trámite.",
      steps: `<h4>Próximamente</h4><p>Falta parametrizar este prompt maestro para evitar que la IA confunda el Código General del Proceso con Ley 906.</p>`,
      url: "",
      btnText: "MÓDULO CERRADO"
    },
    law_audiencias: {
      title: "RESUMIDOR ACTAS DE AUDIENCIA",
      desc: "[EN CONSTRUCCIÓN] Analizará actas crudas para organizar argumentos de la Fiscalía vs Defensa y plantear el problema jurídico al Juez.",
      steps: `<h4>Próximamente</h4><p>Módulo pendiente de integración API profunda o redirección a NotebookLM exclusivo de despachos.</p>`,
      url: "",
      btnText: "MÓDULO CERRADO"
    },
    it_support: {
      title: "SCRIPT MANTENIMIENTO INTEGRAL",
      desc: "Herramienta de diagnóstico y reparación profunda (Limpieza de Temporales, Cache DNS, Reinicio Cola de Impresión y WIA - Escaner).",
      steps: `<h4>Instrucciones para Desbloquear Tu PC</h4><p>1. Da clic en "Descargar Script" abajo.</p><p>2. En tu PC, hazle doble clic a <code>Soporte_IT_Andres_Pinto.bat</code> para que barra y solucione el entorno sin afectar tus documentos.</p>`,
      url: import.meta.env.BASE_URL + "Soporte_IT_Andres_Pinto.bat",
      btnText: "⬇️ DESCARGAR SCRIPT (.bat)"
    }
  };

  // Open Modal Handler
  gemaNodes.forEach(node => {
    node.addEventListener('click', () => {
      const gemaType = node.getAttribute('data-gema-type');
      if (gemData[gemaType]) {
        const data = gemData[gemaType];
        
        // Update Modal Content Dynamically
        modalTitle.innerHTML = data.title;
        modalDesc.innerHTML = data.desc;
        modalSteps.innerHTML = data.steps;
        openGemBtn.innerHTML = data.btnText;
        
        if(data.url) {
          openGemBtn.setAttribute('data-url', data.url);
          openGemBtn.style.opacity = "1";
          openGemBtn.style.pointerEvents = "all";
          openGemBtn.style.backgroundColor = ""; // Reset inline neon pulse
        } else {
          openGemBtn.setAttribute('data-url', "");
          openGemBtn.style.opacity = "0.5";
          openGemBtn.style.pointerEvents = "none";
          openGemBtn.style.backgroundColor = "transparent";
          openGemBtn.style.boxShadow = "none";
        }

        modal.classList.remove('hidden');
        gsap.fromTo('.form-modal', 
          { scale: 0.8, opacity: 0 }, 
          { scale: 1, opacity: 1, duration: 0.6, ease: 'power4.out' }
        );
      }
    });
  });

  // Close Modal Logic
  const closeModal = () => {
    gsap.to('.form-modal', { 
      scale: 0.8, opacity: 0, duration: 0.4, 
      onComplete: () => {
        modal.classList.add('hidden');
      }
    });
  };

  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  // Open Gem Link
  if (openGemBtn) {
    openGemBtn.addEventListener('click', () => {
      const gemUrl = openGemBtn.getAttribute('data-url');
      if (gemUrl) {
        gsap.to(openGemBtn, { scale: 1.05, backgroundColor: '#00ff88', duration: 0.2, yoyo: true, repeat: 1 });
        setTimeout(() => {
          if (gemUrl.endsWith('.bat')) {
            // Force Download for script files
            const a = document.createElement('a');
            a.href = gemUrl;
            a.download = gemUrl.split('/').pop() || 'script.bat';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
          } else {
            // Open Gemini Links in a new tab
            window.open(gemUrl, '_blank');
          }
          closeModal();
        }, 400); // Slight delay for the animation
      }
    });
  }
}

// --- IT Dashboard Interactive Logic ---
function initITDashboard() {
  window.runITAction = function(action) {
    const actions = {
      clean: {
        label: 'Limpieza Profunda', prog: 'prog-clean', btn: 'btn-clean',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Verificando privilegios de administrador...' },
          { delay: 700,  cls: 'info',    msg: '  [1/4] Vaciando %TEMP% del perfil de usuario...' },
          { delay: 1400, cls: 'info',    msg: '  [2/4] Limpiando C:\\Windows\\Temp...' },
          { delay: 2000, cls: 'info',    msg: '  [3/4] Borrando archivos Prefetch obsoletos...' },
          { delay: 2600, cls: 'warning', msg: '  [4/4] Vaciando Papelera de reciclaje...' },
          { delay: 3200, cls: 'success', msg: '  [OK] Limpieza completada. Cache purgada. PC mas rapido.' }
        ]
      },
      printer: {
        label: 'Reparar Impresora', prog: 'prog-printer', btn: 'btn-printer',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> net stop spooler...' },
          { delay: 900,  cls: 'warning', msg: '  El servicio Spooler se esta deteniendo...' },
          { delay: 1600, cls: 'info',    msg: '  Borrando cola atascada...' },
          { delay: 2400, cls: 'cmd',     msg: '> net start spooler...' },
          { delay: 3600, cls: 'success', msg: '  [OK] Impresora desbloqueada. Documentos fantasma destruidos.' }
        ]
      },
      scanner: {
        label: 'Reparar Escaner', prog: 'prog-scanner', btn: 'btn-scanner',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Diagnostico protocolo WIA...' },
          { delay: 800,  cls: 'warning', msg: '  Servicio WIA bloqueado: STOP_PENDING' },
          { delay: 1600, cls: 'cmd',     msg: '> net stop stisvc...' },
          { delay: 2400, cls: 'cmd',     msg: '> net start stisvc...' },
          { delay: 3200, cls: 'success', msg: '  [OK] Escaner reestablecido. Protocolo TWAIN/WIA activo.' }
        ]
      },
      network: {
        label: 'Arreglar Red / Internet', prog: 'prog-network', btn: 'btn-network',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> ipconfig /release...' },
          { delay: 1000, cls: 'info',    msg: '  Direccion IP 192.168.1.X liberada.' },
          { delay: 1700, cls: 'cmd',     msg: '> ipconfig /renew...' },
          { delay: 2500, cls: 'info',    msg: '  Nueva IP asignada correctamente.' },
          { delay: 3000, cls: 'cmd',     msg: '> ipconfig /flushdns...' },
          { delay: 3700, cls: 'cmd',     msg: '> netsh winsock reset...' },
          { delay: 4300, cls: 'success', msg: '  [OK] Red reparada. Reinicie el equipo para aplicar Winsock.' }
        ]
      },
      update: {
        label: 'Reparar Windows Update', prog: 'prog-update', btn: 'btn-update',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> net stop wuauserv...' },
          { delay: 900,  cls: 'cmd',     msg: '> net stop bits...' },
          { delay: 1500, cls: 'warning', msg: '  Borrando SoftwareDistribution\\Download corrupta...' },
          { delay: 2500, cls: 'info',    msg: '  Archivos de actualizacion corruptos eliminados.' },
          { delay: 3800, cls: 'success', msg: '  [OK] Windows Update reparado. Actualice nuevamente.' }
        ]
      },
      explorer: {
        label: 'Resucitar Pantalla', prog: 'prog-explorer', btn: 'btn-explorer',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> taskkill /f /im explorer.exe...' },
          { delay: 900,  cls: 'warning', msg: '  ADVERTENCIA: Pantalla desaparecera momentaneamente.' },
          { delay: 1600, cls: 'info',    msg: '  Proceso explorer.exe terminado (PID: 4821)' },
          { delay: 2200, cls: 'cmd',     msg: '> start explorer.exe...' },
          { delay: 3000, cls: 'success', msg: '  [OK] Shell de Windows reiniciado correctamente.' }
        ]
      },
      god: {
        label: 'MODO DIOS', prog: null, btn: null,
        steps: [
          { delay: 100,  cls: 'warning', msg: '> PROTOCOLO DIOS INICIADO: Barrido total institucional...' },
          { delay: 600,  cls: 'cmd',     msg: '  [1/12] Limpieza de temporales y papelera...' },
          { delay: 1000, cls: 'cmd',     msg: '  [2/12] Desbloqueando Cola de Impresion Spooler...' },
          { delay: 1400, cls: 'cmd',     msg: '  [3/12] Reiniciando servicios WIA (Escaner)...' },
          { delay: 1800, cls: 'cmd',     msg: '  [4/12] Purgando DNS y renovando IP...' },
          { delay: 2200, cls: 'cmd',     msg: '  [5/12] Reparando Windows Update...' },
          { delay: 2600, cls: 'cmd',     msg: '  [6/12] Reiniciando Explorer.exe...' },
          { delay: 3000, cls: 'cmd',     msg: '  [7/12] Diagnostico disco duro CHKDSK...' },
          { delay: 3400, cls: 'cmd',     msg: '  [8/12] Liberando memoria RAM...' },
          { delay: 3800, cls: 'cmd',     msg: '  [9/12] Restaurando Firewall...' },
          { delay: 4200, cls: 'cmd',     msg: '  [10/12] Escaneo WiFi completado...' },
          { delay: 4600, cls: 'cmd',     msg: '  [11/12] Reiniciando controladores USB...' },
          { delay: 5000, cls: 'cmd',     msg: '  [12/12] Reiniciando servicios de audio...' },
          { delay: 5600, cls: 'success', msg: '  [MODO DIOS COMPLETADO] 12 modulos ejecutados. PC 100% restaurado.' }
        ]
      },
      disco: {
        label: 'Diagnostico Disco Duro', prog: 'prog-disco', btn: 'btn-disco',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Iniciando CHKDSK en unidad C:...' },
          { delay: 1000, cls: 'info',    msg: '  Fase 1: Verificando archivos del sistema...' },
          { delay: 2000, cls: 'info',    msg: '  Fase 2: Verificando indices del sistema...' },
          { delay: 3000, cls: 'info',    msg: '  Fase 3: Verificando descriptores de seguridad...' },
          { delay: 4000, cls: 'success', msg: '  [OK] Disco analizado. No se encontraron sectores danados.' }
        ]
      },
      ram: {
        label: 'Liberar Memoria RAM', prog: 'prog-ram', btn: 'btn-ram',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Detectando procesos pesados en segundo plano...' },
          { delay: 800,  cls: 'warning', msg: '  Cerrando: Teams.exe (485 MB)' },
          { delay: 1300, cls: 'warning', msg: '  Cerrando: OneDrive.exe (210 MB)' },
          { delay: 1800, cls: 'warning', msg: '  Cerrando: Widgets.exe (180 MB)' },
          { delay: 2300, cls: 'info',    msg: '  Vaciando cache de memoria del sistema...' },
          { delay: 2800, cls: 'success', msg: '  [OK] 875 MB de RAM liberados. PC mas fluido.' }
        ]
      },
      firewall: {
        label: 'Reparar Firewall', prog: 'prog-firewall', btn: 'btn-firewall',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> netsh advfirewall reset...' },
          { delay: 1000, cls: 'warning', msg: '  Reglas de firewall reseteadas a valores de fabrica.' },
          { delay: 1800, cls: 'cmd',     msg: '> Reactivando Firewall en todos los perfiles...' },
          { delay: 2600, cls: 'success', msg: '  [OK] Firewall restaurado y activo en Dominio/Privado/Publico.' }
        ]
      },
wifi: {
        label: 'Diagnostico WiFi', prog: 'prog-wifi', btn: 'btn-wifi',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> netsh wlan show interfaces...' },
          { delay: 800,  cls: 'info',    msg: '  Adaptador: Intel WiFi 6 AX201' },
          { delay: 1200, cls: 'info',    msg: '  SSID: RED_JUDICIAL_5G | Senal: 78%' },
          { delay: 1800, cls: 'cmd',     msg: '> Escaneando redes disponibles (BSSID)...' },
          { delay: 2500, cls: 'info',    msg: '  12 redes detectadas. Canal 6 congestionado.' },
          { delay: 3200, cls: 'cmd',     msg: '> Generando reporte HTML en C:\\WiFi_Report.html...' },
          { delay: 3800, cls: 'success', msg: '  [OK] Diagnostico WiFi completo. Reporte exportado.' }
        ]
      },
      wifi_boost: {
        label: 'Potenciar WiFi', prog: 'prog-wifi_boost', btn: 'btn-wifi_boost',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Eliminando limite QoS...' },
          { delay: 900,  cls: 'info',    msg: '  Limitador QoS deshabilitado.' },
          { delay: 1600, cls: 'cmd',     msg: '> Configurando DNS rapido (Google + Cloudflare)...' },
          { delay: 2200, cls: 'info',    msg: '  DNS: 8.8.8.8 + 1.1.1.1' },
          { delay: 2800, cls: 'cmd',     msg: '> Ajustando TCP AutoTuning...' },
          { delay: 3400, cls: 'info',    msg: '  TCP AutoTuning activo.' },
          { delay: 4000, cls: 'cmd',     msg: '> Limpiando cache DNS...' },
          { delay: 4600, cls: 'success', msg: '  [OK] WiFi potenciado! Velocidad maxima habilitada.' }
        ]
      },
      usb: {
        label: 'Reparar USB / Dispositivos', prog: 'prog-usb', btn: 'btn-usb',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> Enumerando controladores USB del sistema...' },
          { delay: 900,  cls: 'warning', msg: '  1 dispositivo USB detectado con estado: ERROR' },
          { delay: 1600, cls: 'cmd',     msg: '> Enable-PnpDevice: Reactivando controlador...' },
          { delay: 2300, cls: 'cmd',     msg: '> pnputil /scan-devices...' },
          { delay: 3000, cls: 'success', msg: '  [OK] Puertos USB reiniciados. Reconecte su dispositivo.' }
        ]
      },
      audio: {
        label: 'Reparar Audio / Sonido', prog: 'prog-audio', btn: 'btn-audio',
        steps: [
          { delay: 200,  cls: 'cmd',     msg: '> net stop Audiosrv...' },
          { delay: 800,  cls: 'warning', msg: '  Servicio Windows Audio detenido.' },
          { delay: 1400, cls: 'cmd',     msg: '> net stop AudioEndpointBuilder...' },
          { delay: 2000, cls: 'cmd',     msg: '> Reiniciando AudioEndpointBuilder...' },
          { delay: 2600, cls: 'cmd',     msg: '> Reiniciando Audiosrv...' },
          { delay: 3200, cls: 'success', msg: '  [OK] Audio de Windows reiniciado. Pruebe sus bocinas.' }
        ]
      }
    };

    const config = actions[action];
    if (!config) return;

    // --- User confirmation: Custom Holographic Modal ---
    const overlay = document.getElementById('it-confirm-overlay');
    const confirmIcon = document.getElementById('it-confirm-icon');
    const confirmTitle = document.getElementById('it-confirm-title');
    const confirmBadge = document.getElementById('it-confirm-badge');
    const confirmLabel = document.getElementById('it-confirm-label');
    const confirmDesc = document.getElementById('it-confirm-desc');
    const confirmOk = document.getElementById('it-confirm-ok');
    const confirmCancel = document.getElementById('it-confirm-cancel');

    // Icon map per action
    const iconMap = { clean:'🗑️', printer:'🖨️', scanner:'📠', network:'🌐', update:'🔄',
      explorer:'🖥️', disco:'💽', ram:'🧠', firewall:'🛡️', wifi:'📶', usb:'🔌',
      audio:'🔊', wifi_boost:'🚀', god:'⚡' };

    const descMap = {
      clean: 'Borra archivos temporales, caché, prefetch y vacía la Papelera para recuperar velocidad y espacio en disco.',
      printer: 'Reinicia el servicio Spooler de Windows y destruye documentos atascados en la cola de impresión.',
      scanner: 'Reinicia los servicios WIA y RPC para destrabar protocolos de digitalización de escáneres.',
      network: 'Libera y renueva la IP, purga la caché DNS y resetea el stack Winsock para arreglar "Sin Internet".',
      update: 'Borra la bóveda SoftwareDistribution corrupta y reinicia los servicios WUAU y BITS de actualización.',
      explorer: 'Mata y reinicia el proceso Explorer.exe para recuperar una barra de tareas o escritorio congelado.',
      disco: 'Ejecuta CHKDSK en la unidad C: para detectar y reparar sectores dañados y errores lógicos del disco.',
      ram: 'Cierra procesos pesados en segundo plano (Teams, OneDrive, Widgets) para liberar memoria RAM inmediatamente.',
      firewall: 'Restaura las reglas del Firewall de Windows a sus valores predeterminados y reactiva la protección.',
      wifi: 'Genera un reporte completo de la red inalámbrica, señal, canales y redes disponibles detectadas.',
      usb: 'Reinicia todos los controladores USB y fuerza la reenumeración de dispositivos no reconocidos.',
      audio: 'Reinicia los servicios de audio de Windows cuando las bocinas o audífonos dejan de funcionar.',
      wifi_boost: 'Optimiza TCP/IP, activa el ancho de banda completo eliminando el límite QoS de Windows, cambia a DNS de alta velocidad (Google 8.8.8.8 + Cloudflare 1.1.1.1) y reduce la latencia del WiFi.',
      god: 'Barrido total institucional: ejecuta los 12 módulos de reparación de forma consecutiva. Limpieza, impresoras, escáneres, red, update, explorer, disco, RAM, firewall, WiFi, USB y audio.'
    };

    confirmIcon.textContent = iconMap[action] || '⚙️';
    confirmTitle.textContent = action === 'god' ? 'MODO DIOS — REPARACIÓN TOTAL' : 'CONFIRMAR OPERACIÓN IT';
    confirmBadge.textContent = action === 'god' ? '⚡ PROTOCOLO EXTREMO' : '🔧 REPARACIÓN DETECTADA';
    confirmLabel.textContent = config.label;
    confirmDesc.textContent = descMap[action] || config.label;

    overlay.classList.remove('hidden');

    // One-time listeners
    function onOk() {
      overlay.classList.add('hidden');
      cleanup();
      proceedWithAction();
    }
    function onCancel() {
      overlay.classList.add('hidden');
      cleanup();
    }
    function cleanup() {
      confirmOk.removeEventListener('click', onOk);
      confirmCancel.removeEventListener('click', onCancel);
    }
    confirmOk.addEventListener('click', onOk);
    confirmCancel.addEventListener('click', onCancel);

    function proceedWithAction() {

    const statusEl = document.getElementById('it-global-status');
    const progEl = config.prog ? document.getElementById(config.prog) : null;
    const btnEl = config.btn ? document.getElementById(config.btn) : null;

    if (btnEl) btnEl.disabled = true;
    if (statusEl) statusEl.textContent = 'EJECUTANDO: ' + config.label;

    // --- Auto-Download the real .bat for each action ---
    const base = import.meta.env.BASE_URL;
    const scriptMap = {
      clean:    base + 'it_limpieza.bat',
      printer:  base + 'it_impresora.bat',
      scanner:  base + 'it_escaner.bat',
      network:  base + 'it_red.bat',
      update:   base + 'it_update.bat',
      explorer: base + 'it_explorer.bat',
      disco:    base + 'it_disco.bat',
      ram:      base + 'it_ram.bat',
      firewall: base + 'it_firewall.bat',
      wifi:     base + 'it_wifi.bat',
      usb:      base + 'it_usb.bat',
      audio:    base + 'it_audio.bat',
      wifi_boost: base + 'it_wifi_boost.bat',
      god:      base + 'Soporte_IT_Andres_Pinto.bat'
    };
    if (scriptMap[action]) {
      setTimeout(function() {
        const a = document.createElement('a');
        a.href = scriptMap[action];
        a.download = scriptMap[action].split('/').pop();
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        // Add a console message about the download
        const dlLine = document.createElement('p');
        dlLine.className = 'console-line warning';
        dlLine.textContent = '> Script descargado. Dale doble-clic y aprueba el escudo de Admin para ejecutarlo.';
        consoleOutput.appendChild(dlLine);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
      }, 800);
    }

if (action === 'god') {
      ['prog-clean','prog-printer','prog-scanner','prog-network','prog-update','prog-explorer',
       'prog-disco','prog-ram','prog-firewall','prog-wifi','prog-wifi_boost','prog-usb','prog-audio'].forEach(function(id) {
        const el = document.getElementById(id);
        if (el) { el.style.width = '0%'; el.style.transition = 'width 5.5s ease'; setTimeout(function() { el.style.width = '100%'; }, 200); }
      });
      setTimeout(function() {
        ['btn-clean','btn-printer','btn-scanner','btn-network','btn-update','btn-explorer',
         'btn-disco','btn-ram','btn-firewall','btn-wifi','btn-usb','btn-audio'].forEach(function(id) {
          const el = document.getElementById(id);
          if (el) { el.disabled = false; el.classList.add('success'); el.textContent = 'COMPLETADO'; }
        });
        if (statusEl) statusEl.textContent = 'MODO DIOS: OPERACION EXITOSA';
      }, 5800);
    }

    const totalDuration = config.steps[config.steps.length - 1].delay + 500;
    consoleOutput.innerHTML = '';

    config.steps.forEach(function(step) {
      setTimeout(function() {
        const line = document.createElement('p');
        line.className = 'console-line ' + step.cls;
        line.textContent = step.msg;
        consoleOutput.appendChild(line);
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
        if (progEl) {
          progEl.style.width = Math.round((step.delay / totalDuration) * 100) + '%';
        }
      }, step.delay);
    });

setTimeout(function() {
      if (progEl) progEl.style.width = '100%';
      if (btnEl) { btnEl.disabled = false; btnEl.classList.add('success'); btnEl.textContent = 'COMPLETADO'; }
      if (statusEl && action !== 'god') statusEl.textContent = 'SISTEMA LISTO';
    }, totalDuration);

    }

  }

}
