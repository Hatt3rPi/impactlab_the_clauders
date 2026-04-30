(function () {
  "use strict";

  const BTN_CLASS = "diagram-fullscreen-btn";
  const WRAP_CLASS = "diagram-fullscreen-wrap";
  const MODAL_ID = "diagram-fullscreen-modal";

  function ensureModal() {
    let modal = document.getElementById(MODAL_ID);
    if (modal) return modal;

    modal = document.createElement("div");
    modal.id = MODAL_ID;
    modal.className = "dfs-modal";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.setAttribute("aria-hidden", "true");
    modal.innerHTML =
      '<div class="dfs-toolbar">' +
        '<button type="button" class="dfs-btn" data-action="zoom-out" title="Alejar (−)" aria-label="Alejar">−</button>' +
        '<button type="button" class="dfs-btn" data-action="reset" title="Restablecer (0)" aria-label="Restablecer">⟳</button>' +
        '<button type="button" class="dfs-btn" data-action="zoom-in" title="Acercar (+)" aria-label="Acercar">+</button>' +
        '<span class="dfs-hint">Arrastra para desplazar · rueda para zoom · Esc para cerrar</span>' +
        '<button type="button" class="dfs-btn dfs-close" data-action="close" title="Cerrar (Esc)" aria-label="Cerrar">✕</button>' +
      '</div>' +
      '<div class="dfs-stage">' +
        '<div class="dfs-canvas"></div>' +
      '</div>';
    document.body.appendChild(modal);

    const stage = modal.querySelector(".dfs-stage");
    const canvas = modal.querySelector(".dfs-canvas");

    let scale = 1;
    let tx = 0;
    let ty = 0;
    let dragging = false;
    let startX = 0;
    let startY = 0;
    let startTx = 0;
    let startTy = 0;

    function apply() {
      canvas.style.transform =
        "translate(" + tx + "px," + ty + "px) scale(" + scale + ")";
    }

    function reset() {
      const stageRect = stage.getBoundingClientRect();
      const cw = canvas.offsetWidth || 1;
      const ch = canvas.offsetHeight || 1;
      const fitScale = Math.min(
        (stageRect.width * 0.92) / cw,
        (stageRect.height * 0.92) / ch,
        1
      );
      scale = Math.max(0.2, fitScale);
      tx = (stageRect.width - cw * scale) / 2;
      ty = (stageRect.height - ch * scale) / 2;
      apply();
    }

    function zoomAt(factor, cx, cy) {
      const rect = stage.getBoundingClientRect();
      const px = (cx === undefined ? rect.width / 2 : cx - rect.left);
      const py = (cy === undefined ? rect.height / 2 : cy - rect.top);
      const newScale = Math.min(8, Math.max(0.2, scale * factor));
      const k = newScale / scale;
      tx = px - k * (px - tx);
      ty = py - k * (py - ty);
      scale = newScale;
      apply();
    }

    stage.addEventListener("wheel", function (e) {
      e.preventDefault();
      const factor = e.deltaY < 0 ? 1.15 : 1 / 1.15;
      zoomAt(factor, e.clientX, e.clientY);
    }, { passive: false });

    stage.addEventListener("mousedown", function (e) {
      if (e.button !== 0) return;
      dragging = true;
      startX = e.clientX;
      startY = e.clientY;
      startTx = tx;
      startTy = ty;
      stage.classList.add("dfs-dragging");
    });

    window.addEventListener("mousemove", function (e) {
      if (!dragging) return;
      tx = startTx + (e.clientX - startX);
      ty = startTy + (e.clientY - startY);
      apply();
    });

    window.addEventListener("mouseup", function () {
      if (!dragging) return;
      dragging = false;
      stage.classList.remove("dfs-dragging");
    });

    let pinchDist = 0;
    let pinchScale = 1;
    stage.addEventListener("touchstart", function (e) {
      if (e.touches.length === 2) {
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        pinchDist = Math.hypot(dx, dy);
        pinchScale = scale;
      } else if (e.touches.length === 1) {
        dragging = true;
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        startTx = tx;
        startTy = ty;
      }
    }, { passive: true });

    stage.addEventListener("touchmove", function (e) {
      if (e.touches.length === 2) {
        const dx = e.touches[0].clientX - e.touches[1].clientX;
        const dy = e.touches[0].clientY - e.touches[1].clientY;
        const d = Math.hypot(dx, dy);
        if (pinchDist > 0) {
          const factor = (d / pinchDist) * (pinchScale / scale);
          const cx = (e.touches[0].clientX + e.touches[1].clientX) / 2;
          const cy = (e.touches[0].clientY + e.touches[1].clientY) / 2;
          zoomAt(factor, cx, cy);
        }
        e.preventDefault();
      } else if (e.touches.length === 1 && dragging) {
        tx = startTx + (e.touches[0].clientX - startX);
        ty = startTy + (e.touches[0].clientY - startY);
        apply();
      }
    }, { passive: false });

    stage.addEventListener("touchend", function () {
      dragging = false;
      pinchDist = 0;
    });

    modal.addEventListener("click", function (e) {
      const action = e.target && e.target.getAttribute && e.target.getAttribute("data-action");
      if (action === "close" || e.target === modal) {
        close();
      } else if (action === "zoom-in") {
        zoomAt(1.25);
      } else if (action === "zoom-out") {
        zoomAt(1 / 1.25);
      } else if (action === "reset") {
        reset();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (modal.getAttribute("aria-hidden") === "true") return;
      if (e.key === "Escape") close();
      else if (e.key === "+" || e.key === "=") zoomAt(1.25);
      else if (e.key === "-" || e.key === "_") zoomAt(1 / 1.25);
      else if (e.key === "0") reset();
    });

    function open(node) {
      canvas.innerHTML = "";
      const clone = node.cloneNode(true);
      clone.removeAttribute("style");
      const svg = clone.tagName && clone.tagName.toLowerCase() === "svg" ? clone : (clone.querySelector && clone.querySelector("svg"));
      if (svg) {
        const vb = svg.getAttribute("viewBox");
        let nw = parseFloat(svg.getAttribute("width"));
        let nh = parseFloat(svg.getAttribute("height"));
        if ((!nw || !nh) && vb) {
          const parts = vb.split(/\s+/);
          if (parts.length === 4) {
            nw = nw || parseFloat(parts[2]);
            nh = nh || parseFloat(parts[3]);
          }
        }
        svg.removeAttribute("style");
        if (nw) svg.setAttribute("width", nw);
        if (nh) svg.setAttribute("height", nh);
        svg.style.maxWidth = "none";
        svg.style.maxHeight = "none";
      }
      canvas.appendChild(clone);
      modal.setAttribute("aria-hidden", "false");
      document.documentElement.classList.add("dfs-open");
      requestAnimationFrame(function () {
        if (clone.tagName && clone.tagName.toLowerCase() === "img" && !clone.complete) {
          clone.addEventListener("load", reset, { once: true });
          reset();
        } else {
          reset();
        }
      });
    }

    function close() {
      modal.setAttribute("aria-hidden", "true");
      document.documentElement.classList.remove("dfs-open");
      canvas.innerHTML = "";
    }

    modal._dfsOpen = open;
    modal._dfsClose = close;
    return modal;
  }

  function makeButton() {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = BTN_CLASS;
    btn.title = "Ver en pantalla completa";
    btn.setAttribute("aria-label", "Ver en pantalla completa");
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">' +
        '<path fill="currentColor" d="M5 5h5V3H3v7h2V5zm9-2v2h5v5h2V3h-7zM5 14H3v7h7v-2H5v-5zm14 5h-5v2h7v-7h-2v5z"/>' +
      '</svg>';
    return btn;
  }

  function enhance(el, getTarget) {
    if (!el || el.dataset.dfsReady === "1") return;
    if (el.closest && el.closest(".dfs-canvas")) return;

    const cs = window.getComputedStyle(el);
    if (cs.position === "static") el.style.position = "relative";
    el.classList.add(WRAP_CLASS);

    const btn = makeButton();
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      const target = getTarget();
      if (!target) return;
      const modal = ensureModal();
      modal._dfsOpen(target);
    });
    el.appendChild(btn);
    el.dataset.dfsReady = "1";
  }

  function scan(root) {
    root = root || document;
    const mermaids = root.querySelectorAll(".mermaid");
    mermaids.forEach(function (m) {
      if (!m.querySelector("svg")) return;
      enhance(m, function () { return m.querySelector("svg") || m; });
    });

    const imgs = root.querySelectorAll(".md-content img");
    imgs.forEach(function (img) {
      if (img.closest(".md-header") || img.closest(".md-footer")) return;
      if (img.width && img.width < 80) return;
      const wrap = document.createElement("span");
      wrap.className = "dfs-img-wrap";
      if (img.parentNode === null || img.dataset.dfsImgReady === "1") return;
      img.dataset.dfsImgReady = "1";
      img.parentNode.insertBefore(wrap, img);
      wrap.appendChild(img);
      enhance(wrap, function () { return img; });
    });
  }

  function scanWhenReady() {
    let attempts = 0;
    const tick = function () {
      scan();
      attempts++;
      if (attempts < 20) setTimeout(tick, 250);
    };
    tick();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () { scanWhenReady(); });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scanWhenReady);
  } else {
    scanWhenReady();
  }
})();
