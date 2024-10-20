# pip install reportlab

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib import colors

def get_user_input():
    """
    Fordert den Benutzer auf, die Start- und Endnummer sowie die Anzahl der Spalten und Zeilen einzugeben.
    """
    while True:
        try:
            start = int(input("Starting Number: "))
            end = int(input("Ending Number: "))
            if start > end:
                print("Starting number must be smaller than ending number. Please try again!")
                continue
            cols = int(input("Number of columns on A4 Paper: "))
            rows = int(input("Number of rows on A4 Paper: "))
            if cols <= 0 or rows <= 0:
                print("Number of columns and rows must be greater than 0. Please try again!")
                continue
            output_filename=f"ASNLabels_{start}to{end}_{cols}x{rows}_bracodes.pdf"
            return start, end, cols, rows, output_filename
        except ValueError:
            print("Bitte gib gültige ganze Zahlen ein.")

def calculate_sheets(total_labels, labels_per_sheet):
    """
    Berechnet die benötigte Anzahl an Bögen basierend auf der Gesamtanzahl der Etiketten und der Anzahl der Etiketten pro Blatt.
    """
    return math.ceil(total_labels / labels_per_sheet)

def create_labels_pdf(start, end, cols, rows, output_filename):
    """
    Erstellt eine PDF-Datei mit den generierten Etiketten basierend auf dem angegebenen Bereich und Layout.
    """
    # Seiten- und Etikettengröße
    page_width, page_height = A4
    labels_per_sheet = cols * rows
    label_width = page_width / cols
    label_height = page_height / rows

    total_labels = end - start + 1
    total_sheets = calculate_sheets(total_labels, labels_per_sheet)
    print(f"Sheets of lables needed: {total_sheets}")

    c = canvas.Canvas(output_filename, pagesize=A4)

    for i in range(start, end + 1):
        label_index = i - start
        position_in_sheet = label_index % labels_per_sheet
        col = position_in_sheet % cols
        row = position_in_sheet // cols

        # Position berechnen (von oben links)
        x = col * label_width
        y = page_height - (row + 1) * label_height

        # Innerer Etikettenrahmen (3mm Rand)
        inner_margin = 3 * mm
        inner_x = x + inner_margin
        inner_y = y + inner_margin
        inner_width = label_width - 2 * inner_margin
        inner_height = label_height - 2 * inner_margin

        # Barcode- und Textabmessungen
        desired_barcode_width = inner_width
        desired_barcode_height = inner_height * 0.6  # 60% der inneren Etikettenhöhe

        # Formatierte Nummer mit führenden Nullen
        barcode_value = f"ASN{i:06d}"  # Formatierung mit führenden Nullen
        text = barcode_value

        # Erstellen des Barcodes mit einem initialen barWidth
        initial_barWidth = 0.5  # mm
        barcode = code128.Code128(barcode_value, barHeight=desired_barcode_height, barWidth=initial_barWidth)

        # Berechnen des Skalierungsfaktors, um den Barcode an die gewünschte Breite anzupassen
        scaling_factor = desired_barcode_width / barcode.width

        # Limitieren des Skalierungsfaktors, um Übergrößen zu vermeiden
        max_scaling = 5  # Maximaler Skalierungsfaktor
        if scaling_factor > max_scaling:
            scaling_factor = max_scaling

        # Berechnung des endgültigen barWidth
        final_barWidth = initial_barWidth * scaling_factor
        barcode = code128.Code128(barcode_value, barHeight=desired_barcode_height, barWidth=final_barWidth)

        # Aktualisierte Positionierung, um den Barcode zu zentrieren
        barcode_width = barcode.width
        barcode_x = inner_x + (inner_width - barcode_width) / 2
        barcode_y = inner_y + (inner_height - desired_barcode_height)

        # Zeichnen des Barcodes
        try:
            barcode.drawOn(c, barcode_x, barcode_y)
        except Exception as e:
            print(f"Issue while rendeering barcode with number {barcode_value}: {e}")

        # Berechnung der Textposition, um ihn zu zentrieren
        c.setFont("Helvetica", 10)
        text_width = c.stringWidth(text, "Helvetica", 10)
        text_x = inner_x + (inner_width - text_width) / 2
        text_y = inner_y + 3 * mm  # 3mm Abstand vom unteren Rand

        # Zeichnen des zentrierten Textes
        c.setFillColor(colors.black)
        c.drawString(text_x, text_y, text)

        # Rahmen um jedes Etikett (für bessere Trennung beim Drucken)
        c.setStrokeColor(colors.lightgrey)
        c.rect(inner_x, inner_y, inner_width, inner_height, stroke=1, fill=0)

        # Neue Seite beginnen, wenn ein Blatt voll ist
        if (i - start + 1) % labels_per_sheet == 0 and (i - start + 1) != total_labels:
            c.showPage()

    c.save()
    print(f"PDF '{output_filename}' was generated sucessfully!")

def main():
    start, end, cols, rows, output_filename = get_user_input()
    create_labels_pdf(start, end, cols, rows, output_filename)

if __name__ == "__main__":
    main()
