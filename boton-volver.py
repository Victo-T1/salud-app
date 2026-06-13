from pathlib import Path

CSS_BOTON = r'''

    /* ── Botón volver al menú principal ── */
    .volver-menu {
      position: fixed;
      right: 18px;
      bottom: 18px;
      z-index: 9999;
      background: #1c2e4a;
      color: #ffffff;
      text-decoration: none;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 14px;
      border-radius: 999px;
      box-shadow: 0 4px 12px rgba(0,0,0,.22);
      transition: background .2s ease, transform .2s ease;
    }

    .volver-menu:hover {
      background: #2e4d7d;
      transform: translateY(-2px);
    }

    @media print {
      .volver-menu { display: none; }
    }
'''

HTML_BOTON = '\n<a class="volver-menu" href="../index.html">← Volver al menú principal</a>\n'

ARCHIVOS = [
    Path("modulo-1-pscv/index.html"),
    Path("modulo-2-ecicep/index.html"),
    Path("modulo-3-personas-mayores/index.html"),
    Path("modulo-4-padds-paliativos/index.html"),
]


def modificar_archivo(ruta: Path) -> None:
    if not ruta.exists():
        print(f"NO ENCONTRADO: {ruta}")
        return

    html = ruta.read_text(encoding="utf-8")

    if ".volver-menu" not in html:
        html = html.replace("</style>", CSS_BOTON + "\n</style>", 1)

    if 'class="volver-menu"' not in html:
        html = html.replace("<body>", "<body>" + HTML_BOTON, 1)

    ruta.write_text(html, encoding="utf-8")
    print(f"MODIFICADO: {ruta}")


def main() -> None:
    for archivo in ARCHIVOS:
        modificar_archivo(archivo)

    print("\nListo. Abre index.html principal con Live Server o en tu navegador.")


if __name__ == "__main__":
    main()