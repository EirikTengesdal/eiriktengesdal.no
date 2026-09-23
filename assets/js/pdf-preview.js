// Inline PDF preview that works in desktop and mobile browsers (mobile browsers download PDFs
// instead of showing them in an <iframe>). Every <div class="pdf-preview" data-pdf="..."> is
// replaced by one canvas per page, rendered with Mozilla's PDF.js from cdnjs – the same library
// Zenodo uses for its previews. The download link next to the preview stays the fallback.
import * as pdfjsLib from "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/6.3.289/pdf.min.mjs";

pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/6.3.289/pdf.worker.min.mjs";

async function render(el) {
  const url = el.dataset.pdf;
  if (!url) return;
  try {
    const pdf = await pdfjsLib.getDocument({ url }).promise;
    el.replaceChildren();
    const width = el.clientWidth || 800;
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const base = page.getViewport({ scale: 1 });
      const viewport = page.getViewport({ scale: (width / base.width) * dpr });
      const canvas = document.createElement("canvas");
      canvas.className = "pdf-page";
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      canvas.setAttribute("role", "img");
      canvas.setAttribute("aria-label", `${el.dataset.label || "PDF"} – page ${i} of ${pdf.numPages}`);
      el.appendChild(canvas);
      await page.render({ canvasContext: canvas.getContext("2d"), viewport }).promise;
    }
    const note = document.createElement("p");
    note.className = "pdf-preview-note text-muted small";
    note.textContent = `${pdf.numPages} ${pdf.numPages === 1 ? "page" : "pages"}`;
    el.appendChild(note);
  } catch (err) {
    console.error("pdf-preview:", err);
    el.replaceChildren();
    const p = document.createElement("p");
    p.className = "text-muted small";
    p.textContent = el.dataset.fallback || "The PDF could not be shown here – use the download link above.";
    el.appendChild(p);
  }
}

document.querySelectorAll(".pdf-preview").forEach(render);
