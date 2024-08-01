import segno


# Create a main function to encapsulates every statements
def main() -> None:
    qrcode = segno.make_qr("Hello Qr!")
    qrcode.save("qr_pertamaku.png",scale=10)

# Create a top-level code environment
if __name__ == '__main__':
    main()