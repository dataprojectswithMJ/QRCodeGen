import streamlit as st
import qrcode
import random


def main():
    st.image('QRcode_Gen.png')
    st.title("")

    st.header('About this project:')

    st.markdown("This is a open source web application to make generating QR codes much easier. Built using Python, "
                "[Streamlit](https://streamlit.io) and QRCode.")
    st.markdown("[Github link](https://github.com/dataprojectswithMJ) for those who would like to contribute and "
                "improve this project even further")
    st.markdown("[Email me](mailto:kubeka7712@gmail.com), DM me on [LinkedIn](https://linkedin.com/in/mpho-jan-kubeka) "
                "or [Twitter](https://twitter.com/MphoJKubeka) if you want to work with me. I'm open to new things")

    st.title("")

    st.header('Generate code')

    data = st.text_area('What do you want to encode?')
    filename = f'code_{random.randint(1000, 999999)}.png'
    encrypt = st.button('Generate QR code')

    if encrypt:
        img = qrcode.make(data)
        img.save(filename)
        st.image(filename)

        with open(filename, "rb") as file:
            btn = st.download_button(
                label="Download QR code",
                data=file,
                file_name=filename,
                mime="image/png"
            )
    return


if __name__ == '__main__':
    main()