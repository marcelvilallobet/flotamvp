from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("icons", exist_ok=True)

def make_icon(size):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Fondo redondeado azul
    radius = int(size * 0.21)
    bg_color = (26, 115, 232, 255)  # #1a73e8
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=bg_color)

    # Cuerpo del vehiculo (rectangulo blanco)
    x0 = int(size * 0.15)
    y0 = int(size * 0.45)
    x1 = int(size * 0.85)
    y1 = int(size * 0.72)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=int(size*0.05), fill=(255,255,255,255))

    # Cabina (rectangulo blanco mas pequeno arriba a la derecha)
    cx0 = int(size * 0.45)
    cy0 = int(size * 0.28)
    cx1 = int(size * 0.85)
    cy1 = int(size * 0.50)
    draw.rounded_rectangle([cx0, cy0, cx1, cy1], radius=int(size*0.04), fill=(255,255,255,210))

    # Ruedas
    wheel_r = int(size * 0.10)
    wheel_color = (255, 255, 255, 255)
    inner_color = bg_color

    for cx in [int(size*0.30), int(size*0.70)]:
        cy = int(size * 0.73)
        draw.ellipse([cx-wheel_r, cy-wheel_r, cx+wheel_r, cy+wheel_r], fill=wheel_color)
        inner = int(wheel_r * 0.5)
        draw.ellipse([cx-inner, cy-inner, cx+inner, cy+inner], fill=inner_color)

    # Letra F en el cuerpo
    try:
        font_size = int(size * 0.28)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "F"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = x0 + int((x1 - x0 - tw) / 2) - int(size * 0.05)
    ty = y0 + int((y1 - y0 - th) / 2) - bbox[1]
    draw.text((tx, ty), text, fill=bg_color, font=font)

    return img

for size in [192, 512]:
    icon = make_icon(size)
    path = f"icons/icon-{size}.png"
    icon.save(path, "PNG")
    print(f"Generado: {path}")

print("Iconos creados correctamente.")
