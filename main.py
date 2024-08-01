import segno


# Create a main function to encapsulates every statements
def main() -> None:
    qrcode1 = segno.make_qr("Hello QR!")
    qrcode1.save("qr-picture/qr_pertamaku.png",scale=10)

    # Added another qrcode object, but without the quiet zone (the white border)
    # In general, a QR code without the quiet zone (the white border) is generally discouraged
    qrcode2 = segno.make_qr("Hello QR! Without the quiet zone.")
    qrcode2.save("qr-picture/qr_keduaku.png",scale=5,border=0)

    # Change the colors of the QR code
    qrcode3 = segno.make_qr("Hello QR! With a background color.")
    qrcode3.save(
        "qr-picture/custom_qr_ketiga.png",
        scale=10,
        border=5,
        light="lightblue",
        dark="darkgreen")

    # Change the colors of the quiet zone
    qrcode4 = segno.make_qr("Hello QR! With custom color quiet zone.")
    qrcode4.save(
        "qr-picture/custom_qr_keempat.png",
        scale=10,
        border=3,
        dark="yellow",
        quiet_zone="lightgreen"
        )
    
    # Change the `data_light=` and `data_dark=` parameters (keyword argumentse)
    qrcode5 = segno.make_qr("Hello QR!")
    qrcode5.save("qr-picture/custom_qr_kelima.png",scale=5,border=3,data_light="lightgreen",data_dark="red")

# Create a top-level code environment
if __name__ == '__main__':
    main()