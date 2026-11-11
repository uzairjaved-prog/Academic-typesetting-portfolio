"""Render compact, client-facing preview images from the generated PDF samples."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]


def render_first_page(pdf: Path, output_prefix: Path) -> Path:
    """Render the first PDF page to an optimized JPEG using Poppler."""
    subprocess.run(
        [
            "pdftoppm",
            "-f", "1",
            "-l", "1",
            "-singlefile",
            "-scale-to-x", "760",
            "-scale-to-y", "-1",
            "-jpeg",
            "-jpegopt", "quality=68,progressive=y,optimize=y",
            str(pdf),
            str(output_prefix),
        ],
        check=True,
    )
    return output_prefix.with_suffix(".jpg")


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load a predictable font on Linux CI, falling back to Pillow's default."""
    filename = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    candidates = [
        Path("/usr/share/fonts/truetype/dejavu") / filename,
        Path("/usr/share/fonts/dejavu") / filename,
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def make_overview(preview_dir: Path) -> Path:
    """Compose the four generated samples into one README-friendly overview."""
    width, height = 1440, 1220
    background = (244, 247, 251)
    ink = (25, 42, 67)
    canvas = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(34, bold=True)
    subtitle_font = load_font(19)
    label_font = load_font(17, bold=True)
    draw.rectangle((0, 0, width, 160), fill=ink)
    draw.text((70, 38), "ACADEMIC TYPESETTING PORTFOLIO", font=title_font, fill="white")
    draw.text(
        (72, 92),
        "LaTeX  •  TikZ / PGFPlots  •  Thesis layouts  •  Scientific figures",
        font=subtitle_font,
        fill=(220, 230, 244),
    )

    items = [
        ("JOURNAL PAPER", "paper-page-1.jpg"),
        ("THESIS LAYOUT", "thesis-cover.jpg"),
        ("TIKZ / PGFPLOTS", "tikz-gallery.jpg"),
        ("SCIENTIFIC FIGURES", "scientific-figures.jpg"),
    ]
    margin, gap = 65, 35
    card_width = (width - 2 * margin - gap) // 2
    card_height = 470
    positions = [
        (margin, 210),
        (margin + card_width + gap, 210),
        (margin, 210 + card_height + gap),
        (margin + card_width + gap, 210 + card_height + gap),
    ]

    for (label, filename), (x, y) in zip(items, positions):
        draw.rounded_rectangle(
            (x, y, x + card_width, y + card_height),
            radius=18,
            fill=(255, 255, 255),
            outline=(218, 225, 235),
            width=2,
        )
        draw.text((x + 24, y + 18), label, font=label_font, fill=ink)
        draw.rounded_rectangle(
            (x + 18, y + 56, x + card_width - 18, y + card_height - 18),
            radius=10,
            fill=(250, 251, 253),
        )
        image = Image.open(preview_dir / filename).convert("RGB")
        image.thumbnail((card_width - 45, card_height - 82), Image.Resampling.LANCZOS)
        image_x = x + (card_width - image.width) // 2
        image_y = y + 64 + (card_height - 82 - image.height) // 2
        canvas.paste(image, (image_x, image_y))

    output = preview_dir / "portfolio-overview.jpg"
    canvas.save(output, "JPEG", quality=72, optimize=True, progressive=True)
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist" / "previews")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    samples = [
        ("paper.pdf", "paper-page-1"),
        ("thesis.pdf", "thesis-cover"),
        ("tikz-showcase.pdf", "tikz-gallery"),
    ]
    for pdf_name, output_name in samples:
        pdf_path = args.pdf_dir / pdf_name
        if not pdf_path.is_file():
            raise FileNotFoundError(f"Missing PDF sample: {pdf_path}")
        render_first_page(pdf_path, args.output_dir / output_name)

    figure_path = ROOT / "figures" / "fig_multipanel.png"
    if not figure_path.is_file():
        raise FileNotFoundError(f"Missing scientific figure: {figure_path}")
    figure = Image.open(figure_path).convert("RGB")
    figure.thumbnail((760, 560), Image.Resampling.LANCZOS)
    figure.save(
        args.output_dir / "scientific-figures.jpg",
        "JPEG",
        quality=68,
        optimize=True,
        progressive=True,
    )

    overview = make_overview(args.output_dir)
    print(f"Created portfolio previews in {args.output_dir}")
    print(f"Overview: {overview}")


if __name__ == "__main__":
    main()
