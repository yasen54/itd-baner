def generate_js(pixels):
    out = [
        "(function(){",
        "  const canvas = document.querySelector('.drawing-canvas');",
        "  if (!canvas) { console.error('Canvas not found'); return; }",
        "  const ctx = canvas.getContext('2d');"
    ]

    for x, y, w, h, color in pixels:
        out.append(f'  ctx.fillStyle = "{color}";')
        out.append(f'  ctx.fillRect({x}, {y}, {w}, {h});')

    out.append("})();")
    return "\n".join(out)
